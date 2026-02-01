from uuid import uuid4
from datetime import datetime, UTC


def generate_uuid_str() -> str:
    return str(uuid4())


def datetime_now() -> datetime:
    return datetime.now(tz=UTC)
