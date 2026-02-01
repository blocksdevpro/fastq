from fastq.core.task import Task, TaskStatus


def test_task_creation():
    task = Task(name="test_task")

    assert task.id is not None
    assert task.name == "test_task"
    assert task.status == "pending"
    assert not task.is_finished


def test_task_serialization():
    task = Task(name="test_task")

    serialized_task = task.to_dict()

    assert serialized_task["id"] == task.id
    assert serialized_task["name"] == task.name
    assert serialized_task["status"] == task.status.value
    assert serialized_task["created_at"] == task.created_at.isoformat()
    assert serialized_task["started_at"] == (
        task.started_at.isoformat() if task.started_at else None
    )
    assert serialized_task["completed_at"] == (
        task.completed_at.isoformat() if task.completed_at else None
    )
    assert serialized_task["result"] == task.result
    assert serialized_task["error"] == task.error
    assert serialized_task["retry_count"] == task.retry_count


def test_task_deserialization():
    task = Task(name="test_task")
    serialized_task = task.to_dict()

    deserialized_task = Task.from_dict(serialized_task)

    assert deserialized_task.id == task.id
    assert deserialized_task.name == task.name
    assert deserialized_task.status == task.status
    assert deserialized_task.created_at == task.created_at
    assert deserialized_task.started_at == task.started_at
    assert deserialized_task.completed_at == task.completed_at
    assert deserialized_task.result == task.result
    assert deserialized_task.error == task.error
    assert deserialized_task.retry_count == task.retry_count


test_task_creation()
test_task_serialization()
test_task_deserialization()
