from django.views.generic import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy

class SignUpView(CreateView): # POST request
    template_name = 'registration/signup.html'

    # form_class attribute that allow us to create objects from a form class
    form_class = UserCreationForm
    # success_url attribute that allow us to redirect to a URL after the form is successfully submitted
    success_url = reverse_lazy('login')