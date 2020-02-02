from django.shortcuts import render
from django.core.mail import send_mail


def index(request):
    return render(request, 'index.html', {})


def index(request):
    return None

def contact(request):
    if request.method == "POST":
        #do stuff
        message_name = request.POST['message-name']
        message_email = request.POST['message-email']
        message = request.POST['message']
        return render(request, 'contact.html', {'message_name': message_name})

        send_mail(message_name, message, message_email, ['seiyu32@gmail.com'], fail_silently=False,)

    else:
        return render(request, 'contact.html', {})

def about(request):
    return render(request, 'about.html', {})

def blog(request):
    return render(request, 'blog.html', {})

def blog_details(request):
    return render(request, 'blog-details.html', {})
