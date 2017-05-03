from django.template.context_processors import csrf
from django.shortcuts import render_to_response, redirect, render, HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from django.core.mail import send_mail
from django.views.decorators.csrf import requires_csrf_token
from midterm import settings


@requires_csrf_token
def loginview(request):
    c = {}
    c.update(csrf(request))
    return render_to_response('login.html', c)


@login_required
def regsec(request):
    return render(request, 'regsec.html')


def auth_and_login(request, onsuccess='/'):
    user = authenticate(username=request.POST['email'], password=request.POST['password'])
    content = 'user does not exist go back to 127.0.0.1:8000/login/'
    if user is not None:
        login(request, user)
        return redirect(onsuccess)
    else:
        return HttpResponse(content, content_type='text/plain')


def create_user(username, email, first_name, last_name, password):
    user = User(username=username, email=email, first_name=first_name, last_name=last_name)
    user.set_password(password)
    user.save()
    subject = 'Thank you for registering'
    message = 'welcome to midterm project to login please go to http://127.0.0.1:8000/login'
    from_email = settings.EMAIL_USE_TLS
    recipient_list = [user.email, settings.EMAIL_HOST_USER]

    send_mail(subject, message, from_email, recipient_list, fail_silently=True)
    return user


def user_exists(username):
    user_count = User.objects.filter(username=username).count()
    if user_count == 0:
        return False
    return True


def sign_up_in(request):
    post = request.POST
    if not user_exists(post['email']):
        user = create_user(username=post['email'], email=post['email'], password=post['password'],
                           first_name=post['first_name'], last_name=post['last_name'])
        return render(request, 'regsec.html')
    else:
        return redirect("/login/")


def logout_view(request):
    logout(request)
    response = redirect("/login/")
    return response


@login_required(login_url='/login/')
def secured(request):
    return render(request, 'secure.html')
