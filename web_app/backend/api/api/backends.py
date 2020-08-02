from django.contrib.auth import get_user_model

class OTPAuthentication(object):
    """
    Custom Email Backend to perform authentication via email
    """
    def authenticate(self, username):
        my_user_model = get_user_model()
        try:
            user = my_user_model.objects.get(email=username)
            return user
        except my_user_model.DoesNotExist:
            return None # return None if custom user model does not exist 
        except:
            return None # return None in case of other exceptions
