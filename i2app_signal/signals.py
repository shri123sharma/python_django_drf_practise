from django.dispatch import receiver
from .models import Category, Device, Task, Hospital
from django.db.models.signals import pre_init, post_init, pre_save, post_save, pre_delete, post_delete


@receiver(pre_init, sender=Device)
def device_pre_init(sender, **kwargs):
    print(f"Pre_init: Preparing to initialize device: {sender}")


@receiver(post_init, sender=Device)
def device_post_init(sender, instance, **kwargs):
    print(f"Post_init: Device '{instance}' has been initialized!")


@receiver(pre_save, sender=Device)
def device_pre_save(sender, instance, **kwargs):
    print(f"Pre_save: Preparing to save device: {instance.name}")


@receiver(post_save, sender=Device)
def device_post_save(sender, instance, created, **kwargs):
    if created:
        print(f"Post_save: New device '{instance.name}' has been saved!")
    else:
        print(f"Post_update: Device '{instance.name}' has been updated!")


@receiver(pre_delete, sender=Device)
def device_pre_delete(sender, instance, **kwargs):
    print(f"Pre_delete:Preparing to delete device: {instance.name}")


@receiver(post_delete, sender=Device)
def device_post_delete(sender, instance, **kwargs):
    print(f"Post_delete:Device '{instance.name}' has been deleted!")


@receiver(post_save, sender=Hospital)
def hospital_post_save(sender, instance, **kwargs):
    print("Hospital objects to send to notify in receiver signal and perform task")
