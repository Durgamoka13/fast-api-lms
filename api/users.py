import fastapi
from typing import List, Optional
from pydantic import BaseModel

router = fastapi.APIRouter()
users = []

class User(BaseModel):
    email: str
    is_active: bool
    bio: Optional[str]


@router.get("/users", response_model=List[User])
async def get_users():
    return users

@router.post("/users")
async def create_user(user: User):
    users.append(user)
    return {"message": "User created"}

@router.get("/users/{user_id}")
async def get_user(id: int):
    return {"user":users[id]}