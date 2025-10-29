from http import HTTPStatus


status_code_OK = HTTPStatus.OK


def test_read_root_deve_retornar_bem_vindo(client):

    response = client.get("/")

    assert response.status_code == status_code_OK
    assert response.json() == {"message": "bem vindo"}
