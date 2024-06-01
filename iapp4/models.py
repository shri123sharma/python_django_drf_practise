from django.db import models
# Create your models here.


class CustomManager(models.Manager):
    def get_queryset(self) -> models.QuerySet:
        return super().get_queryset().filter(post_name="personal_post")


class Post(models.Model):
    post_name = models.CharField(
        max_length=255, help_text="Enter which post upload")
    created_date = models.DateField(auto_created=True, null=True, blank=True)
    updated_date = models.DateTimeField(auto_now=True, null=True, blank=True)
    like = models.IntegerField(default=0)

    # objects=CustomManager()

    def __str__(self):
        return self.post_name


class Comment(models.Model):
    email = models.EmailField(max_length=1028, null=True)
    content = models.CharField(
        max_length=100, help_text="enter a good content")
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email
