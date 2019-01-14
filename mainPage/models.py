from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
import alliance.models
from django.db.models.signals import post_save
from django.dispatch import receiver


class Comment(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)


class SupportTicket(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    comments = models.ManyToManyField(Comment, blank=True)
    question_type = models.CharField(max_length=200, blank=True, null=True)
    have_been_taken = models.BooleanField(default=False)
    have_been_taken_by = models.ForeignKey(User, related_name='employee', on_delete=models.CASCADE, null=True, blank=True)


class Post(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    comments = models.ManyToManyField(Comment, blank=True)
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title


class Server(models.Model):
    name = models.CharField(max_length=50)
    player_amount = models.IntegerField(default=0)
    speed = models.FloatField(max_length=10)
    multiplication_value = models.FloatField(max_length=10)
    next_village_x = models.IntegerField(default=1575)
    next_village_y = models.IntegerField(default=1175)
    next_village_id = models.IntegerField(default=1)

    def update_village_pos(self, x, y):
        self.next_village_x = x
        self.next_village_y = y

    def __str__(self):
        return self.name


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    alliance = models.ForeignKey(alliance.models.Alliance, on_delete=models.CASCADE, blank=True, null=True)
    bio = models.TextField(null=True, blank=True)
    profile_pic = models.FileField(null=True, blank=True)
    is_premium = models.BooleanField(default=False)
    until_premium = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return str(self.user)


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()


class CityPositions(models.Model):
    village_x = models.IntegerField(default=1575)
    village_y = models.IntegerField(default=1175)

    def __str__(self):
        return self.id

