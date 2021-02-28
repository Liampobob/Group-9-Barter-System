from django.db import models
from datetime import datetime as dt

# Create your models here.

class User(models.Model):
	username = models.SlugField(max_length=32, primary_key=True)
	password = models.CharField(max_length=20)
	phone_number = models.CharField(max_length=20)
	latitude = models.FloatField(null=True)
	longitude = models.FloatField(null=True)

	def __str__(self):
		return self.username

	@property
	def location(self):
		return (self.latitude, self.longitude)

class JobManager(models.Manager):
	def get_jobs_with_client(self, username):
		return super().get_queryset().filter(client_username=username)

	def get_all_OpenUrgent_jobs(self):
		return super().get_queryset().filter(
			(status=Job.Status.OPEN)
			| (status=Job.Status.URGENT)
		)
		"""
		def getAllOpenUrgentJobs():
			q = Job.objects.filter(
				Q(status=Job.Status.OPEN)
				| Q(status=Job.Status.URGENT)
			)
			q_str = str(q.query)
			return q_str
		"""

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
