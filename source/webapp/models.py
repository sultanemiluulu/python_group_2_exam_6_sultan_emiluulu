from django.db import models
from django.contrib.auth.models import User

class UserInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.PROTECT, related_name='client', verbose_name='User')
    phone = models.CharField(max_length=50, verbose_name='Phone', blank=True, null=True)
    friend = models.ManyToManyField(User, related_name='friend', verbose_name='Friend',
                                    blank=True)
    avatar = models.ImageField(verbose_name='Image', blank=True, null=True)

    def __str__(self):
        return self.user.get_full_name()


class Post(models.Model):
    header = models.CharField(max_length=100, verbose_name='Header', blank=True, null=True)
    text = models.TextField(max_length=2000, verbose_name='Text', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='When was created')
    author = models.ForeignKey(User, related_name='post', on_delete=models.PROTECT, verbose_name='Post')

    def __str__(self):
        return "%s, %s, %s" % (self.header, self.author, self.created_at)