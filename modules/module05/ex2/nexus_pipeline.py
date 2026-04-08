from abc import ABC, abstractmethod
from typing import Any, Protocol


# =========================
# Base Processor
# =========================
class DataProcessor(ABC):

    def __init__(self):
        self.data = []
        self.total_processed = 0

    @abstractmethod
    def validate(self, data: Any) -> bool:
        pass

    @abstractmethod
    def ingest(self, data: Any) -> None:
        pass

    def output(self, n: int) -> list[tuple[int, Any]]:
        result = [(i, self.data[i]) for i in range(min(n, len(self.data)))]
        self.data = self.data[n:]
        return result


# =========================
# Processors
# =========================
class NumericProcessor(DataProcessor):

    def validate(self, data: Any) -> bool:
        return (
            isinstance(data, list)
            and all(isinstance(i, (int, float)) for i in data)
        )

    def ingest(self, data: Any) -> None:
        if not self.validate(data):
            return

        self.data.extend(data)
        self.total_processed += len(data)


class TextProcessor(DataProcessor):

    def validate(self, data: Any) -> bool:
        return isinstance(data, str)

    def ingest(self, data: Any) -> None:
        if not self.validate(data):
            return

        self.data.append(data)
        self.total_processed += 1


class LogProcessor(DataProcessor):

    def validate(self, data: Any) -> bool:
        return (
            isinstance(data, dict)
            and "log_level" in data
            and "log_message" in data
        )

    def ingest(self, data: Any) -> None:
        if not self.validate(data):
            return

        self.data.append(data)
        self.total_processed += 1


# =========================
# Export Plugin (Protocol)
# =========================
class ExportPlugin(Protocol):
    def process_output(self, data: list[tuple[int, Any]]) -> None:
        ...


# =========================
# CSV Plugin
# =========================
class CSVExportPlugin:

    def process_output(self, data: list[tuple[int, Any]]) -> None:
        print("id,value")
        for idx, value in data:
            print(f"{idx},{value}")


# =========================
# JSON Plugin
# =========================
class JSONExportPlugin:

    def process_output(self, data: list[tuple[int, Any]]) -> None:
        print("[")
        for i, (idx, value) in enumerate(data):
            comma = "," if i < len(data) - 1 else ""
            print(f'  {{"id": {idx}, "value": "{value}"}}{comma}')
        print("]")


# =========================
# Data Stream
# =========================
class DataStream:

    def __init__(self):
        self.processors = []

    def register(self, processor: DataProcessor):
        self.processors.append(processor)

    def send(self, batch):
        for item in batch:
            processed = False

            for processor in self.processors:
                if processor.validate(item):
                    processor.ingest(item)
                    processed = True
                    break

            if not processed:
                print(
                    f"DataStream error - Can't process element in stream: {item}"
                )

    def output_pipeline(self, nb: int, plugin: ExportPlugin) -> None:
        all_data = []

        for processor in self.processors:
            data = processor.output(nb)
            all_data.extend(data)

        plugin.process_output(all_data)


if __name__ == "__main__":

    stream = DataStream()

    numeric = NumericProcessor()
    text = TextProcessor()
    log = LogProcessor()

    stream.register(numeric)
    stream.register(text)
    stream.register(log)

    batch = [
        "Hello world",
        [1, 2, 3],
        {"log_level": "INFO", "log_message": "System ready"},
    ]

    stream.send(batch)

    print("\n=== CSV Export ===")
    stream.output_pipeline(2, CSVExportPlugin())

    print("\n=== JSON Export ===")
    stream.output_pipeline(2, JSONExportPlugin())
