from django.views.generic import CreateView

from ..forms import CustomerUserCreationForm
from ..models.accounts import CustomerUser

class RegisterView(CreateView):
    model = CustomerUser
    form_class = CustomerUserCreationForm
    template_name = "accounts/register.html"
    success_url = "/"

register_view = RegisterView.as_view()