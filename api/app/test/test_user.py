from app.carbon.models.user import User


database = User.Meta.database

@database.transaction()
async def create_user():
    user = User(
        username="doggonebad",
        email="dog@doggonebad.xyz",
        password="12345")

    await User.objects.create(user)

create_user()