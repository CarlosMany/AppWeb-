from django.test import TestCase, Client
from django.urls import reverse
from .models import Cliente, Producto, Contacto, Empresa, Venta
from .forms import ClienteForm

class SimpleTest(TestCase):
    def test_basic_addition(self):
        self.assertEqual(1 + 1, 2)

class ClienteModelTest(TestCase):
    def setUp(self):
        self.cliente = Cliente.objects.create(nombre='Test Cliente', email='test@cliente.com')

    def test_cliente_creation(self):
        self.assertEqual(self.cliente.nombre, 'Test Cliente')
        self.assertEqual(self.cliente.email, 'test@cliente.com')

    def test_cliente_str(self):
        self.assertEqual(str(self.cliente), self.cliente.nombre)

class IntegrationTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.cliente = Cliente.objects.create(nombre='Integration Test Cliente', email='integration@test.com')

    def test_cliente_list_view(self):
        response = self.client.get(reverse('cliente_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Integration Test Cliente')

    def test_cliente_detail_view(self):
        response = self.client.get(reverse('cliente_detail', args=[self.cliente.id]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'integration@test.com')

    def test_login_view(self):
        response = self.client.post(reverse('login'), {'username': 'admin', 'password': 'admin'})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Invalid login')

class FormTest(TestCase):
    def test_cliente_form(self):
        form_data = {'nombre': 'Form Test Cliente', 'email': 'form@test.com'}
        form = ClienteForm(data=form_data)
        self.assertTrue(form.is_valid())
        cliente = form.save()
        self.assertEqual(cliente.nombre, 'Form Test Cliente')
        self.assertEqual(cliente.email, 'form@test.com')
