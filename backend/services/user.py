from app.models import User

def create_user(username, email):
    user = User(username=username, email=email)
    user.save()

def get_user(username):
    user = User.objects(username=username).first()
    return user

def get_all_users():
    users = User.objects()
    return users
