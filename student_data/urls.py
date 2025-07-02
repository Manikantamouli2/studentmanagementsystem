
from django.urls import path
from .import views

urlpatterns = [
    path("",views.home,name="home"),
    path("show/",views.list_student,name="show"),
    path("update/<int:id>",views.update,name="update"),
    path("add/",views.add,name="add"),
    path("delete/<int:id>",views.delete,name="delete"),
    path("searchstudent/",views.searchstudent,name="searchstudent"),
    path("signup/",views.signup_user,name="signup"),
    path("logout/",views.logout_user,name="logout"),
    path("login/",views.login_user,name="login")
]