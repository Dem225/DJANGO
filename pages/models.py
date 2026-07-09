from django.db import models

# Create your models here.
class ContactMessage(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField()
    message=models.TextField()
    created_at=models.DateTimeField(
        auto_now_add=True
    )
    is_treated=models.BooleanField(default=False)
    
    def __str__(self):
        return f"{self.name} - {self.email} - {self.message}"
                                                        




class inscription_page(models.Model):
    name=models.CharField(max_length=100)
    role=models.CharField(max_length=10)
    matricule=models.CharField(max_length=12)
    user_name=models.CharField(max_length=12)
    pass_word=models.CharField(max_length=20)
    created_at=models.DateTimeField(
        auto_created=True
    )
    is_treated=models.BooleanField(default=False)
    def __str__(self):
        return f"{self.role}-{self.user_name}"