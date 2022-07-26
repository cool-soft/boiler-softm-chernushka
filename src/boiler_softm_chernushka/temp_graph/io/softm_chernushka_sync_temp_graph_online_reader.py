import io
import json
from typing import BinaryIO

import pandas as pd
from boiler.temp_graph.io.abstract_sync_temp_graph_reader import AbstractSyncTempGraphReader

from boiler_softm_chernushka.logging import logger
from boiler_softm_chernushka.constants import converting_parameters


class SoftMChernushkaSyncTempGraphOnlineReader(AbstractSyncTempGraphReader):

    def __init__(self, encoding: str = "utf-8") -> None:
        logger.debug("Creating instance")
        self._column_names_equal = converting_parameters.CHERNUSHKA_TEMP_GRAPH_COLUMN_NAMES_EQUALS
        self._encoding = encoding

    def read_temp_graph_from_binary_stream(self, binary_stream: BinaryIO) -> pd.DataFrame:
        logger.debug("Reading temp graph")
        with io.TextIOWrapper(binary_stream, encoding=self._encoding) as text_stream:
            temp_graph_server_response = json.load(text_stream)
        df = pd.DataFrame(temp_graph_server_response.get("data"))
        df = df.rename(columns=self._column_names_equal)
        logger.debug("Temp graph is read")
        return df
