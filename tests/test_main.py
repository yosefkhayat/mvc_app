from fastapi.testclient import TestClient
from server import server

client = TestClient(server)

def test_sanity_check():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"msg" : "The server is working properly!"}