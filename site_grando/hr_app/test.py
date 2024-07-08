from django.test import TestCase, Client
from django.urls import reverse
from django.core.files.uploadedfile import SimpleUploadedFile

from users.models import User

class HrAppTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(
            username='testuser',
            password='testpassword'
        )
        
    def test_upload_vacation_data_view(self):
        url = reverse('hr_app:vacation_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'list_vacation.html')
    
    def test_upload_vacation_data(self):
        data = {
            'name': 'test_vacation',
            'vacation_date_start': '2024-05-05',
            'vacation_date_end': '2024-06-06',
            'status_confirm': 'На согласовании'
        }