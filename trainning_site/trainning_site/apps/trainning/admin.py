from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import ugettext_lazy as _

from trainning_site.apps.trainning.models import SystemUser
from trainning_site.apps.trainning.forms import (SystemUserChangeForm, SystemUserCreationForm)

class SystemUserAdmin(UserAdmin):
	# The forms to add and change user instances
	form = SystemUserChangeForm
	add_form = SystemUserCreationForm
	# The fields to be used in displaying the User model.
	# These override the definitions on the base UserAdmin
	# that reference the removed 'username' field
	list_display = ('username','email','password','is_superuser')
	list_filter = ('is_superuser',)
	fieldsets = (
	    (None, {'fields': ('username','email', 'password')}),
	    ('Personal info', {'fields': ('username',)}),
	    ('Permissions', {'fields': ('is_superuser',)}),
	)
	# add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
	# overrides get_fieldsets to use this attribute when creating a user.
	add_fieldsets = (
	    (None, {
	        'classes': ('wide',),
	        'fields': ('username','email',  'password1', 'password2')}
	    ),
	)
	search_fields = ('email',)
	ordering = ('email',)
	filter_horizontal = ()

admin.site.register(SystemUser, SystemUserAdmin)
