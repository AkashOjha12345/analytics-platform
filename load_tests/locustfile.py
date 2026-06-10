from locust import HttpUser, task, between


class AnalyticsUser(HttpUser):
    wait_time = between(1, 3)

    @task
    def health(self):
        self.client.get("/health")

    @task
    def analytics(self):
        self.client.get("/analytics/sales")