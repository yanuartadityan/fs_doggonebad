from typing import List
from ..model import User, Group, Owner
from ..db import database
from ..main import app


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
@app.get("/users/", response_model=List[User])
async def get_user():
    users = await User.objects.all()
    
    return users