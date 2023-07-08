from django.db import models
from ckeditor.fields import RichTextField

class Identity(models.Model):
    name = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    phone=models.CharField(max_length=255)
    pro_phone=models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    pro_email = models.EmailField(max_length=255)
    address = models.CharField(max_length=500)
    pro_address = models.CharField(max_length=500)
    birthday = models.CharField(max_length=255)
    image = models.ImageField(default="", upload_to="images/")
    profil_image = models.ImageField(default="", upload_to="images/")
    about_me = RichTextField(null=True)
    
    def __str(self):
        return self.name
    

class Service(models.Model):
    icon_class = models.CharField(max_length=255)
    service = models.CharField(max_length=255)
    
    def __str(self):
        return self.service
    
class Education(models.Model):
    qualification = models.CharField(max_length=255)
    year = models.CharField(max_length=255)
    school = models.CharField(max_length=255)
    
    def __str(self):
        return self.qualification

class Experience(models.Model):
    year = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    
    def __str__(self):
        return self.title

class Skill(models.Model):
    skill = models.CharField(max_length=255)
    tag_color = models.CharField(max_length=255)
    
    def __str__(self):
        return self.skill
    
class Work(models.Model):
    name = models.CharField(max_length=255)
    type = models.CharField(max_length=255)
    image = models.ImageField(default="", upload_to='images/')
    tech_used = models.CharField(max_length=255)
    description =   RichTextField(blank=True)
    github = models.CharField(max_length=500, null=True)
    
    def __Str__(self):
        return self.name
    
class Uploadresume(models.Model):
    name = models.CharField(max_length=255)
    pdf_file = models.FileField(upload_to="images/")
    
    def __str__(self):
        return self.name
