from pydantic import BaseModel, EmailStr, Field
from time import time


class UserSchema(BaseModel):
    """
    Описание структуры пользователя.
    """
    id: str
    email: EmailStr
    last_name: str = Field(alias='lastName')
    first_name: str = Field(alias='firstName')
    middle_name: str = Field(alias='middleName')
    phone_number: str = Field(alias='phoneNumber')


class CreateUserRequestSchema(BaseModel):
    """
    Описание структуры создания пользователя.
    """
    email: EmailStr = Field(default=f"user{time()}@test.ru")
    last_name: str = Field(alias='lastName', default='test-last-name')
    first_name: str = Field(alias='firstName', default='test-first-name')
    middle_name: str = Field(alias='middleName', default='test-middle-name')
    phone_number: str = Field(alias='phoneNumber', default='89999999999')


class CreateUserResponseSchema(BaseModel):
    """
    Описание структуры ответа создания пользователя.
    """
    user: UserSchema