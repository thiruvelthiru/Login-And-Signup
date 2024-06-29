from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm 

class CreateUserForm(UserCreationForm):
    class meta:
        model = User
        fields = ['username','email','password1','password2']