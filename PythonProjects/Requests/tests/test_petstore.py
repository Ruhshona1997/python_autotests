import requests
import pytest

def test_Statuscode():
    responce = requests.get("https://petstore.swagger.io/v2/pet/250")
    assert responce.status_code == 200


def test_piece_of_body():
    responce = requests.get("https://petstore.swagger.io/v2/pet/250")
    assert responce.json () ['name'] == 'hleb'