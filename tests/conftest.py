import pytest
import asyncio
from fastq import clear_registry


@pytest.fixture(autouse=True)
def reset_registry():
    """Automatically clear registry after each test"""
    clear_registry()
    yield
    clear_registry()
