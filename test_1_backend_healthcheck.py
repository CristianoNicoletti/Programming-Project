
# Test for backend healthcheck endpoint
import requests

def test_healthcheck():
    """
    Test that the /healthcheck endpoint returns status 200 and correct JSON.
    """
    response = requests.get("http://localhost:5000/healthcheck")
    assert response.status_code == 200
    assert response.json() == {"status": "healthy"}