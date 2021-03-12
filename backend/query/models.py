from django.db import models
from datetime import datetime as dt

# Create your models here.

class UserManager(models.Manager):
	def get_users(self):
		return super().get_queryset()

class User(models.Model):
	username = models.SlugField(max_length=32, primary_key=True)
	password = models.CharField(max_length=20)
	name = models.CharField(max_length=80, null=True)
	phone_number = models.CharField(max_length=20, null=True)
	latitude = models.FloatField(null=True)
	longitude = models.FloatField(null=True)
	isBusiness = models.BooleanField(default=False)
	bio = models.TextField()


	def __str__(self):
		return self.username

	@property
	def location(self):
		return (self.latitude, self.longitude)

	def to_dict(self):
		d = {
			'username' : self.username,
			'name' : self.name,
			'phone_number' : self.phone_number,
			'is_business' : self.isBusiness,
			'bio' : self.bio,
			'location' : {
				'latitude' : self.latitude,
				'longitude' : self.longitude,
			},
		}
		return d
"""
# not part of MVP
class JobManager(models.Manager):
	def get_jobs_with_client(self, username):
		return super().get_queryset().filter(client_username=username)

	def get_all_OpenUrgent_jobs(self):
		return super().get_queryset().filter(
			(status=Job.Status.OPEN)
			| (status=Job.Status.URGENT)
		)

class Job(models.Model):
	class Status(models.TextChoices):
		OPEN = "O", _('Open')
		URGENT = "U", _('Urgent')
		IN_PROGRESS = "P", _('In Progress')
		COMPLETE = "C", _('Complete')
		CANCELLED = "X", _('Cancelled')

	job_id = models.IntegerField(primary_key=True)
	client_username = models.ForeignKey(
		User,
		on_delete=models.SET_NULL
	)
	date_posted = models.DateTimeField(default=dt.now())
	title = models.CharField(max_length=100)
	job_description = models.TextField(max_length=1000)
	status = models.CharField(
		max_length=1,
		choices=Status.choices,
		default=Status.OPEN
	)
	date_closed = models.DateField(null=True, blank=True)
	worker_usernames = models.ManyToManyField(User)
"""
