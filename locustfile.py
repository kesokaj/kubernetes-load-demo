from locust import HttpUser, between, task
class WebsiteUser(HttpUser):
    wait_time = between(5, 15)
    host = "https://load-demo.app01.arrowdemo.xyz"
    @task
    def index(self):
        self.client.get("/")

