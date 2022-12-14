from django.db import models

# Create your models here.

class Post(models.Model):
    name = models.CharField(max_length=30)
    nick = models.TextField(null=True, max_length=30)

    p_num = models.TextField(null=True, max_length=30)
    memo = models.TextField(null=True)

    b_day = models.DateTimeField(null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'[{self.pk}]{self.name}'

