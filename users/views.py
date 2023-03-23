from django.shortcuts import render, HttpResponseRedirect
from django.contrib import auth, messages
from users.models import User
from django.urls import reverse, reverse_lazy

from django.contrib.auth.views import LoginView
from django.views.generic.edit import CreateView, UpdateView
from django.contrib.messages.views import SuccessMessageMixin
from common.views import TitleMixin

from users.forms import UserLoginForm, UserRegistratonForm, UserProfileForm
from products.models import Basket


class UserLoginView(LoginView):
    template_name = 'users/login.html'
    form_class = UserLoginForm

class UserRegistrationView(SuccessMessageMixin, TitleMixin, CreateView):
    model = User
    form_class = UserRegistratonForm
    template_name = 'users/registration.html'
    success_url = reverse_lazy('users:profile')
    success_message = 'Вы успешно зарегестрировались'
    title = 'Регистрация'

class UserProfileView(TitleMixin, UpdateView):
    model = User
    form_class = UserProfileForm
    template_name = 'users/profile.html'
    title = 'Личный кабинет'
    def get_success_url(self):
        return reverse_lazy('users:profile', args=(self.object.id))

    def get_context_data(self, **kwargs):
        context = super(UserProfileView, self).get_context_data()
        context['baskets'] = Basket.objects.filter(user=self.request.user)
        return context



# def login(request):
#     if request.method == 'POST':
#         form = UserLoginForm(data=request.POST)
#         if form.is_valid():
#             username = request.POST['username']
#             password = request.POST['password']
#             user = auth.authenticate(username=username, password=password)
#             if user:
#                 auth.login(request, user)
#                 return HttpResponseRedirect(reverse('index'))
#
#     else:
#         form = UserLoginForm()
#     context = {'form': UserLoginForm}
#     return render(request, 'users/login.html', context)

# def logout(requst):
#     auth.logout(requst)
#     return HttpResponseRedirect(reverse('index'))


# @login_required
# def profile(request):
#     if request.method == 'POST':
#         form = UserProfileForm(instance=request.user, data=request.POST, files=request.FILES)
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect(reverse('users:profile'))
#     else:
#         form = UserProfileForm(instance=request.user)
#         baskets = Basket.objects.filter(user=request.user)
#     context = {'title': 'Профиль',
#                'form': form,
#                'baskets': baskets,
#                }
#     return render(request, 'users/profile.html', context)



# def registration(request):
#     if request.method == 'POST':
#         form = UserRegistratonForm(data=request.POST)
#         if form.is_valid():
#             form.save()
#             messages.success(request, 'Вы успешно зарегестрировались')
#             return HttpResponseRedirect(reverse('users:login'))
#     else:
#         form = UserRegistratonForm()
#     context = {'form': form}
#     return render(request, 'users/registration.html', context)
