# from django.contrib.auth import get_user_model, login, authenticate, logout
from django.views import generic
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView
from django.contrib.auth.views import LoginView as BaseLoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from .forms import SignupForm


# Create your views here.
class IndexView(LoginRequiredMixin, generic.View):
    template_name = 'boards/board_list.html'
    def get(self, request):
        return render(request, 'boards/board_list.html')

    def dispatch(self, request, *args, **kwargs):
        if not self.request.user.is_authenticated:
            return redirect('common:login')
        else:
            return redirect('boards:board_list')


# 로그인
class LoginView(BaseLoginView):
    template_name = 'common/login.html'
    authentication_form = SignupForm
    redirect_authenticated_user = True

    def get_success_url(self):
        next_url = self.request.GET.get('next')
        if next_url:
            return next_url
        else:
            return reverse_lazy('boards:board_list')


# 회원가입
class SignupView(CreateView):
    form_class = SignupForm
    template_name = 'common/signup.html'
    success_url = reverse_lazy('common:login')

    def form_valid(self, form):
        response = super().form_valid(form)
        form.save() # 회원 정보 저장
        return response
