import httpx

response = httpx.get("https://jsonplaceholder.typicode.com/todos/1")

print(response.status_code)  # 200
print(response.json())       # {'userId': 1, 'id': 1, 'title': 'delectus aut autem', 'completed': False}

data = {
    "title": "Новая задача",
    "completed": False,
    "userId": 1
}

response = httpx.post("https://jsonplaceholder.typicode.com/todos", json=data)

print(response.status_code)  # 201 (Created)
print(response.json())       # Ответ с созданной записью


data = {"username": "test_user", "password": "123456"}

response = httpx.post("https://httpbin.org/post", data=data)

 # {'form': {'username': 'test_user', 'password': '123456'}, ...}


headers = {"Authorization": "Bearer my_secret_token"}

response = httpx.get("https://httpbin.org/get", headers=headers)




params = {"userId": 1}

response = httpx.get("https://jsonplaceholder.typicode.com/todos", params=params)

print(response.url)    # https://jsonplaceholder.typicode.com/todos?userId=1
print(response.json()) # Фильтрованный список задач



files = {"file": ("t.txt", open("requirements.txt", "rb"))}

response = httpx.post("https://httpbin.org/post", files=files)

response.raise_for_status()


with httpx.Client(base_url="https://jsonplaceholder.typicode.com/todos/") as client:
    response1 = client.get("1")
    response2 = client.get("2")

print(response1.json())  # Данные первой задачи
print(response2.json())  # Данные второй задачи

