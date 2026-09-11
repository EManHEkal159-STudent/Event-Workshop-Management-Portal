from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    class Role(models.TextChoices):
        ADMIN = 'ADMIN', 'Admin'
        ORGANIZER = 'ORGANIZER', 'Organizer'
        ATTENDEE = 'ATTENDEE', 'Attendee'

    role = models.CharField(
        max_length=20,
        choices=Role.choices,
        default=Role.ATTENDEE
    )
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    bio = models.TextField(blank=True, null=True)

    def is_organizer(self):
        return self.role == self.Role.ORGANIZER or self.is_superuser

    def is_attendee(self):
        return self.role == self.Role.ATTENDEE

    def __str__(self):
        return f"{self.username} ({self.get_role_display()})"
