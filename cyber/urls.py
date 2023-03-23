from django.urls import path
from . import views as v

urlpatterns = [
    path('', v.home),
    path('register', v.register),
    path('login', v.loginn),
    path("logout", v.logoutt),
    path('about', v.about),
    path('contact', v.contact),
    # path('contact1', v.contact1),
    path('follow', v.follow),
    path('feedback', v.feedback),
    path("vacancies", v.vacancies),
    path('nextpage', v.nextpage),
    path('New_User', v.New_User)
]
