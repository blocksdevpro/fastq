import pytest
import fastq


def test_task_creation():
    """Test task registry"""

    @fastq.task
    async def test_task():
        pass

    assert fastq.list_tasks() == ["test_task"]


def test_task_retrieval():
    """Test task retrieval"""

    @fastq.task
    async def test_task():
        pass

    assert fastq.get_task("test_task") == test_task


def test_task_not_found():
    """Test task not found"""
    with pytest.raises(fastq.FastQTaskNotFoundException):
        fastq.get_task("nonexistent_task")


def test_clear_registry():
    """Test clear registry"""

    @fastq.task
    async def test_task():
        pass

    assert fastq.list_tasks() == ["test_task"]
    fastq.clear_registry()
    assert fastq.list_tasks() == []
