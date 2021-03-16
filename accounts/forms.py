from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

class UserCreateForm(UserCreationForm):

  class Meta:
    # Those fields belong to auth
    fields = ('username', 'email', 'password1', 'password2')
    model = get_user_model()

  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)

    # To customize labels for form
    self.fields['username'].label = 'Display Name'
    self.fields['email'].label = 'Email Address'
