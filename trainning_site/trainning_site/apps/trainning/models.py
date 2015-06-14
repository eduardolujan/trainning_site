from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.contrib.auth.models import BaseUserManager
from django.utils import timezone




class SystemUserManager(BaseUserManager):

	def _create_user(self, username, password, **extra_fields):
		"""
		Creates and saves a User with the given email and password.
		"""
		email = None
		try:
			email = extra_fields['email']
		except Exception as e:
			email = None

		now = timezone.now()
		if not email:
		    raise ValueError('The given email must be set')

		
		email = self.normalize_email(email)
		user = self.model(username=username,
		                  password=password,
		                  is_superuser = True,
		                   **extra_fields)
		user.set_password(password)
		user.save(using=self._db)
		return user

	def create_user(self, username, password=None, **extra_fields):
		return self._create_user(email, password, 
                         **extra_fields)

	def create_superuser(self, username, password=None, **extra_fields):
		return self._create_user(username, password, 
                         **extra_fields)


class SystemUser(AbstractBaseUser, PermissionsMixin):
	username = models.CharField(max_length=254, unique=True)
	email = models.EmailField(blank=False)
	first_name = models.CharField(_('first name'),max_length=30, blank=True)
	last_name = models.CharField(_('last name'),max_length=30, blank=True)
	address = models.CharField(_('address'),max_length=60,blank=True)
	zip_code = models.CharField(_('zipcode'),max_length=10,blank=True)
	municipality = models.CharField(_('municipality'),blank=False,max_length=25)
	state = models.CharField(_('state'),blank=False,max_length=25)
	country = models.CharField(_('country'),blank=False,max_length=25)
	is_active = models.BooleanField(_('is active'), default=True)
	is_staff = models.BooleanField(_('is staff'), default=True)
	
	USERNAME_FIELD = 'username'
	REQUIRED_FIELDS = ['email']

	objects = SystemUserManager()
	class Meta:
		verbose_name = _('user')
		verbose_name_plural = _('users')

	def get_absolute_url(self):
		return "/users/%s/" % urlquote(self.email)

	def get_full_name(self):
		full_name = '%s %s' % (self.first_name, self.last_name)
		return full_name.strip()

	def get_short_name(self):

		return self.first_name

	def email_user(self, subject, message, from_email=None):
		send_mail(subject, message, from_email, [self.email])





	
	
