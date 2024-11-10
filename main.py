from fastapi import FastAPI,Path,Query
from pydantic import BaseModel
from typing import Optional, List
from api import users,sections,courses

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

app.include_router(users.router)
app.include_router(sections.router)
app.include_router(courses.router)


