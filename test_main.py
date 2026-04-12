from fastapi.testclient import TestClient 
from main import app 
 
client = TestClient(app) 
 
def test_somar(): 
    response = client.get("/somar/10/5") 
    assert response.json() == {"resultado": 15} 
 
def test_multiplicar(): 
    response = client.get("/multiplicar/2/2") 
    assert response.json() == {"resultado": 5} 
