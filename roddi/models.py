from django.db import models
from django.contrib.auth.models import (BaseUserManager, AbstractBaseUser, UserManager)


# class Item(models.Model):
# title = models.CharFiel(max_lenght=100)
# content = models.TextField()

class User(AbstractBaseUser):
	objects = UserManager()

	user_name = models.TextField(
		verbose_name='User name',
		max_length=50,
		unique=True,
	)
	admin = models.BooleanField(default=False)
	# er en admin, men ikke super-user slik som eier

	owner = models.BooleanField(default=False)
	# eier er roddi-team, er super-user

	USERNAME_FIELD = 'username'

	REQUIRED_FIELDS = []  # brukernavn og passord kreves av default


	def get_name(self):
		# brukeren er idenitifsert gjennom navn
		return self.user_name


	def _str_(self):
		return self.user_name


	def has_perm(self, perm, obj=None):
		"Har brukeren en spesifkk tilgang?"
		return True


	def has_module_perms(self, app_label):
		"Har brukeren tilgang til å se appen `app_label`?"
		return True


	@property
	def is_admin(self):
		"Er dette en admin bruker?"
		return self.admin


	@property
	def is_owner(self):
		"Er dette en eier?"
		return self.owner


class UserManager(BaseUserManager):
	def create_user(self, user_name, password=None):
		"""
		Lager og lagrer en bruker med et gitt brukernavn og passord
		:param user_name:
		:param password:
		:return: user
		"""

		if not user_name:
			raise ValueError('Brukere må ha et brukernavn')

		user = self.model(
			user_name=self.normalize_email(user_name)
		)

		user.set_password(password)
		user.save(using=self._db)
		#dette blir lagringsdelen, se om det henger sammen

		return user

	def create_adminuser(self, user_name, password):
		"""
		Lager og lagrer en admin bruker med gitt brukernavn og passord
		:param user_name:
		:param password:
		:return: user
		"""

		user = self.create_user(
			user_name,
			password=password,
		)

		user.admin = True
		user.save(using=self._db)
		return user

	def create_owneruser(self, user_name, password):
		"""
		Lager og lagrer en "super-user"/eier med brukernavn og passord
		:param user_name:
		:param password:
		:return:
		"""

		user = self.create_user(
			user_name,
			password=password,
		)

		user.admin=True
		user.owner=True
		user.save(using=self._db)
		return user



