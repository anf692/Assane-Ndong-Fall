from django.contrib import admin
from .models import Projet, Formation, Certification, Message


@admin.register(Projet)
class ProjetAdmin(admin.ModelAdmin):
    list_display  = ['titre', 'technologies', 'ordre']
    list_editable = ['ordre']


@admin.register(Formation)
class FormationAdmin(admin.ModelAdmin):
    list_display = ['titre', 'etablissement', 'date_debut', 'date_fin']


@admin.register(Certification)
class CertificationAdmin(admin.ModelAdmin):
    list_display = ['titre', 'organisme']


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display  = ['nom', 'email', 'created_at', 'lu']
    list_editable = ['lu']
    readonly_fields = ['nom', 'email', 'contenu', 'created_at']

