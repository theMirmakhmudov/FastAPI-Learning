from fastapi import FastAPI
from enum import Enum
app = FastAPI()

class UserRole(str,Enum):
    admin="admin"
    superuser="superuser"
    regular_user="user"

@app.get("/")
async def get_hello():
    return {"Hello":"World"}

@app.get("/user_role/{user_type}")
async def get_user_status(user_type:UserRole):
    if user_type==UserRole.admin:
        return {"role" : "Your status admin"}

    elif user_type==UserRole.superuser:
        return {"role" : "Your status superuser"}

    else:
        return {"role" : "Your status user"}