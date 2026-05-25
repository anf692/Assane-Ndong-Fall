from django.db import models


# ================================
# MODÈLE : Projet
# ================================
class Projet(models.Model):
    titre       = models.CharField(max_length=200)       
    description = models.TextField()                        
    technologies = models.CharField(max_length=300)     
    image       = models.ImageField(upload_to='projets/', blank=True, null=True)
    lien_demo   = models.URLField(blank=True, null=True)    
    lien_code   = models.URLField(blank=True, null=True)   
    ordre       = models.PositiveIntegerField(default=0)   
    created_at  = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['ordre', '-created_at'] 
        verbose_name = 'Projet'
        verbose_name_plural = 'Projets'

    def __str__(self):
        return self.titre

    def get_technologies_list(self):
        # Retourne la liste des technologies sous forme de liste Python
        return [t.strip() for t in self.technologies.split(',')]


# ================================
# MODÈLE : Formation
# ================================
class Formation(models.Model):
    date_debut  = models.CharField(max_length=50)            
    date_fin    = models.CharField(max_length=50)          
    titre       = models.CharField(max_length=200)
    etablissement = models.CharField(max_length=200)
    description = models.TextField(blank=True)

    class Meta:
        verbose_name = 'Formation'
        verbose_name_plural = 'Formations'

    def __str__(self):
        return f"{self.titre} — {self.etablissement}"

    def get_periode(self):
        return f"{self.date_debut} - {self.date_fin}"


# ================================
# MODÈLE : Certification
# ================================
class Certification(models.Model):
    titre      = models.CharField(max_length=200)
    organisme  = models.CharField(max_length=200)        
    lien       = models.URLField(blank=True, null=True)   

    class Meta:
        verbose_name = 'Certification'
        verbose_name_plural = 'Certifications'

    def __str__(self):
        return f"{self.titre} — {self.organisme}"


# ================================
# MODÈLE : Message (formulaire contact)
# ================================
class Message(models.Model):
    nom        = models.CharField(max_length=100)
    email      = models.EmailField()
    contenu    = models.TextField()
    lu         = models.BooleanField(default=False)       
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Message'
        verbose_name_plural = 'Messages'

    def __str__(self):
        return f"Message de {self.nom} — {self.email}"
