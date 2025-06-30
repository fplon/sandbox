"""
Maybe a better example...
"""

from typing import Dict, Any
import csv
import json


# Existing interface representing financial data in JSON format
class JSONFinancialData:
    def load_json_data(self, file_path: str) -> Dict[str, Any]:
        # Load JSON data from file (mock implementation)
        with open(file_path, "r") as file:
            return json.load(file)


# Target interface expected by the client
class CSVFinancialData:
    def load_csv_data(self, file_path: str) -> Dict[str, Any]:
        # Load CSV data from file (mock implementation)
        with open(file_path, "r") as file:
            return [row for row in csv.reader(file)]


# Adapter class to adapt JSONFinancialData interface to CSVFinancialData interface
class JSONToCSVAdapter(CSVFinancialData):
    def __init__(self, json_data: JSONFinancialData):
        self.json_data = json_data

    def load_csv_data(self, file_path: str) -> Dict[str, Any]:
        # Load JSON data using existing interface and convert to CSV format
        json_data = self.json_data.load_json_data(file_path)
        csv_data = self._convert_to_csv(json_data)
        return csv_data

    def _convert_to_csv(self, json_data: Dict[str, Any]) -> Dict[str, Any]:
        csv_data = []
        # Assuming each JSON object represents a financial record
        # Convert JSON data to CSV format
        headers = list(json_data[0].keys())  # Extract headers from the first record
        csv_data.append(headers)
        for record in json_data:
            csv_data.append([str(record[header]) for header in headers])
        return csv_data


# Example usage
def main():
    json_data = JSONFinancialData()
    adapter = JSONToCSVAdapter(json_data)
    csv_data = adapter.load_csv_data("financial_data.json")
    for row in csv_data:
        print(",".join(row))


if __name__ == "__main__":
    main()
