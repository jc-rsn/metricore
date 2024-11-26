import time

import snowflake.const as const
import snowflake.var as var

__all__ = ('generate')


def generate() -> int:
    node = const.NODE_MAX
    epoch = const.BASE_EPOCH
    timestamp = int(time.time() * 1000) - epoch

    if epoch < 0:
        raise ValueError("epoch cannot be negative")

    if node < 0 or node > const.NODE_MAX:
        raise ValueError(f"node cannot be negative and must be less than {const.NODE_MAX}!")

    if timestamp < 0 or timestamp > const.TIMESTAMP_MAX:
        raise ValueError(f"timestamp cannot be negative and must be less than {const.TIMESTAMP_MAX}!")

    if timestamp == var.TIMESTAMP_LAST:
        var.SEQUENCE_LAST = (var.SEQUENCE_LAST + 1) & const.SEQUENCE_MAX

        if var.SEQUENCE_LAST == 0:
            raise ValueError(f"sequence cannot be negative and must be less than {const.SEQUENCE_MAX}!")
    else:
        var.SEQUENCE_LAST = 0
        var.TIMESTAMP_LAST = timestamp

    snowflake_id = ((timestamp << 22) | (node << 12) | var.SEQUENCE_LAST)

    return snowflake_id
