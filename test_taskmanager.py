import os
import task_manager

def setup_function():
    # Reset tasks before each test
    if os.path.exists("tasks.json"):
        os.remove("tasks.json")

def test_add_task():
    task_manager.add_task("Test task")
    tasks = task_manager.load_tasks()
    assert tasks[0]["title"] == "Test task"
    assert not tasks[0]["done"]

def test_mark_done():
    task_manager.add_task("To be done")
    task_manager.mark_done(0)
    tasks = task_manager.load_tasks()
    assert tasks[0]["done"]

def test_delete_task():
    task_manager.add_task("To be deleted")
    task_manager.delete_task(0)
    tasks = task_manager.load_tasks()
    assert len(tasks) == 0
