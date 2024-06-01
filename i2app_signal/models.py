from django.db import models
# Create your models here.


class User(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=2555, unique=True)

    def __str__(self):
        return f"this is User Instance Save{self.name}"


class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return f"this is Category instance{self.name}"


class Device(models.Model):
    name = models.CharField(max_length=255)
    category = models.ForeignKey(Category, null=True, blank=True,
                                 related_name='category_device', on_delete=models.CASCADE)

    def __str__(self):
        return f"this is Device instance{self.name}"


class Task(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    device = models.ManyToManyField(
        Device, related_name='device_task', blank=True)
    price = models.IntegerField()

    def __str__(self):
        return f"this is task instance{self.name}-{self.description}"

# from django.db.models import Count
# t1=Task.objects.annotate(price_value=Count('price'))

# from django.db.models import Count
# t2=Task.objects.aggregate(price_count=Count('price'))


class CustomManager(models.Manager):
    def get_queryset(self) -> models.QuerySet:
        return super().get_queryset().filter(comp_location="Mumbai")


class Company(models.Model):
    company_choice = (
        ("IT", "Information technology"),
        ("Sales", "Sales"),
        ("Telecom", "TC")
    )

    comp_name = models.CharField(max_length=255)
    comp_location = models.CharField(max_length=255)
    comp_type = models.CharField(
        max_length=8, choices=company_choice, default="IT")

    objects = models.Manager()
    custom_object = CustomManager()

    def __str__(self):
        return self.comp_name


class HospitalManger(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(name="Rashoma")


class Hospital(models.Model):
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)

    # objects=HospitalManger()

    def __str__(self):
        return self.name+"-"+self.location
