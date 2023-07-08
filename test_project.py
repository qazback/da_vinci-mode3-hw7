from project import add_task, list_tasks, complete_task


def test_add_task():
    tasks = []
    add_task(tasks, "Task 1")
    assert len(tasks) == 1
    assert tasks[0]["name"] == "Task 1"
    assert tasks[0]["completed"] is False

    add_task(tasks, "Task 2")
    assert len(tasks) == 2
    assert tasks[1]["name"] == "Task 2"
    assert tasks[1]["completed"] is False


def test_list_tasks(capsys):
    tasks = [{"name": "Task 1", "completed": False}, {"name": "Task 2", "completed": True}]
    list_tasks(tasks)
    captured = capsys.readouterr()
    expected_output = "Tasks:\nTask 1 [ ]\nTask 2 [x]\n"
    assert captured.out == expected_output


def test_complete_task():
    tasks = [{"name": "Task 1", "completed": False}, {"name": "Task 2", "completed": True}]
    complete_task(tasks, "Task 1")
    assert tasks[0]["completed"] is True

    complete_task(tasks, "Task 3")
    assert tasks[0]["completed"] is True


if __name__ == "__main__":
    test_add_task()
    test_list_tasks()
    test_complete_task()
