from django.shortcuts import render, get_object_or_404
from .models import Identity, Service, Education, Experience, Skill, Work, Uploadresume
from django.core.mail import send_mail
from django.http import JsonResponse
from django.conf import settings
from django.contrib import messages

# Create your views here.
def home(request):
    identity = Identity.objects.first()
    identity = Identity.objects.first()
    
    resume = Uploadresume.objects.first()
    
    context = {
        'identity': identity,
        'resume': resume,
    }
    return render(request, 'home.html', context)

def about(request):
    identity = Identity.objects.first()
    services = Service.objects.all()
    context = {
        'identity': identity,
        'services': services,
    }

    return render(request, 'about.html', context)

def resume(request):
    education = Education.objects.all()
    experience = Experience.objects.all()
    skill = Skill.objects.all()
    
    context = {
        'education': education,
        'experience':experience,
        'skill': skill
    }
    
    return render(request, 'resume.html', context)

def contact(request):
    identity = Identity.objects.first()
    
        
    if request.method == 'POST':
        object = request.POST.get('object')
        sender_email = request.POST.get('email')
        message = request.POST.get('message')

        # Compose and send the email
        send_mail(
            object, 
            f"from: {sender_email} \n{message}",
            settings.DEFAULT_FROM_EMAIL,
            ['michelnyembo.dev@gmail.com'],
            fail_silently=False,
        )
        
        messages.success(request, 'Email has been sent successfully!')
         
    context = {
        'identity': identity,
    }
    return render(request, 'contact.html', context)

def work(request):
    work = Work.objects.all()
    context = {
        'work': work,
    }
    return render(request, 'work.html', context)
        
