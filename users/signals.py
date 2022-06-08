from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Profile

@receiver(post_save, sender=User)
def create_profile(sender,instance,created,**kwargs):
    if created:
        Profile.objects.create(user=instance)

#Bu dosyayı oluşturmamızın sebebi biz yeni kullanıcı ekledikçe ona otomatik profile sayfası oluşturmasınız sağlıyor.
#Apps.py dosyasına gidip import etmeyi unutma!!!!!!!!!