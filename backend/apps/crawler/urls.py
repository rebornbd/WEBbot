from django.urls import path
from django.views.decorators.csrf import csrf_exempt

from .views import (home)


urlpatterns = [
    path('', home),

    # path('create', csrf_exempt(FBV_CreateView)),
    # path('update', csrf_exempt(FBV_UpdateView)),
    # path('remove', csrf_exempt(FBV_DeleteView)),

    # path('login', csrf_exempt(LoginView)),
    # path('logout', csrf_exempt(LogoutView)),
]