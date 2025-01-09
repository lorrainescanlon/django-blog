from django.test import TestCase
from django.urls import reverse
from .models import About
from .models import CollaborateRequest
from .forms import CollaborateForm


class TestAboutView(TestCase):
    def setUp(self):
        """ Create about me content"""
        self.about_content = About(title ="My title",
         content = "My content")
        self.about_content.save()
   
    def test_render_about_page_with_collaborate_form(self):
        """ verifies get request for about me containing a collaboratio form"""
        response = self.client.get(reverse('about'))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'My content', response.content)
        self.assertIn(b'My title', response.content)
        self.assertIsInstance(response.context['collaborate_form'], CollaborateForm)


    def test_successful_collaboration_request_submission(self):
        """ Test for a successful collaborarion request submission """

        post_data = {
            'name': 'Lorraine.',
            'email': 'lorraine@lorr.com',
            'message': 'test message, please collab with me'
        }

        response = self.client.post(reverse(
            'about'), post_data)
        self.assertEqual(response.status_code, 200)
        self.assertIn(
            b'Collaboration request received! I endeavour to respond within 2 working days.',
            response.content
        )