from lib2to3.fixes.fix_input import context

from django.contrib.auth import login, logout
from django.shortcuts import redirect
from django.contrib.auth.views import LoginView as AuthLoginView

from ..forms import CustomerUserLoginForm
from ..models.accounts import CustomerUser


class LoginView(AuthLoginView):
    template_name = "accounts/login.html"
    form_class = CustomerUserLoginForm
    model = CustomerUser

    def form_valid(self, form):
        login(self.request, form.get_user())
        return redirect("store:stor_list")

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect("store:stor_list")
        return super().get(request, *args, **kwargs)

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs.update({"request": self.request})
        return kwargs


login_view = LoginView.as_view()
