from boiler.constants import column_names, circuit_types

from boiler_softm_chernushka.constants import circuit_ids as chernushka_circuit_ids
from boiler_softm_chernushka.constants import column_names as chernushka_column_names

CHERNUSHKA_WEATHER_INFO_COLUMN_EQUALS = {
    chernushka_column_names.CHERNUSHKA_WEATHER_TEMP: column_names.WEATHER_TEMP,
    chernushka_column_names.CHERNUSHKA_WEATHER_TIMESTAMP: column_names.TIMESTAMP
}

CHERNUSHKA_TEMP_GRAPH_COLUMN_NAMES_EQUALS = {
    chernushka_column_names.CHERNUSHKA_TEMP_GRAPH_WEATHER_TEMP: column_names.WEATHER_TEMP,
    chernushka_column_names.CHERNUSHKA_TEMP_GRAPH_TEMP_AT_IN: column_names.FORWARD_PIPE_COOLANT_TEMP,
    chernushka_column_names.CHERNUSHKA_TEMP_GRAPH_TEMP_AT_OUT: column_names.BACKWARD_PIPE_COOLANT_TEMP
}

CHERNUSHKA_HEATING_OBJ_TIMESTAMP_PARSING_PATTERNS = (
    r"(?P<year>\d{4})-(?P<month>\d{2})-(?P<day>\d{2})\s(?P<hours>\d{2}):(?P<minutes>\d{2}).{7}",
    r"(?P<day>\d{2})\.(?P<month>\d{2})\.(?P<year>\d{4})\s(?P<hours>\d{1,2}):(?P<minutes>\d{2})",
    r"(?P<month>\d{2})/(?P<day>\d{2})/(?P<year>\d{4})\s(?P<hours>\d{1,2}):(?P<minutes>\d{2}):(?P<seconds>\d{2})"
)

CHERNUSHKA_HEATING_OBJ_COLUMN_NAMES_EQUALS = {
    chernushka_column_names.CHERNUSHKA_HEATING_SYSTEM_TIMESTAMP:
        column_names.TIMESTAMP,
    chernushka_column_names.CHERNUSHKA_HEATING_SYSTEM_FORWARD_PIPE_COOLANT_TEMP:
        column_names.FORWARD_PIPE_COOLANT_TEMP,
    chernushka_column_names.CHERNUSHKA_HEATING_SYSTEM_BACKWARD_PIPE_COOLANT_TEMP:
        column_names.BACKWARD_PIPE_COOLANT_TEMP,
    chernushka_column_names.CHERNUSHKA_HEATING_SYSTEM_FORWARD_PIPE_COOLANT_VOLUME:
        column_names.FORWARD_PIPE_COOLANT_VOLUME,
    chernushka_column_names.CHERNUSHKA_HEATING_SYSTEM_BACKWARD_PIPE_COOLANT_VOLUME:
        column_names.BACKWARD_PIPE_COOLANT_VOLUME,
    chernushka_column_names.CHERNUSHKA_HEATING_SYSTEM_FORWARD_PIPE_COOLANT_PRESSURE:
        column_names.FORWARD_PIPE_COOLANT_PRESSURE,
    chernushka_column_names.CHERNUSHKA_HEATING_SYSTEM_BACKWARD_PIPE_COOLANT_PRESSURE:
        column_names.BACKWARD_PIPE_COOLANT_PRESSURE
}

CHERNUSHKA_BOILER_FLOAT_COLUMNS = [
    column_names.FORWARD_PIPE_COOLANT_TEMP,
    column_names.BACKWARD_PIPE_COOLANT_TEMP,
    column_names.FORWARD_PIPE_COOLANT_PRESSURE,
    column_names.BACKWARD_PIPE_COOLANT_PRESSURE,
    column_names.FORWARD_PIPE_COOLANT_VOLUME,
    column_names.BACKWARD_PIPE_COOLANT_VOLUME
]

CHERNUSHKA_BOILER_AVAILABLE_COLUMNS = [
    column_names.TIMESTAMP,
    *CHERNUSHKA_BOILER_FLOAT_COLUMNS
]

CHERNUSHKA_APARTMENT_HOUSE_FLOAT_COLUMNS = [
    column_names.FORWARD_PIPE_COOLANT_TEMP,
    column_names.BACKWARD_PIPE_COOLANT_TEMP,
]

CHERNUSHKA_APARTMENT_HOUSE_NEED_INTERPOLATE_COLUMNS = CHERNUSHKA_APARTMENT_HOUSE_FLOAT_COLUMNS

CHERNUSHKA_APARTMENT_HOUSE_AVAILABLE_COLUMNS = [
    column_names.TIMESTAMP,
    *CHERNUSHKA_APARTMENT_HOUSE_FLOAT_COLUMNS
]

CHERNUSHKA_CIRCUIT_ID_EQUALS = {
    chernushka_circuit_ids.HOT_WATER_CIRCUIT: circuit_types.HOT_WATER,
    chernushka_circuit_ids.HEATING_CIRCUIT: circuit_types.HEATING
}
