from abc import ABC, abstractmethod
from typing import Any


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

    def output(self, n: int) -> list:
        result = self.data[:n]
        self.data = self.data[n:]
        return result


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
                    f"DataStream error-Can't process element in stream: {item}"
                )

    def stats(self):
        print("== DataStream statistics ==")

        if not self.processors:
            print("No processor found, no data")
            return

        for p in self.processors:
            name = p.__class__.__name__.replace("Processor", " Processor")
            print(
                f"{name}: total {p.total_processed} items processed, "
                f"remaining {len(p.data)} on processor"
            )


print("=== Code Nexus - Data Stream ===")
print("Initialize Data Stream...")

stream = DataStream()
stream.stats()

print("Registering Numeric Processor")
numeric = NumericProcessor()
stream.register(numeric)

txt0 = "Telnet access! Use ssh instead"
batch = [
    "Hello world",
    [3.14, -1, 2.71],
    [
        {"log_level": "WARNING", "log_message": txt0},
        {"log_level": "INFO", "log_message": "User wil is connected"},
    ],
    42,
    ["Hi", "five"],
]

print(f"Send first batch of data on stream: {batch}")
stream.send(batch)

stream.stats()

print("Registering other data processors")
text = TextProcessor()
log = LogProcessor()

stream.register(text)
stream.register(log)

print("Send the same batch again")
stream.send(batch)

stream.stats()

txt1 = "Consume some elements from the data processors:"
num_n = 3
text_n = 2
log_n = 1

print(
    f"{txt1} Numeric {num_n}, "
    f"Text {text_n}, Log {log_n}"
)

numeric.output(num_n)
text.output(text_n)
log.output(log_n)

stream.stats()
