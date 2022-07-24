import io
from datetime import tzinfo
from typing import BinaryIO

import pandas as pd
from boiler.constants import column_names
from boiler.weather.io.abstract_sync_weather_reader import AbstractSyncWeatherReader

from boiler_softm_chernushka.constants import converting_parameters
from boiler_softm_chernushka.logging import logger


class SoftMChernushkaWeatherForecastOnlineReader(AbstractSyncWeatherReader):

    def __init__(self,
                 encoding: str = "utf-8",
                 weather_data_timezone: tzinfo = None
                 ) -> None:
        self._weather_data_timezone = weather_data_timezone
        self._encoding = encoding
        self._column_names_equals = converting_parameters.CHERNUSHKA_WEATHER_INFO_COLUMN_EQUALS.copy()
        logger.debug(
            f"Creating instance:"
            f"weather_data_timezone: {self._weather_data_timezone}"
            f"encoding: {self._encoding}"
        )

    def read_weather_from_binary_stream(self, binary_stream: BinaryIO) -> pd.DataFrame:
        logger.debug("Parsing weather")
        with io.TextIOWrapper(binary_stream, encoding=self._encoding) as text_stream:
            df = pd.read_json(text_stream, convert_dates=False)
        df = self._rename_columns(df)
        df = self._convert_datetime_to_timestamp(df)
        logger.debug("Weather is parsed")
        return df

    def _rename_columns(self, df: pd.DataFrame) -> pd.DataFrame:
        logger.debug("Renaming columns")
        df = df.copy()
        df.rename(columns=self._column_names_equals, inplace=True)
        return df

    def _convert_datetime_to_timestamp(self, df: pd.DataFrame) -> pd.DataFrame:
        logger.debug("Converting dates and time to timestamp")
        df = df.copy()
        datetime_as_str = df[column_names.TIMESTAMP]
        timestamp = pd.to_datetime(datetime_as_str)
        timestamp = timestamp.dt.tz_convert(self._weather_data_timezone)
        df[column_names.TIMESTAMP] = timestamp
        return df
