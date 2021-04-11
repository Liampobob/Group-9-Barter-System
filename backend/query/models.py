from django.db import models
from datetime import datetime as dt
from django.contrib import auth

# Create your models here.


class BusinessReviewsManager(models.Manager):
    def get_reviews(self):
        return super().get_queryset()


class BusinessReviews(models.Model):
    user_id = models.IntegerField(null=False)
    business_id = models.IntegerField(null=False)
    review_text = models.CharField(null=False, max_length=256)
    stars = models.PositiveIntegerField(null=False)
    time = models.TimeField(auto_now=True)

    def __str__(self):
        return self.review_text

    def to_dict(self):
        d = {
            'user_id': self.user_id,
            'business_id': self.business_id,
            'review_text': self.review_text,
            'stars': self.stars,
            'time': self.time
        }
        return d

class UserManager(models.Manager):
    def get_users(self):
        return super().get_queryset()

class User(auth.models.User):
    facebook_id = models.CharField(max_length=32, null=True)
    name = models.CharField(max_length=128, null=True)
    phone_number = models.CharField(max_length=20, null=True)
    latitude = models.FloatField(null=True)
    longitude = models.FloatField(null=True)
    bio = models.CharField(null=True, max_length=256)

    def __str__(self):
        return self.username

    @property
    def location(self):
        return (self.latitude, self.longitude)

    def to_dict(self):
        d = {
            'username': self.username,
            'name': self.name,
            'phone_number': self.phone_number,
            'bio': self.bio,
            'facebook_id': self.facebook_id,
            'location': {
                'latitude': self.latitude,
                'longitude': self.longitude,
            },
        }
        return d

class BusinessManager(models.Manager):
    def get_businesses(self):
        return super().get_queryset()

class Business(User):
    is_cbo = models.BooleanField(null=False, default=False)
    contact_name = models.CharField(null=True, max_length=128)
    work_tags = models.CharField(null=True, max_length=256)
    description = models.CharField(null=True, max_length=256)
    working_days = models.CharField(null=True, max_length=128)
    start_time = models.IntegerField(null=True)
    end_time = models.IntegerField(null=True)

    def to_dict(self):
        d = {
            'name': self.name,
            'contact_name': self.contact_name,
            'work_tags': self.work_tags,
            'description': self.description,
            'phone_number': self.phone_number,
            'working_days': self.working_days,
            'start_time': self.start_time,
            'end_time': self.end_time
        }
        return d

class Listing(models.Model):
    CATEGORIES = (
        ('J', 'Job'),
        ('C', 'Class'),
        ('B', 'toBuy'),
        ('S', 'toSell'),
        ('O', 'CBO'),
    )
    posted_by = models.ForeignKey( User, null=True, on_delete=models.SET_NULL )
    date_posted = models.DateTimeField(default=dt.now(), null=False)
    title = models.CharField(max_length=128, null=False)
    category = models.CharField(max_length=1, null=False, choices=CATEGORIES)
    description = models.CharField(max_length=1024, null=False)
    owner = models.CharField(max_length=80, null=False)

    def __str__(self):
        return self.title

    def to_dict(self):
        d = {
            'posted_by': self.posted_by,
            'date_posted': self.date_posted,
            'title': self.title,
            'description': self.description,
            'category': self.category,
            'owner': self.owner
        }
        return d
