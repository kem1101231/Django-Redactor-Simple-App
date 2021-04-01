# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from redactor.fields import RedactorField


# List of Car Types
class SimpleModel(models.Model):
	name = models.CharField(max_length=10)
	type_description = RedactorField()
	
	def __str__(self):
		return self.name
