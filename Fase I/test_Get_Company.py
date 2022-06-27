import requests


def test_02():
    response = requests.get("https://rapipago-adapter.qa.clave.cloud/billings/companies?companySearchString=ypf")
    assert response.status_code == 200
    assert response.headers["Content-Type"] == "application/json"

