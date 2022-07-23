from locust import HttpUser, task


class WebsiteTest(HttpUser):

    @task(1)
    def test1(self):
        self.client.get("http://localhost:5000")

    @task(2)
    def test2(self):
        self.client.post("http://localhost:5000/showSummary", {"email": "john@simplylift.co"})

    @task(3)
    def test3(self):
        self.client.get("http://localhost:5000/book/Spring%20Festival/Simply%20Lift")

    @task(4)
    def test4(self):
        self.client.post("http://localhost:5000/purchasePlaces",
                         {"club": "Simply Lift", "competition": "Spring Festival", "places": "3"})

    @task(5)
    def test5(self):
        self.client.get("http://localhost:5000/logout")