from fastapi import APIRouter, HTTPException
from models import User
from services.user_service import UserService

router = APIRouter()
user_service = UserService()

@router.get('/users/')
def get_users():
    return user_service.get_users()