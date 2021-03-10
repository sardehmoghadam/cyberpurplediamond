from django.contrib.auth import login, logout, authenticate
from .models import contactmodel, blog
from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.models import User
from django_email_verification import send_email
from django.core.mail import EmailMessage
from .tokens import account_activation_token
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.contrib.sites.shortcuts import get_current_site
from django.contrib.auth.tokens import default_token_generator
from pyattck import Attck
from django.contrib.auth import get_user_model
# Create your views here.

def index(request):
    flag = False
    if not request.user.is_authenticated:
        flag = True
    return render(request, "temp/index.html",{
        "flag": flag
    })

def contact(request):
    flag = False
    if not request.user.is_authenticated:
        flag = True
    if request.method == "POST":
        # form = contactform(request.POST)
        # if form.is_valid():
            # name = form.cleaned_data["name"]
            # email = form.cleaned_data["email"]
            # subject = form.cleaned_data["subject"]
            # desc = form.cleaned_data["desc"]
            name = request.POST["name"]
            email = request.POST["email"]
            subject = request.POST["subject"]
            desc = request.POST["desc"]
            f = contactmodel(name=name, email=email, subject=subject, desc=desc, readed=False)
            f.save()
            return render(request, "temp/contact.html", {
                "flag": flag
            })
    else:
            # return render(request, "temp/contact.html",{
            #     "form": form
            # })
            return render(request, "temp/contact.html", {
                "flag": flag
    })
def feature(request):
    flag = False
    if not request.user.is_authenticated:
        flag = True
    attack = Attck()

    for technique in attack.enterprise.techniques:
        print(technique.id)
        print(technique.name)
    return render(request, "temp/features.html", {
        "flag": flag,
        'attack': attack
    })

def mitrematrix(request):
    flag = False
    if not request.user.is_authenticated:
        flag = True
    return render(request, "temp/compass.html",{
        "flag": flag
    })

def news(request):
    flag = False
    if not request.user.is_authenticated:
        flag = True
    posts = blog.objects.all()
    return render(request, "temp/news.html", {
        "flag": flag,
        "posts": posts
    })
def about(request):
    flag = False
    if not request.user.is_authenticated:
        flag = True
    posts = blog.objects.all()
    return render(request, "temp/about.html", {
        "flag": flag
    })

def post(request, pk):
    flag = False
    if not request.user.is_authenticated:
        flag = True
    content = blog.objects.get(pk=pk)
    content.totalread = content.totalread + 1
    context = {
        'content': content
    }
    return render(request, "temp/post.html", {
        "flag": flag,
        "content": content
    })

def register(request):
    flag = False
    if not request.user.is_authenticated:
        flag = True
    if request.method == "POST":
        name = request.POST["name"]
        useremail = request.POST["email"]
        password = request.POST["password"]
        confirmpassword = request.POST["confirmpassword"]
        if password == confirmpassword:
            user = User.objects.create_user(name, useremail, password)
            user.is_active = False  # Example
            user.save()
            current_site = get_current_site(request)
            mail_subject = 'Activate your account.'
            message = render_to_string('temp/acc_active_email.html', {
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': default_token_generator.make_token(user),
            })
            email = EmailMessage(
                mail_subject, message, to=[useremail]
            )
            email.send()

            return HttpResponse('Please confirm your email address to complete the registration')
        else:
            message = "Password does not match"
            return render(request, "temp/login.html", {
                "message": message
            })

    else:
        # return render(request, "temp/contact.html",{
        #     "form": form
        # })
        return render(request, "temp/login.html", {
            "flag": flag,
    })

def log_out(request):
    logout(request)
    return HttpResponseRedirect(reverse("temp:index"))

def logging(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("temp:index"), {
                "message": "Valid credentials"
            })
        else:
            return render(request, "temp/index.html", {
                "message": "Invalid credentials."
            })

    return HttpResponseRedirect(reverse("temp:index"))

def activate(request, uidb64, token):
    try:
        uid = urlsafe_base64_decode(uidb64).decode()
        user = User._default_manager.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and default_token_generator.check_token(user, token):
        user.is_active = True
        user.save()
        return HttpResponse('Thank you for your email confirmation. Now you can login your account.')
    else:
        return HttpResponse('Activation link is invalid!')

def post_detail(request, pk):
    content = blog.objects.get(pk=pk)
    content.totalread = content.totalread + 1
    context = {
        'content': content
    }
    return render(request, 'temp/post.html', context)