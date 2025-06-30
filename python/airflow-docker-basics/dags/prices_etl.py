from typing import List

from datetime import datetime, timedelta

from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.utils.dates import days_ago
from airflow.models import Variable

from wd_data_pipeline.etl.etl_facade import StandardEtlProcess
from wd_data_pipeline.etl.extractor import YahooFinanceExtractor
from wd_data_pipeline.etl.transformer import YahooFinanceTransformer
from wd_data_pipeline.etl.loader import FastApiLoader
from wd_data_pipeline.api_client import AuthorisedApiClient
from wd_data_pipeline.utils.utils import IdMapUtils
from wd_data_pipeline.app_logger import logger, ConsoleHandler, LogLevel

default_args = {
    "owner": "Finlay",
    # "depends_on_past": False,
    # "email": ["airflow@example.com"],
    # "email_on_failure": False,
    # "email_on_retry": False,
    "retries": 5,
    "retry_delay": timedelta(minutes=2),
}

data = [
    {
        "isin": "GB00BJL5C004",
        "sedol": "BJL5C00",
        "alternative_symbols": {"yahoo_finance": "0P000127UC.L"},
        "name": "iShares Pacific ex Jpn Eq Idx (UK) H Acc",
        "exchange": "LSE",
        "instrument_type": "Fund",
        "currency": "GBp",
        "timezone": "GMT",
    },
    {
        "isin": "GB00BJ2JPG83",
        "sedol": "BJ2JPG8",
        "alternative_symbols": {"yahoo_finance": "0P0001FT5V.L"},
        "name": "L&G Global Health & Pharma Index C Acc",
        "exchange": "LSE",
        "instrument_type": "Fund",
        "currency": "GBp",
        "timezone": "GMT",
    },
    {
        "isin": "GB00BG0QPP99",
        "sedol": "BG0QPP9",
        "alternative_symbols": {"yahoo_finance": "0P000102MR.L"},
        "name": "L&G Global Inflation Linked Bd Idx C Inc",
        "exchange": "LSE",
        "instrument_type": "Fund",
        "currency": "GBp",
        "timezone": "GMT",
    },
]


def run_etl() -> None:
    logger.add_handler(ConsoleHandler(log_level=LogLevel.INFO))
    logger.info("Starting instruments pipeline")

    logger.info("Retrieving instruments data")
    api_client = AuthorisedApiClient(
        Variable.get("API_USER"),
        Variable.get("API_PASSWORD"),
        Variable.get("API_BASE_URL"),
    )
    endpoint = "prices"
    instruments = data

    logger.info("Building identifier map")
    identifier_map = IdMapUtils.build_yf_ticker_to_sedol_and_isin_map(instruments)

    logger.info("Determining tickers to process")
    tickers: List[str] = list(identifier_map.keys())

    start_date = (datetime.now() - timedelta(days=5)).strftime("%Y-%m-%d")
    end_date = datetime.now().strftime("%Y-%m-%d")

    logger.info(f"Processing prices for {len(tickers)} tickers")
    etl = StandardEtlProcess(
        extractor=YahooFinanceExtractor(tickers, start_date, end_date),
        transformer=YahooFinanceTransformer(identifier_map),
        loader=FastApiLoader(api_client, endpoint),
    )
    etl.run()


with DAG(
    dag_id="prices_etl",
    default_args=default_args,
    description="ETL for prices data",
    # start_date=datetime(2024, 3, 26, 9),
    start_date=days_ago(1),
    schedule_interval="@daily",
    # schedule_interval=timedelta(days=1),
) as dag:
    etl_task = PythonOperator(
        task_id="etl_task",
        python_callable=run_etl,
    )

    etl_task
