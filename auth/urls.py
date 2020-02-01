
from django.urls import path

from auth.views import login_view, register_view, logout_view, home

urlpatterns = [
    path('', home),

    path('login/', login_view),
    path('register/', register_view),
    path('logout/', logout_view)
]
