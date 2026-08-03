import uvicorn
from fastapi import FastAPI, APIRouter, HTTPException, status
from pydantic import BaseModel, EmailStr, RootModel

app = FastAPI(title="Apishka")
router = APIRouter(
    prefix="/api/v1/users",
    tags=['Users']
)


class UserIn(BaseModel):
    email: EmailStr
    username: str


class UserOut(UserIn):
    id: int

class UsersStore(RootModel):
    root: list[UserOut]

    def find(self, user_id: int) -> UserOut:
        print()
        return next(filter(lambda user: user.id == user_id, self.root), None)

    def get_all(self) -> list[UserOut]:
        return self.root

    def create(self, user: UserIn) -> UserOut:
        created_user = UserOut(id=len(self.root) + 1, **user.model_dump())

        self.root.append(created_user)

        return created_user

    def update(self, user_id: int, user: UserIn) -> UserOut:
        index = next(index for index, user in enumerate(self.root) if user.id == user_id)

        updated_user = UserOut(id=user_id, **user.model_dump())
        self.root[index] = updated_user

        return updated_user

    def delete(self, user_id: int):
        users = [user for user in self.root if user.id != user_id]

        self.root = users


root = UsersStore(root=[])


@app.get('/{user_id}', response_model=UserOut)
async def get_user(user_id: int):
    if not (user := root.find(user_id=user_id)):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"User with id {user_id} not found"
        )
    return user


@app.get('/')
async def get_users():
    return root.get_all()


@app.post('/', response_model=UserOut)
async def create_user(user: UserIn):
    return root.create(user)


@app.put('/{user_id}', response_model=UserOut)
async def update_user(user_id: int, user: UserIn):
    if not root.find(user_id=user_id):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f'User with id {user_id} not found'
        )
    return root.update(user_id=user_id, user=user)


@app.delete('/{user_id}', status_code=status.HTTP_204_NO_CONTENT)
def delete_user(user_id: int):
    if not root.find(user_id):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f'User with id {user_id} not found'
        )
    root.delete(user_id)


app.include_router(router)

if __name__ == '__main__':
    uvicorn.run(
        "fastapi_users2:app",
        host="127.0.0.1",
        port=8000,
        reload=True,
        log_level="info"
    )
