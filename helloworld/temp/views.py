from django.contrib.auth import login, logout, authenticate
from .models import contactmodel, blog, technique, TACTIC, malware, actor, emulation, useratt, customadversary, actionsofadversary, userans, exam

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
from django.template import loader
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import JsonResponse
from .forms import RegistrationForm
import socket
from django.contrib.auth import get_user_model
# Create your views here.

def index(request):
    form = RegistrationForm()
    flag = False
    if not request.user.is_authenticated:
        flag = True
    return render(request, "temp/index.html",{
        "flag": flag,
        "form": form
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
    return render(request, "temp/features.html", {
        "flag": flag,
        'attack': attack
    })

def preattck(request):
    flag = False
    if not request.user.is_authenticated:
        flag = True
    attack = Attck()
    return render(request, "temp/preattck.html", {
        "flag": flag,
        'attack': attack
    })

def mobile(request):
    flag = False
    if not request.user.is_authenticated:
        flag = True
    attack = Attck()
    return render(request, "temp/mobile.html", {
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
    page = 1
    page = request.GET.get('page')
    allposts = blog.objects.all()
    # use Django's pagination
    # https://docs.djangoproject.com/en/dev/topics/pagination/
    results_per_page = 5
    paginator = Paginator(allposts, results_per_page)
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    # build a html posts list with the paginated posts
    return render(request, 'temp/news.html', {
        'posts': posts,
        'flag': flag,
        'page': page
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
    return render(request, "temp/{{ pk }}.html", {
        "flag": flag,
        "content": content
    })

def register(request):
    flag = False
    if not request.user.is_authenticated:
        flag = True
    form = RegistrationForm(request.POST)
    if request.method == "POST":
        name = request.POST["username"]
        useremail = request.POST["email"]
        password = request.POST["password1"]
        confirmpassword = request.POST["password2"]
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
            # email.send()

            return HttpResponse('Please confirm your email address to complete the registration')
        else:
            message = "Password does not match"
            return render(request, "temp/login.html", {
                "message": message,
                "flag": flag,
                "form": form
            })

    else:
        # return render(request, "temp/contact.html",{
        #     "form": form
        # })
        return render(request, "temp/login.html", {
            "flag": flag,
            "form": form,
    })

def registerform(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect("")
    else:
        form = RegisterForm()
        return render(response, "",
            {
                "form":form
        })

def log_out(request):
    logout(request)
    return HttpResponseRedirect(reverse("temp:index"))

def logging(request):
    if request.method == "POST":
        email = request.POST["username"]
        password = request.POST["password"]
        username = User.objects.get(email=email)
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
    flag = False
    if not request.user.is_authenticated:
        flag = True
    content = blog.objects.get(pk=pk)
    content.totalread = content.totalread + 1
    content.save()
    return render(request, "temp/post.html", {
        "flag": flag,
        "content": content
    })

def lazy_load_posts(request):
    flag = False
    if not request.user.is_authenticated:
        flag = True
    page = request.POST.get('page')
    posts = blog.objects.all()
    # use Django's pagination
    # https://docs.djangoproject.com/en/dev/topics/pagination/
    results_per_page = 2
    paginator = Paginator(posts, results_per_page)
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    # build a html posts list with the paginated posts
    posts_html = loader.render_to_string(
        'temp/post.html',

        {'posts': posts,
         'flag': flag
         }
    )
    # package output data and return it as a JSON object
    output_data = {
        'posts_html': posts_html,
        'flag': flag,
        'has_next': posts.has_next()
    }
    return JsonResponse(output_data)

def updatemitre(request):
    flag = False
    if not request.user.is_authenticated:
        flag = True
    if request.method == "POST":
        attack = Attck()
        # emulation.objects.all().delete()
        # for tactic in attack.enterprise.tactics:
        #     for technique in tactic.techniques:
        #         q = emulation()
        #         q.ability = "(" + tactic.id + " " + tactic.name + ")" + " " + technique.id + " " + technique.name
        #         q.save()
        # p = TACTIC.objects.order_by('identifier')
        technique.objects.all().delete()
        for item in attack.enterprise.techniques:
            q = technique()
            q.identifier = item.id
            q.name = item.name
            q.description = item.description
            q.reference = item.reference
            q.stix = item.stix
            q.platform = item.platforms
            q.permission = item.permissions
            q.rel_tactic = TACTIC.objects.get(identifier='TA0009')
            q.save()
        # for item in attack.enterprise.malwares:
        #     m = malware()
        #     m.identifier = item.id
        #     m.name = item.name
        #     m.description = item.description
        #     m.reference = item.reference
        #     m.stix = item.stix
        #     m.save()
        # for item in attack.enterprise.actors:
        #     a = actor()
        #     a.identifier = item.id
        #     a.name = item.name
        #     a.description = item.description
        #     a.reference = item.reference
        #     a.stix = item.stix
        #     a.save()
    return render(request, "temp/updatemitre.html", {
        "flag": flag,
    })

def subscription(request):
    flag = False
    if not request.user.is_authenticated:
        flag = True
    return render(request, "temp/subscription.html", {
        "flag": flag,
    })

def hypothesis(request):
    flag = False
    if not request.user.is_authenticated:
        flag = True
    return render(request, "temp/hypothesis.html", {
        "flag": flag,
    })

def ai(request):
    flag = False
    if not request.user.is_authenticated:
        flag = True
    return render(request, "temp/ai.html", {
        "flag": flag,
    })

def emulate(request):
    flag = False
    user = request.user
    if not request.user.is_authenticated:
        flag = True
    # message = "Click on \"RUN\" button to run the server and then run the agent"
    message = "If you have the agent, click on start and run the agent. Otherwise, you can download it from "
    global client_socket, client_address, result, serverstatus, possibledetection, tactic, technique, command
    possibledetection = ""
    tactic=""
    technique=""
    command=""
    result = []
    serverstatus = False
    if request.method == "POST" and "form1" in request.POST:
        status = True
    if request.method == "POST" and "form2" in request.POST:
        status = False
    SERVER_HOST = "localhost"
    userattobject = useratt.objects.get(user_id=user.id)
    SERVER_PORT = userattobject.assignedport
    # send 1024 (1kb) a time (as buffer size)
    BUFFER_SIZE = 4096
    # create a socket object

    # bind the socket to all IP addresses of this host

    s = socket.socket()
    if request.method == "POST" and "run" in request.POST:
        try:
            s.bind((SERVER_HOST, SERVER_PORT))
            s.listen(5)
            # message = f"Listening as {SERVER_HOST}:{SERVER_PORT} ..."
            # global client_socket, client_address
            client_socket, client_address = s.accept()
            # message = f"{client_address[0]}:{client_address[1]} Connected!"
            # just sending a message, for demonstration purposes
            message = "Hello and Welcome".encode()
            client_socket.send(message)
        except OSError:
            message = "Server is running right now"
        serverstatus = True

    if request.method == "POST" and "stop" in request.POST:
        try:
            # close connection to the client
            client_socket.close()
            # close server connection
            s.close()
            message = "Client and server disconnected"
        except:
            message = "Failed to close the connection"
            serverstatus = True
        serverstatus = False
        message = "Client and server disconnected"
    if request.method == "POST" and "form3" in request.POST:
        command = ["ifconfig", "ls"]
        for item in command:
            try:
                client_socket.send(item.encode())
                # retrieve command results
                result.append(client_socket.recv(BUFFER_SIZE).decode())
                serverstatus = True
            except:
                message = "Failed to execute the command. Make sure the server is running and client is connected"
                command = ""
    if request.method == "POST" and "form1" in request.POST:
        tactic = request.POST["tactic"]
        technique = request.POST["technique"]
        action = request.POST["action"]
        filter = emulation.objects.get(tactic=tactic, technique=technique, action=action)
        command = filter.command
        result = [filter.tactic, filter.technique, filter.action, filter.command, filter.possibledetection]
        try:
            client_socket.send(command.encode())
            # retrieve command results
            result.append(client_socket.recv(BUFFER_SIZE).decode())
            possibledetection = "Possible detection: ['4688 ', 'Process CMD Line']"
            serverstatus = True
        except:
            message = "Failed to execute the command. Make sure the server is running and client is connected"
            possibledetection = ""
            command = ""
    if request.method == "POST" and "mannualcommand" in request.POST:
        command = request.POST["command"]
        try:
            client_socket.send(command.encode())
            # retrieve command results
            result.append(client_socket.recv(BUFFER_SIZE).decode())
        except OSError:
            message = "Failed to execute the command".encode()
        serverstatus = True

    return render(request, "temp/emulate.html", {
        "flag": flag,
        "serverstatus": serverstatus,
        "message": message,
        "result": result,
        "possibledetection": possibledetection,
        "tactic": tactic,
        "technique": technique,
        "command": command,
        "user": user.username,
        "tactic": tactic,
    })

def makeadversary(request):
    flag = False
    user = request.user
    if not request.user.is_authenticated:
        flag = True

    # message = "Click on \"RUN\" button to run the server and then run the agent"
    message = ""
    global client_socket, client_address, result, serverstatus, possibledetection, tactic, technique, command
    possibledetection = ""
    tactic=""
    technique=""
    command=""
    result = []
    listactions = []
    listadversary = []
    serverstatus = False
    allemulationobjects = emulation.objects.all()
    f = customadversary.objects.filter(user_id=user.id)
    for item in f:
        listadversary.append(item.name)
    if request.method == "POST" and "form1" in request.POST:
        status = True
    if request.method == "POST" and "form2" in request.POST:
        status = False
    SERVER_HOST = "localhost"
    userattobject = useratt.objects.get(user_id=user.id)
    SERVER_PORT = userattobject.assignedport
    # send 1024 (1kb) a time (as buffer size)
    BUFFER_SIZE = 4096
    # create a socket object

    # bind the socket to all IP addresses of this host

    s = socket.socket()
    if request.method == "POST" and "run" in request.POST:
        try:
            s.bind((SERVER_HOST, SERVER_PORT))
            s.listen(5)
            # message = f"Listening as {SERVER_HOST}:{SERVER_PORT} ..."
            # global client_socket, client_address
            client_socket, client_address = s.accept()
            # message = f"{client_address[0]}:{client_address[1]} Connected!"
            # just sending a message, for demonstration purposes
            message = "Hello and Welcome".encode()
            client_socket.send(message)
        except OSError:
            message = "Server is running right now"
        serverstatus = True
        message = f"Listening as {SERVER_HOST}:{SERVER_PORT} ..."
    if request.method == "POST" and "stop" in request.POST:
        try:
            # close connection to the client
            client_socket.close()
            # close server connection
            s.close()
            message = "Client and server disconnected"
        except:
            message = "Failed to close the connection"
            serverstatus = True
        serverstatus = False
        message = "Client and server disconnected"
    if request.method == "POST" and "form3" in request.POST:
        showadversary = request.POST["showadversary"]
        f = customadversary.objects.get(name=showadversary, user_id=user.id)
        filter = actionsofadversary.objects.filter(adversary_id=f.id)
        i = 0
        for item in filter:
            a = actionsofadversary.objects.get(order=i)
            b = emulation.objects.get(id=a.actionid)
            list = [b.tactic, b.technique, b.action, b.command, b.possibledetection]
            listactions.append(list)
            i = i + 1
    if request.method == "POST" and "runadversary" in request.POST:
        showadversary = request.POST["showadversary"]
        f = customadversary.objects.get(name=showadversary, user_id=user.id)
        filter = actionsofadversary.objects.filter(adversary_id=f.id)
        i = 0
        for item in filter:
            a = actionsofadversary.objects.get(order=i)
            b = emulation.objects.get(id=a.actionid)

            try:
                client_socket.send(b.command.encode())
                # retrieve command results
                returnedvalue = client_socket.recv(BUFFER_SIZE).decode()
                serverstatus = True
            except:
                message = "Failed to execute the command. Make sure the server is running and client is connected"
                command = ""
                returnedvalue = ""
            list = [b.tactic, b.technique, b.action, b.command, b.possibledetection, returnedvalue]
            listactions.append(list)
            i = i + 1
    if request.method == "POST" and "form1" in request.POST:
        tactic = request.POST["tactic"]
        technique = request.POST["technique"]
        action = request.POST["action"]
        selectedadversary = request.POST["selectedadversary"]
        filter = emulation.objects.get(tactic=tactic, technique=technique, action=action)
        f = customadversary.objects.get(name=selectedadversary)
        a = actionsofadversary.objects.filter(adversary_id=f.id)
        i = 0
        for item in a:
            i = i+1
        a = actionsofadversary(adversary_id=f.id, order=i,actionid=filter.id)
        a.save()
    if request.method == "POST" and "mannualcommand" in request.POST:
        command = request.POST["command"]
        # adversary.save(name=command)
        try:
            f = adversary(name=command, user_id=user.id)
            f.list = []
            f.save()
        except:
            message = "Failed to save the adversary"
        serverstatus = True

    return render(request, "temp/makeadversary.html", {
        "flag": flag,
        "serverstatus": serverstatus,
        "message": message,
        "result": result,
        "possibledetection": possibledetection,
        "tactic": tactic,
        "technique": technique,
        "command": command,
        "listadversary": listadversary,
        "listactions": listactions,
        "allemulationobjects": allemulationobjects,
    })

def certification(request):
    flag = False; first = False; last = False
    if not request.user.is_authenticated:
        flag = True
    user = request.user
    countofquestions = exam.objects.all().count()
    if userans.objects.filter(user_id=user.id).count() == 0:
        userans.objects.create(user_id=user.id, answer=[], lastanswer=1)
    else:
        useranswer = userans.objects.get(user_id=user.id)
    question = exam.objects.get(qnumber=useranswer.lastanswer)
    if countofquestions == useranswer.lastanswer:
        last = True
    if useranswer.lastanswer == 1:
        first = True
    if request.method == "POST" and "NEXT" in request.POST:
        useranswer.lastanswer = useranswer.lastanswer + 1
        useranswer.save()
        question = exam.objects.get(qnumber=(useranswer.lastanswer))
        first = False
        if countofquestions == useranswer.lastanswer:
            last = True
        if "choice1" in request.POST:
            choice = 1
        elif "choice2" in request.POST:
            choice = 2
        elif "choice3" in request.POST:
            choice = 3
        elif "choice4" in request.POST:
            choice = 4
        useranswer.answer.append("1")
    if request.method == "POST" and "PREVIOUS" in request.POST:
        useranswer.lastanswer = useranswer.lastanswer - 1
        useranswer.save()
        question = exam.objects.get(qnumber=(useranswer.lastanswer))
        last = False
        if useranswer.lastanswer == 1:
            first = True
    return render(request, "temp/certification.html", {
        "flag": flag,
        "question": question,
        "first": first,
        "last": last,
    })