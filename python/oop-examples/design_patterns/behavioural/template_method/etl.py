from abc import ABC, abstractmethod
import csv


class ETLTemplate(ABC):
    """
    Abstract class defining the template method for the ETL process.
    """

    def __init__(self, input_file: str, output_file: str):
        self.input_file = input_file
        self.output_file = output_file

    def etl_process(self) -> None:
        """
        Template method defining the overall ETL process.
        """
        data = self.extract_data()
        transformed_data = self.transform_data(data)
        self.load_data(transformed_data)

    @abstractmethod
    def extract_data(self):
        """
        Abstract method for extracting data.
        """
        pass

    @abstractmethod
    def transform_data(self, data):
        """
        Abstract method for transforming data.
        """
        pass

    def load_data(self, transformed_data) -> None:
        """
        Default method for loading data.
        """
        with open(self.output_file, "w", newline="") as csvfile:
            writer = csv.writer(csvfile)
            for row in transformed_data:
                writer.writerow(row)


class CSVETL(ETLTemplate):
    """
    Concrete subclass implementing ETL process for CSV files.
    """

    def extract_data(self):
        """
        Extracts data from a CSV file.
        """
        data = []
        with open(self.input_file, "r") as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                data.append(row)
        return data

    def transform_data(self, data):
        """
        Transforms CSV data (in this case, simply converts it to uppercase).
        """
        transformed_data = []
        for row in data:
            transformed_row = [cell.upper() for cell in row]
            transformed_data.append(transformed_row)
        return transformed_data


if __name__ == "__main__":
    # Define input and output files
    input_file = "input.csv"
    output_file = "output.csv"

    # Create an instance of CSVETL and run the ETL process
    csv_etl = CSVETL(input_file, output_file)
    csv_etl.etl_process()
