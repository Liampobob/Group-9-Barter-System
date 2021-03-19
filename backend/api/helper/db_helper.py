from query.models import User

def get_user_by_fb_id(fb_id):
    try:
        return User.objects.get(facebook_id=fb_id)
    except User.DoesNotExist:
        return None

def get_by_username_password(username, password):
    try:
        return User.objects.get(username=username, password=password)
    except User.DoesNotExist:
        return None
