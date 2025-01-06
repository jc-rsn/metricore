import time
from dataclasses import dataclass
from typing import ClassVar

from fastapi import FastAPI, APIRouter

snowflake = APIRouter(
    prefix="/snowflake",
    tags=["snowflake"]
)


@snowflake.get("/snowflake")
async def get_snowflake():
    return create_snowflake()


@dataclass(frozen=True)
class SnowflakeComponents:
    base_epoch: int = 0
    max_timestamp: int = int(0b11111111111111111111111111111111111111111)
    max_node: int = int(0b1111111111)
    max_sequence: int = int(0b111111111111)


@dataclass
class SnowflakeState:
    last_timestamp: ClassVar[int] = int(0b0)
    last_sequence: ClassVar[int] = int(0b0)


def create_snowflake() -> int:
    node = SnowflakeComponents.max_node
    epoch = SnowflakeComponents.base_epoch
    timestamp = int(time.time() * 1000) - epoch

    if epoch < 0:
        raise ValueError("epoch cannot be negative")

    if node < 0 or node > SnowflakeComponents.max_node:
        raise ValueError(f"node cannot be negative and must be less than {SnowflakeComponents.max_node}")

    if timestamp < 0 or timestamp > SnowflakeComponents.max_timestamp:
        raise ValueError(f"timestamp cannot be negative and must be less than {SnowflakeComponents.max_timestamp}")

    if timestamp == SnowflakeState.last_timestamp:
        SnowflakeState.last_sequence = (SnowflakeState.last_sequence + 1) & SnowflakeComponents.max_sequence

    if SnowflakeState.last_sequence == 0:
        raise ValueError(f"sequence cannot be negative and must be less than {SnowflakeComponents.max_sequence}")
    else:
        SnowflakeState.last_sequence = 0
        SnowflakeState.last_timestamp = timestamp

    snowflake_id = ((timestamp << 22) | (node << 12) | SnowflakeState.last_sequence)

    return snowflake_id


__all__ = ['create_snowflake']
