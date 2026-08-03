from fastapi import FastAPI, Query, Path, Body, APIRouter, Depends, HTTPException, status
from pydantic import BaseModel
import uvicorn

app = FastAPI(title="Rugaga")

router = APIRouter(
    prefix='/api/v1/users', tags=['Users']
)


class CreateUserRequest(BaseModel):
    username: str
    age: int


class CreateUserResponse(BaseModel):
    username: str
    age: int
    message: str


def validate_age(age: int = 18):
    def checker(body: CreateUserRequest):
        if body.age < age:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                                detail="Возраст должен быть от 18")
        return body

    return checker


@app.get('/{nth}')
def get_user_info(
        name: str = Query(
            default="Ivan",
            description="Имя пользователя"
        ),
        nth: int = Path(
            ...,
            description='Порядковый номер'
        )
):
    return f"Name is {name}, number is {nth}"


@app.post('/', response_model=CreateUserResponse)
def create_user(
            body: CreateUserRequest = Depends(validate_age(age=18))
):
    return CreateUserResponse(
        username=body.username,
        age=body.age,
        message="New user created"
    )


app.include_router(router)

if __name__ == '__main__':
    uvicorn.run(
        "fastapi_basics2:app",
        host="127.0.0.1",
        port=8000,
        reload=True,
        log_level="info"
    )
