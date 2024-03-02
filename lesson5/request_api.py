import httpx
import json

BASE_URL = "http://127.0.0.1:8000"


def send_post_request():
    task_data = {
        "id": 1,
        "title": "Sample task",
        "description": "This is a sample task for testing.",
        "status": False
    }

    response = httpx.post(f"{BASE_URL}/tasks", json=task_data)

    if response.status_code == 200:
        print("Task created successfully:")
        print(json.dumps(response.json(), indent=2))
    else:
        print("Failed to create task:")
        print(f"Status code: {response.status_code}")
        print(f"Response: {response.text}")


def get_tasks():
    response = httpx.get(f"{BASE_URL}/tasks")
    if response.status_code == 200:
        print("Tasks list:")
        print(json.dumps(response.json(), indent=2))
    else:
        print("Failed to create task:")
        print(f"Status code: {response.status_code}")
        print(f"Response: {response.text}")


if __name__ == "__main__":
    send_post_request()
    send_post_request()
    send_post_request()
    send_post_request()
    send_post_request()
    send_post_request()
    get_tasks()
