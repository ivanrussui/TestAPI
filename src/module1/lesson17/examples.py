import requests

class TaskClient:

    def __init__(self, base_url):
        self.base_url = base_url

    def url(self, path) -> str:
        return f'{self.base_url}{path}'

    def get_all(self) -> dict:
        resp = requests.get(
            url=self.url("/todo/api/v1.0/tasks")
        )
        status_code = resp.status_code
        assert status_code == 200, f"Статус код не 200 [{status_code}]"
        return resp.text

    def get(self, task_id) -> dict:
        resp = requests.get(
            url=self.url(f"/todo/api/v1.0/tasks/{task_id}")
        )
        status_code = resp.status_code
        assert status_code == 200 or status_code == 404, 'Неопределенный статус код'
        return resp.json()

    def create(self, title=None, description=None, done=False):
        json = {
            'title': title,
            'description': description,
            'done': done
        }
        resp = requests.post(
            url=self.url(f"/todo/api/v1.0/tasks"),
            data=json
        )
        status_code = resp.status_code
        assert status_code == 201, f"Статус код не 201 [{status_code}]"
        return resp.json()


task_client = TaskClient('http://localhost:5000')

result = task_client.get_all()
print(result)

result = task_client.create(
    title='Test title',
    description='Test description',
    done=False
)
task_id = result["task"]["id"]
print(result)









# todo так делали до TaskClient
# BASE_URL = 'http://localhost:5000'


# def print_resp(resp):
#     print(f"URL: {resp.url}")
#     print(f"STATUS CODE: {resp.status_code}")
#     print(f"JSON: {resp.text}")


# todo запросы для app
# получить все задачи
# resp = requests.get(
#     url=f"{BASE_URL}/todo/api/v1.0/tasks"
# )
# print_resp(resp)


# получить задачу 3
# resp = requests.get(
#     url=f"{BASE_URL}/todo/api/v1.0/tasks/3"
# )
# print_resp(resp)


# создать задачу (начиная с id: 3 и uri: 'http://.../tasks/3')
# resp = requests.post(
#     url=f"{BASE_URL}/todo/api/v1.0/tasks",
#     data={
#         'title': 'Test title',
#         'description': 'Test description',
#         'done': False
#     }
# )
# print_resp(resp)


# todo это актуально для make_public_task() из app
# получить новую задачу по uri
# url_for_task = resp.json()["task"]["uri"]
# resp = requests.get(
#     url=url_for_task
# )
# print_resp(resp)


# todo это актуально для task из app
# получить новую задачу по id
# task_id = resp.json()["task"]["id"]
# resp = requests.get(
#     url=f"{BASE_URL}/todo/api/v1.0/tasks/{task_id}"
# )
# print_resp(resp)


# изменить новую задачу по id/uri
# resp = requests.put(
#     url=f"{BASE_URL}/todo/api/v1.0/tasks/{task_id}",
#     # url=f"{url_for_task}",
#     data={
#         'title': 'Change Title',
#         'description': 'Change description',
#         'done': True
#     }
# )
# print_resp(resp)


# получить-проверить новую задачу по id/uri
# resp = requests.get(
#     url=f"{BASE_URL}/todo/api/v1.0/tasks/{task_id}"
#     # url=f"{url_for_task}"
# )
# print_resp(resp)


# удалить новую задачу по id/uri
# resp = requests.delete(
#     url=f"{BASE_URL}/todo/api/v1.0/tasks/{task_id}"
#     # url=f"{url_for_task}"
# )
# print_resp(resp)


# получить-проверить новую задачу по id/uri
# resp = requests.get(
#     url=f"{BASE_URL}/todo/api/v1.0/tasks/{task_id}"
#     # url=f"{url_for_task}"
# )
# print_resp(resp)


# получить все задачи
# resp = requests.get(
#     url=f"{BASE_URL}/todo/api/v1.0/tasks"
# )
# print_resp(resp)




# todo запросы для my_app
# print('SIMPLE GET')
# resp = requests.get(
#     url=f"{BASE_URL}/ping"
# )
# print_resp(resp)
# print("-------")
#
# print('GET WITH PATH PARAMS')
# resp = requests.get(
#     url=f"{BASE_URL}/ping/10"
# )
# print_resp(resp)
# print("-------")
#
# print('GET WITH QUERY PARAMS')
# resp = requests.get(
#     url=f"{BASE_URL}/request",
#     params={'id': 300, 'name': 'Anna'}
# )
# print_resp(resp)
# print("-------")
#
# print('GET WITH PATH & QUERY PARAMS')
# resp = requests.get(
#     url=f"{BASE_URL}/request/20",
#     params={'id': 500, 'name': 'Melissa'}
# )
# print_resp(resp)
# print("-------")



# todo все что ниже было в файле который скинул Леша
# from src.module1.lesson17.task import Task
# from src.module1.lesson17.task_client import TaskClient
#
# task_client = TaskClient("http://localhost:5000")
#
# tasks = task_client.get_all()
# print(tasks)
#
# task = task_client.create(
#     Task(title="Test title", description="Test description", done=False)
# )
#
# task = task_client.get(task_id=task.id)
# print(task)
#
# task.done = True
# updated_task = task_client.update(task)
# print(updated_task)
#
# task = task_client.get(task_id=updated_task.id)
# print(task)
#
# # task_client.delete(task_id)
# #
# # result = task_client.get(task_id=task_id)
# # print(result)
