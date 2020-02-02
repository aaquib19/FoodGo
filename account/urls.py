from django.urls import path

from account.views import login_view, register_view, logout_view, home, edit_profile

app_name = "accounts"

urlpatterns = [
    path('', home),

    path('login/', login_view, name='login'),
    path('register/', register_view, name="register"),
    path('logout/', logout_view, name="logout"),
    path('edit-profile/', edit_profile, name="editProfile")
]
