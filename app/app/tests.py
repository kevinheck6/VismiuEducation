"""
Sample Tests for the app
"""

from django.test import TestCase, SimpleTestCase
from rest_framework.test import APIClient

from app import demonstrationsTests

class DemonstrationTestsMododules(TestCase):
	"""Test the demonstrationsTests module"""

	def test_add_numbers(self):
		"""Test that two numbers are added together"""
		self.assertEqual(demonstrationsTests.add(3, 8), 11)

	def test_add_numbers2(self):
		"""Test that two numbers are added together - Second Version"""
		result = demonstrationsTests.add(3, 8)

		self.assertEqual(result, 11)

	def test_subtract_numbers(self):
		"""Test that values are subtracted and returned"""
		self.assertEqual(demonstrationsTests.subtract(5, 11), -6)

class TestViews(SimpleTestCase):
	"""Test the views"""

	def test_home_page_status_code(self):
		"""Test that the home page works"""
		client = APIClient()
		response = client.get('')

		self.assertEqual(response.status_code, 200)

	#def test_about_page_status_code(self):
	#	"""Test that the about page works"""
	#	client = APIClient()
	#	response = self.client.get('/about/')
	#	self.assertEqual(response.status_code, 200)