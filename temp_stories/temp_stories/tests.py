from django.test import Client, TestCase
from django.urls import reverse


# Create your tests here.
class TemperatureTests(TestCase):

	def test_temp_text(self):
		client = Client()
		response = client.get('/')
		self.assertEqual(response.status_code, 200)
		self.assertContains(response, "Enter the temperature in fahrenheit")
	
	def test_convert(self):
		self.assertEqual(100.000, convert(212))
	
	def test_temp_form(self):
		client = Client()
		response = client.post('/', {'temp': 32})
		self.assertEqual(response.status_code, 200)
		self.assertContains(response, "Your converted temperature of 32 in F is 0.0 in C")

	
	# def test_story_text(self):
	# 	client = Client()
	# 	response = client.get('/')
	# 	self.assertEqual(response.status_code, 200)
	# 	self.assertContains(response, "which spurs him into conflict with")

	# def test_view_uses_correct_template(self):
	# 	response = self.client.get(reverse('index'))
	# 	self.assertEqual(response.status_code, 200)
	# 	self.assertTemplateused(response, 'temp_stories/index.html')	