from abc import ABC, abstractmethod

# Strategy Interface
class ReportExporter(ABC):
    @abstractmethod
    def export(self, report_data):
        pass


# Concrete Strategies
class PdfExporter(ReportExporter):
    def export(self, report_data):
        print(f"Exporting report as PDF: {report_data}")


class CsvExporter(ReportExporter):
    def export(self, report_data):
        print(f"Exporting report as CSV: {report_data}")


class JsonExporter(ReportExporter):
    def export(self, report_data):
        print(f"Exporting report as JSON: {report_data}")


# Context
class ReportGenerator:
    def __init__(self, exporter: ReportExporter):
        self.exporter = exporter

    def generate(self, report_data):
        self.exporter.export(report_data)


# Client Code
report_data = {"sales": 5000}

generator = ReportGenerator(PdfExporter())
generator.generate(report_data)

generator = ReportGenerator(CsvExporter())
generator.generate(report_data)