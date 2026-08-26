
from sample_app import app


def test_ejemplo():
    client = app.test_client()
    response = client.get('/') 
    
    if response.status_code != 200:
        raise AssertionError(f"Prueba Fallida: La ruta principal devuelve un estado {response.status_code}.")