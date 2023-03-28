from typing import List

from fastapi import APIRouter

from ..db import database
from ..model import Group
from ..model import Owner
from ..model import User

router = APIRouter(
    prefix="/users", tags=["users"], responses={404: {"description": "not found"}}
)

"""
create section:
 - create_user
 - create_owner
 - create_group
"""

"""
get section:
 - get_user
 - get_owner
 - get_group
"""


@router.get("/get_all/", response_model=List[User])
async def get_user():
    users = await User.objects.all()
    return users
