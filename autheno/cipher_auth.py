from django.contrib.auth.hashers import make_password, check_password
from database.models import user, profile
from django.contrib import messages
import datetime
from django.utils import timezone
currentDateTime = datetime.datetime.now(tz=timezone.utc)
# cipher authentication part
def auth_user(request, user_email, password):
    # adding a email to the session
    
    u = user.objects.filter(email=user_email).first()
    if u != None:
        if check_password(password, u.password_hash):
            request.session["email"] = user_email
            # updating the last login
            
            u.last_login = currentDateTime
            u.save()
            request.session["last_login"] = str(u.last_login)
        else:
            messages.error(request, "Password does not match")
    else:
        messages.error(request, "User does not exist in the system")

def is_user_auth(request):
    # checking if the request sessions have the auth credientials
    if "email" in request.session:
        return True
    else:
        return False

def get_user(request):
    user_email = request.session.get('email')
    u = user.objects.filter(email=user_email).first()
    return u

def get_userbyid(user_id):
    try:
        u = user.objects.get(pk=user_id)
        return u
    except:
        return None

# this function check if the session user is equal to another user
def user_equal(request, u):
    # getting the user who is on the session right now
    u_own = get_user(request)
    if u_own.id == u.id:
        return True
    else:
        return False
def get_user_profile(u):
    p = profile.objects.get(user = u)
    return p


def get_verfied():
    pass

def send_verification_message():
    pass

def get_current_datetime():
    return currentDateTime