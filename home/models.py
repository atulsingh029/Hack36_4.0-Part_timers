from django.db import models
from django.contrib.auth.models import User, AbstractUser


class Account(AbstractUser):
    sex = models.CharField(max_length=15, choices=(('male', 'male'), ('female', 'female')), null=True, blank=True)
    dob = models.DateField(null=True, blank=True)
    profile_pic = models.ImageField(null=True, blank=True, upload_to='profile_pictures', default='def_user.png')
    phone = models.PositiveIntegerField(null=True, blank=True)
    type = models.CharField(choices=[('basic', 'basic'), ('advance', 'advance')], max_length=10)
    badge = models.CharField(choices=[('volunteer', 'volunteer'), ('victim', 'victim')], max_length=10)
    badge_title = models.CharField(max_length=50, null=True, blank=True)
    other_info = models.CharField(max_length=4048, null=True, blank=True)


class AlertContact(models.Model):
    name = models.CharField(max_length=255)
    geo_code = models.CharField(max_length=255)
    phone = models.PositiveIntegerField()
    email = models.EmailField(max_length=1024)
    contact_type = models.CharField(max_length=50, choices=(('police_station', 'police_station'),
                                                            ('women_helpline', 'women_helpline'), ('other', 'other')))

    def __str__(self):
        return self.geo_code


class EmergencyContact(models.Model):
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    name = models.CharField(max_length=512)
    phone = models.PositiveIntegerField()
    email = models.EmailField(max_length=1024)


class Voice(models.Model):
    account = models.OneToOneField(Account, on_delete=models.CASCADE)


class Story(models.Model):
    datetime = models.DateTimeField(auto_now_add=True, null=False, blank=False)
    storyid = models.CharField(max_length=255, unique=True)
    title = models.CharField(max_length=512, null=False, blank=False)
    story = models.CharField(max_length=204800, null=False, blank=False)
    writer = models.ForeignKey(Account, on_delete=models.SET_NULL, null=True, blank=True)
    image = models.ImageField(null=True, blank=True, upload_to='story')
    voice = models.ManyToManyField(Voice, blank=True)
    status = models.CharField(choices=[('requested', 'requested'), ('accepted', 'accepted'), ('rejected', 'rejected')],
                              max_length=10, default='accepted')
    visibility = models.CharField(
        choices=[('public', 'public'), ('advance user only', 'advance user only'), ('private', 'private')],
        max_length=20, default='public')

    def __str__(self):
        return self.title


class Comment(models.Model):
    story = models.ForeignKey(Story, on_delete=models.CASCADE)
    comment = models.CharField(max_length=512)
    datetime = models.DateTimeField(auto_now_add=True, null=False, blank=False)
    writer = models.ForeignKey(Account, on_delete=models.CASCADE)

    def __str__(self):
        return self.comment


class Help(models.Model):
    helper = models.ForeignKey(Account, on_delete=models.CASCADE, related_name='helper_account')
    receiver = models.ForeignKey(Account, on_delete=models.CASCADE, related_name='receiver_account')
    story = models.ForeignKey(Story, on_delete=models.CASCADE)
    message = models.CharField(max_length=1024)
    contact_details = models.CharField(max_length=1024)

    def __str__(self):
        return self.story.title