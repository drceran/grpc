from locust import HttpUser, task, between
import random

class FastAPITestUser(HttpUser):
    # Set the wait time between requests
    wait_time = between(1, 2)  # Random wait time between requests

    @task
    def test_fastapi_request(self):
        # Generate a random device ID
        device_id = f"device{random.randint(1, 100)}"  # Random device ID between device1 and device100

        # Perform a POST request to the FastAPI endpoint
        response = self.client.post(
            "/device-data/", json={"id": device_id}  # POST request with random device ID
        )
        
        # Check if the response status code is 200 (OK)
        if response.status_code == 200:
            data = response.json()
            # Ensure that 'message' and 'id' are part of the response structure
            print(f"Response for device ID {data['id']}: {data.get('message', 'No message field found')}")
        else:
            print(f"Request failed with status code {response.status_code}")
