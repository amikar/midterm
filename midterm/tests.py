from django.test import TestCase
from django.contrib.auth.models import User
from midterm import views

'''to run tests python manage.py test midterm -k in terminal'''
"""test where email does not have @nameofhost.com"""
class midtermtest1(TestCase):
    def test_add(self):
        views.create_user(username = "amikar", email = "amikar" , first_name = "amikar", last_name = "divij", password = "true123")
        resp = self.client.get('/login/')
        self.assertEqual(resp.status_code, 200)

"""test where password is the same as username"""
class midtermtest7(TestCase):
    def test_add(self):
        views.create_user(username="amikar", email="amikardivij@gmail.com", first_name="amikar", last_name="divij", password="amikar")
        resp = self.client.get('/login/')
        self.assertEqual(resp.status_code, 200)


"""test where all values are null"""
class midtermtest2(TestCase):
    def test_add(self):
        views.create_user(username="", email="", first_name="", last_name="", password="")
        resp = self.client.get('/login/')
        self.assertEqual(resp.status_code, 200)


"""test where password is null"""
class midtermtest3(TestCase):
    def test_add(self):
        views.create_user(username="amikar", email="amikardivij@gmail.com", first_name="amikar", last_name="divij", password="")
        resp = self.client.get('/login/')
        self.assertEqual(resp.status_code, 200)

"""test where email is null"""
class midtermtest4(TestCase):
    def test_add(self):
        views.create_user(username="amikar", email="", first_name="amikar", last_name="divij", password="true123")
        resp = self.client.get('/login/')
        self.assertEqual(resp.status_code, 200)

"""test where all values are space"""
class midtermtest5(TestCase):
    def test_add(self):
        views.create_user(username=" ", email=" ", first_name=" ", last_name=" ", password=" ")
        resp = self.client.get('/login/')
        self.assertEqual(resp.status_code, 200)

"""test where email and password are blank"""
class midtermtest6(TestCase):
    def test_add(self):
        views.create_user(username="amikar", email=" ", first_name="amikar", last_name="divij", password=" ")
        resp = self.client.get('/login/')
        self.assertEqual(resp.status_code, 200)


"""test if after registration user is redirected to registration confirmation"""
class midtermtest8(TestCase):
    def test_add(self):
        views.create_user(username="amikar", email=" ", first_name="amikar", last_name="divij", password=" ")
        resp = self.client.get('/regsec/')
        self.assertEqual(resp.status_code, 302)


