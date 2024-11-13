from locust import HttpUser, TaskSet, task, between

class SimpleTasks(TaskSet):
    @task(1)
    def home(self):
        # Test the home route
        self.client.get("/")

    @task(2)
    def fast(self):
        # Test the fast route
        self.client.get("/fast")

    @task(3)
    def medium(self):
        # Test the medium route
        self.client.get("/medium")

    @task(4)
    def heavy(self):
        # Test the heavy route
        self.client.get("/heavy")

    @task(1)
    def echo(self):
        # Test the echo route
        payload = {"message": "Hello, Locust!"}
        self.client.post("/echo", json=payload)

class SimpleUser(HttpUser):
    tasks = [SimpleTasks]
    weight = 2
    wait_time = between(1, 5)  # Simulate a wait time between requests

class HeavyUser(HttpUser):
    tasks = [SimpleTasks]
    weight = 98
    wait_time = between(10, 20)  # Simulate a wait time between requests