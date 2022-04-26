from locust import HttpUser, task


class ProjectPerfTest(HttpUser):
    @task(5)
    def index(self):
        response = self.client.get("/")
        print("Response status code:", response.status_code)
        print("Response text:", response.text)

    @task(5)
    def show_summary_page(self):
        response = self.client.post("/showSummary", {"email": "john@simplylift.co"})
        print("Response status code:", response.status_code)
        print("Response text:", response.text)

    @task(5)
    def purchase_places(self):
        input_places_desire = "2"
        club = "Simply Lift"
        competition = "Spring Festival"
        response = self.client.post('/purchasePlaces',
                                    data=dict(club=club, competition=competition, places=input_places_desire),
                                    )
        print("Response status code:", response.status_code)
        print("Response text:", response.text)

    @task(5)
    def board_clubs(self):
        response = self.client.get("/boardClubs")
        print("Response status code:", response.status_code)
        print("Response text:", response.text)