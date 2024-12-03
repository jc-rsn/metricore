import time

import snowflake.constant as constant
import snowflake.variable as variable

__all__ = ['create_snowflake_id']


def create_snowflake_id() -> int:
    node = constant.NODE_MAX
    epoch = constant.BASE_EPOCH
    timestamp = int(time.time() * 1000) - epoch

    if epoch < 0:
        raise ValueError("epoch cannot be negative")

    if node < 0 or node > constant.NODE_MAX:
        raise ValueError(f"node cannot be negative and must be less than {constant.NODE_MAX}")

    if timestamp < 0 or timestamp > constant.TIMESTAMP_MAX:
        raise ValueError(f"timestamp cannot be negative and must be less than {constant.TIMESTAMP_MAX}")

    if timestamp == variable.TIMESTAMP_LAST:
        variable.SEQUENCE_LAST = (variable.SEQUENCE_LAST + 1) & constant.SEQUENCE_MAX

        if variable.SEQUENCE_LAST == 0:
            raise ValueError(f"sequence cannot be negative and must be less than {constant.SEQUENCE_MAX}")
    else:
        variable.SEQUENCE_LAST = 0
        variable.TIMESTAMP_LAST = timestamp

    snowflake_id = ((timestamp << 22) | (node << 12) | variable.SEQUENCE_LAST)

    return snowflake_id
