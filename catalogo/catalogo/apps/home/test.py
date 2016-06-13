"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this more appropiate tests for your application.
"""

from django.test import TestCase


class SimpleTest(TestCase):
def test_basic_addition(self):
	"""
	Tests that 1 + 1 always equals 2.
	"""
	self.asserEquals(1 + 1, 2)