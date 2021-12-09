from locust import HttpUser, between, task
class WebsiteUser(HttpUser):
    wait_time = between(5, 15)
    host = "https://google.com"
    @task
    def index(self):
        self.client.get("/")

