from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Projet, Formation, Certification, Message


def home(request):
    projets        = Projet.objects.all()
    formations     = Formation.objects.all()
    certifications = Certification.objects.all()

    context = {
        'projets'        : projets,
        'formations'     : formations,
        'certifications' : certifications,
    }
    return render(request, 'main/index.html', context)


def contact(request):
    if request.method == 'POST':
        nom     = request.POST.get('nom')
        email   = request.POST.get('email')
        contenu = request.POST.get('message')

        # Enregistre le message en base de données
        Message.objects.create(nom=nom, email=email, contenu=contenu)

        messages.success(request, f'Merci {nom} ! Votre message a bien été envoyé.')
        return redirect('home')

    return redirect('home')

