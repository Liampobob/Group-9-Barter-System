from query.models import User

def get_user_by_fb_id(fb_id):
    try:
        return User.objects.get(facebook_id=fb_id)
    except User.DoesNotExist:
        return None

