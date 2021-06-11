from django.db import models

# Create your models here.

class text_editor(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=300)
    text = models.CharField(max_length=3000)
    det = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title