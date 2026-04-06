from abc import ABC, abstractmethod
from typing import Any, Union, List, Dict, Tuple


# =========================
# Base Abstract Class
# =========================
class DataProcessor(ABC):

    def __init__(self):
        self.data: List[str] = []

    @abstractmethod
    def validate(self, data: Any) -> bool:
        """Check if data is acceptable for this processor"""
        pass

    @abstractmethod
    def ingest(self, data: Any) -> None:
        """Ingest data after validation. Raise exception if invalid"""
        pass

    def output(self) -> Tuple[int, str]:
        """Extract the oldest item and its rank"""
        if not self.data:
            raise IndexError("No data to output")
        value = self.data.pop(0)
        return len(self.data), value


# =========================
# Numeric Processor
# =========================
class NumericProcessor(DataProcessor):

    def validate(self, data: Any) -> bool:
        if isinstance(data, (int, float)):
            return True
        if isinstance(data, list) and all(isinstance(x, (int, float)) for x in data):
            return True
        return False

    def ingest(self, data: Union[int, float, List[Union[int, float]]]) -> None:
        if not self.validate(data):
            raise ValueError("Improper numeric data")
        if isinstance(data, list):
            self.data.extend(str(x) for x in data)
        else:
            self.data.append(str(data))


# =========================
# Text Processor
# =========================
class TextProcessor(DataProcessor):

    def validate(self, data: Any) -> bool:
        if isinstance(data, str):
            return True
        if isinstance(data, list) and all(isinstance(x, str) for x in data):
            return True
        return False

    def ingest(self, data: Union[str, List[str]]) -> None:
        if not self.validate(data):
            raise ValueError("Improper text data")
        if isinstance(data, list):
            self.data.extend(data)
        else:
            self.data.append(data)


# =========================
# Log Processor
# =========================
class LogProcessor(DataProcessor):

    def validate(self, data: Any) -> bool:
        if isinstance(data, dict):
            return "log_level" in data and "log_message" in data
        if isinstance(data, list):
            return all(
                isinstance(x, dict) and "log_level" in x and "log_message" in x
                for x in data
            )
        return False

    def ingest(self, data: Union[Dict[str, str], List[Dict[str, str]]]) -> None:
        if not self.validate(data):
            raise ValueError("Improper log data")
        if isinstance(data, list):
            self.data.extend(
                f"{x['log_level']}: {x['log_message']}" for x in data
            )
        else:
            self.data.append(f"{data['log_level']}: {data['log_message']}")


# =========================
# DEMO / TESTING
# =========================
if __name__ == "__main__":

    print("=== Code Nexus - Data Processor ===")

    # Numeric Processor
    print("Testing Numeric Processor...")
    numeric = NumericProcessor()
    print("Trying to validate input '42':", numeric.validate(42))
    print("Trying to validate input 'Hello':", numeric.validate("Hello"))
    print("Test invalid ingestion of string 'foo' without prior validation:")
    try:
        numeric.ingest("foo")
    except Exception as e:
        print("Got exception:", e)

    print("Processing data: [1, 2, 3, 4, 5]")
    numeric.ingest([1, 2, 3, 4, 5])
    print("Extracting 3 values...")
    for i in range(3):
        rank, value = numeric.output()
        print(f"Numeric value {i}: {value}")

    # Text Processor
    print("Testing Text Processor...")
    text = TextProcessor()
    print("Trying to validate input '42':", text.validate(42))
    print("Processing data: ['Hello', 'Nexus', 'World']")
    text.ingest(["Hello", "Nexus", "World"])
    print("Extracting 1 value...")
    rank, value = text.output()
    print(f"Text value 0: {value}")

    # Log Processor
    print("Testing Log Processor...")
    log = LogProcessor()
    print("Trying to validate input 'Hello':", log.validate("Hello"))
    logs_data = [
        {"log_level": "NOTICE", "log_message": "Connection to server"},
        {"log_level": "ERROR", "log_message": "Unauthorized access!!"}
    ]
    print("Processing data:", logs_data)
    log.ingest(logs_data)
    print("Extracting 2 values...")
    for i in range(2):
        rank, value = log.output()
        print(f"Log entry {i}: {value}")