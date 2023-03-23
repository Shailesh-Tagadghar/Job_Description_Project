from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, logout, authenticate
from . models import *


def home(request):
    return render(request, "home.html")


def register(request):
    if request.method == 'POST':
        obj = UserCreationForm(request.POST)
        obj.save()
        return redirect("/")
    else:
        d = {'form': UserCreationForm}
        return render(request, 'form1.html', d)


def loginn(request):
    if request.method == "POST":
        uname = request.POST.get("uname")
        pswd = request.POST.get("pswd")
        user = authenticate(request, username=uname, password=pswd)
        if user is not None:
            request.session['id'] = user.id
            print(request.session.get('id'))
            login(request, user)
            return redirect("/")
        else:
            d = {"form": LoginForm}
            return render(request, "form.html", d)

    else:
        d = {"form": LoginForm}
        return render(request, "form.html", d)


def logoutt(request):
    logout(request)
    return redirect("/")


def about(request):
    return render(request, "about.html")


# def contact(request):
#     if request.method == "POST":
#         obj = ContactForm(request.POST)
#         obj.save()
#         return redirect("/")
#     else:
#         d = {'form': ContactForm}
#         return render(request, "contact.html", d)
    # return render(request, "form2.html")

# def contact(request):
#     if request.method == "POST":
#         form = ContactForm(request.POST)
#         if form.is_valid():
#             form.save()
#     else:
#         form = ContactForm()
#     return render(request, 'contact.html', {'form': form})

def contact(request):
    if request.method == "POST":
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        email = request.POST.get('email')
        contact = request.POST.get('contact')
        msg = request.POST.get("msg")
        obj = Contact()
        obj.fname = fname
        obj.lname = lname
        obj.email = email
        obj.contact = contact
        obj.msg = msg
        obj.save()
        return redirect("/")
    else:
        d = {"form": ContactForm}
        return render(request, "contact.html")

# def contact1(request):
#     # fname = request.GET.get("fname")
#     # lname = request.GET.get("lname")
#     # email = request.GET.get("email")
#     # contact = request.GET.get("contact")
#     # msg = request.GET.get("msg")
#     if request.method == "POST":
#         obj = ContactForm(request.POST)
#         obj.save()
#         return redirect("/")
#     else:
#         d = {'form': ContactForm}
#         return render(request, "form2.html", d)


def follow(request):
    return render(request, "follow.html")


def feedback(request):
    return render(request, "feedback.html")


def vacancies(request):
    return render(request, "vacancies.html")


def nextpage(request):
    return render(request, 'nextpage.html')


def New_User(request):
    if request.method == "POST":
        obj = UserCreationForm(request.POST)
        obj.save()
        return redirect("/")
    else:
        d = {'form': UserCreationForm}
        return render(request, "form.html", d)
