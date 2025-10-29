from myproject.schemas import Message
from fastapi import FastAPI  # type: ignore
from http import HTTPStatus

status_code_OK = HTTPStatus.OK

app = FastAPI()


@app.get("/", status_code=status_code_OK, response_model=Message)
def read_root():
    return {"message": "bem vindo"}
