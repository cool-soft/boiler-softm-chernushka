import io
import json
from datetime import tzinfo
from typing import BinaryIO

import pandas as pd
from boiler.constants import column_names
from boiler.weather.io.abstract_sync_weather_reader import AbstractSyncWeatherReader
from dateutil.tz import gettz

from boiler_softm_chernushka.constants import converting_parameters
from boiler_softm_chernushka.logging import logger


class SoftMChernushkaWeatherForecastOnlineReader(AbstractSyncWeatherReader):

    def __init__(self,
                 encoding: str = "utf-8",
                 weather_data_timezone: tzinfo = gettz("Asia/Yekaterinburg")
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
            server_response = json.load(text_stream)
        df = pd.DataFrame(server_response.get("data"))
        df = self._rename_columns(df)
        df = self._convert_datetime_to_timestamp(df)
        df = self._convert_weather_temp_to_float(df)
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
        timestamp = pd.to_datetime(df[column_names.TIMESTAMP])
        timestamp = timestamp.dt.tz_convert(self._weather_data_timezone)
        df[column_names.TIMESTAMP] = timestamp
        return df

    # noinspection PyMethodMayBeStatic
    def _convert_weather_temp_to_float(self, df: pd.DataFrame) -> pd.DataFrame:
        logger.debug("Converting weather temp to float type")
        df = df.copy()
        df[column_names.WEATHER_TEMP] = df[column_names.WEATHER_TEMP].apply(float)
        return df
