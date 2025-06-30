"""
- We introduced an abstract base class ReportGenerator with an abstract method generate_report,
defining the interface for generating reports.
- We created concrete subclasses PDFReportGenerator, CSVReportGenerator, and HTMLReportGenerator,
each implementing the generate_report method for a specific report format.
- We can easily extend the behavior of the ReportGenerator class by adding new subclasses for other
report formats (e.g., JSON, Excel) without modifying the existing code. This adheres to the Open-Closed
Principle, as the behavior is open for extension (we can add new report generators) but closed for
modification (we don't need to modify existing code to add new generators).

By adhering to the Open-Closed Principle, our code becomes more maintainable, modular, and flexible,
as it allows for easy extension without risking the stability of existing functionality. This approach
also facilitates better separation of concerns and promotes code reusability.
"""

from abc import ABC, abstractmethod
from typing import Any


class ReportGenerator(ABC):
    @abstractmethod
    def generate_report(self, data: Any) -> None:
        pass


class PDFReportGenerator(ReportGenerator):
    def generate_report(self, data: Any) -> None:
        # Assume some logic to generate a report in PDF format
        print("Generating PDF report")


class CSVReportGenerator(ReportGenerator):
    def generate_report(self, data: Any) -> None:
        # Assume some logic to generate a report in CSV format
        print("Generating CSV report")


class HTMLReportGenerator(ReportGenerator):
    def generate_report(self, data: Any) -> None:
        # Assume some logic to generate a report in HTML format
        print("Generating HTML report")


# Usage
report_generators = [PDFReportGenerator(), CSVReportGenerator(), HTMLReportGenerator()]
data = {"example": "data"}

for generator in report_generators:
    generator.generate_report(data)
