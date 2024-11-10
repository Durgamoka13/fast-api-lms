from fastapi import FastAPI,Path,Query
from pydantic import BaseModel
from typing import Optional, List

app = FastAPI(
    title="LMS App",
    description="Lms for managing students and teachers",
    contact={
        "name": "Durga",
        "email": "durgamoka@gmail.com",
    },
    license_info={
        "name": "NIT",
    },
)

users = []

class User(BaseModel):
    email: str
    is_active: bool
    bio: Optional[str]



@app.get("/users", response_model=List[User])
async def get_users():
    return users

@app.post("/users")
async def create_user(user: User):
    users.append(user)
    return {"message": "User created"}

@app.get("/users/{user_id}")
async def get_user(user_id: int = Path(...,description="The ID of the user to get",lt=2),
                   q:str = Query(None,max_length=10)):
    return {"user":users[user_id],"query":q}