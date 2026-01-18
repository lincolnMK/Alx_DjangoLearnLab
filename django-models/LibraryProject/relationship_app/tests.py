# relationship_app/tests.py
from django.test import TestCase, Client
from django.contrib.auth.models import User
from .models import UserProfile

class RoleBasedAccessTests(TestCase):
    def setUp(self):
        # Create Admin user
        self.admin_user = User.objects.create_user(username='adminuser', password='adminpass')
        profile, created = UserProfile.objects.get_or_create(user=self.admin_user)
        profile.role = 'Admin'
        profile.save()

        # Create Librarian user
        self.librarian_user = User.objects.create_user(username='librarianuser', password='librarianpass')
        profile, created = UserProfile.objects.get_or_create(user=self.librarian_user)
        profile.role = 'Librarian'
        profile.save()

        # Create Member user
        self.member_user = User.objects.create_user(username='memberuser', password='memberpass')
        profile, created = UserProfile.objects.get_or_create(user=self.member_user)
        profile.role = 'Member'
        profile.save()

        # Client for testing requests
        self.client = Client()

    # -------------------
    # Admin view tests
    # -------------------
    def test_admin_can_access_admin_view(self):
        self.client.login(username='adminuser', password='adminpass')
        response = self.client.get('/admin/tasks/')  # replace with your actual URL
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'relationship_app/admin_task.html')

    def test_librarian_cannot_access_admin_view(self):
        self.client.login(username='librarianuser', password='librarianpass')
        response = self.client.get('/admin/tasks/')
        # Should be redirected or forbidden
        self.assertIn(response.status_code, [302, 403])

    def test_member_cannot_access_admin_view(self):
        self.client.login(username='memberuser', password='memberpass')
        response = self.client.get('/admin/tasks/')
        self.assertIn(response.status_code, [302, 403])

    def test_anonymous_cannot_access_admin_view(self):
        response = self.client.get('/admin/tasks/')
        self.assertEqual(response.status_code, 302)
        self.assertTrue('/login/' in response.url)

    # -------------------
    # Librarian view tests
    # -------------------
    def test_librarian_can_access_librarian_view(self):
        self.client.login(username='librarianuser', password='librarianpass')
        response = self.client.get('/librarian/tasks/')  # replace with your URL
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'relationship_app/librarian_task.html')

    def test_member_cannot_access_librarian_view(self):
        self.client.login(username='memberuser', password='memberpass')
        response = self.client.get('/librarian/tasks/')
        self.assertIn(response.status_code, [302, 403])

    def test_admin_cannot_access_librarian_view(self):
        self.client.login(username='adminuser', password='adminpass')
        response = self.client.get('/librarian/tasks/')
        self.assertIn(response.status_code, [302, 403])

    def test_anonymous_cannot_access_librarian_view(self):
        response = self.client.get('/librarian/tasks/')
        self.assertEqual(response.status_code, 302)
        self.assertTrue('/login/' in response.url)

    # -------------------
    # Member view tests
    # -------------------
    def test_member_can_access_member_view(self):
        self.client.login(username='memberuser', password='memberpass')
        response = self.client.get('/member/tasks/')  # replace with your URL
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'relationship_app/member_task.html')

    def test_librarian_cannot_access_member_view(self):
        self.client.login(username='librarianuser', password='librarianpass')
        response = self.client.get('/member/tasks/')
        self.assertIn(response.status_code, [302, 403])

    def test_admin_cannot_access_member_view(self):
        self.client.login(username='adminuser', password='adminpass')
        response = self.client.get('/member/tasks/')
        self.assertIn(response.status_code, [302, 403])

    def test_anonymous_cannot_access_member_view(self):
        response = self.client.get('/member/tasks/')
        self.assertEqual(response.status_code, 302)
        self.assertTrue('/login/' in response.url)
