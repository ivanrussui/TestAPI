from typing import List

import requests

from src.module1.lesson17.task import Task


class TaskClient:

    def __init__(self, base_url):
        self.base_url = base_url

    def url(self, path) -> str:
        return f"{self.base_url}{path}"

    def get_all(self) -> List[Task]:
        resp = requests.get(
            url=self.url("/todo/api/v1.0/tasks")
        )
        status_code = resp.status_code
        assert status_code == 200, f"Статус код не равен 200 [{status_code}]"
        tasks = [Task(**t) for t in resp.json()["tasks"]]
        return tasks

    def get(self, task_id) -> Task:
        resp = requests.get(
            url=self.url(f"/todo/api/v1.0/tasks/{task_id}")
        )
        status_code = resp.status_code
        assert status_code == 200 or status_code == 404, "Неопределенный статус код"
        return Task(**resp.json()["task"])

    def create(self, task: Task) -> Task:
        resp = requests.post(
            url=self.url("/todo/api/v1.0/tasks"),
            data=task.to_json()
        )
        status_code = resp.status_code
        assert status_code == 201, f"Статус код не равен 201 [{status_code}]"
        print(f"Создана задача с id {resp.json()['task']['id']}")
        return Task(**resp.json()["task"])

    def update(self, task: Task) -> Task:
        resp = requests.put(
            url=self.url(f"/todo/api/v1.0/tasks/{task.id}"),
            data=task.to_json()
        )
        status_code = resp.status_code
        assert status_code == 200, f"Статус код не равен 200 [{status_code}]"
        print(f"Задача <{task.id}> обновлена")
        return Task(**resp.json()["task"])

    def delete(self, task_id) -> None:
        resp = requests.delete(
            url=self.url(f"/todo/api/v1.0/tasks/{task_id}"),
        )
        status_code = resp.status_code
        assert status_code == 200, f"Статус код не равен 200 [{status_code}]"
        assert resp.json()["result"] == True, f"Запись не была удалена [{resp.json()['result']}]"
