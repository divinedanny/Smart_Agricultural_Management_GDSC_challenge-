from django.test import TestCase
from .models import User

# Create your tests here.

class TestCase(TestCase):
    
    def test_register(self):
        User.objects.create(username='test', email='test@example.com', password='test', first_name='first', last_name='last', gender='male')
    



