from django.db import models
from django.urls import reverse

# Create your models here.
from tenant_schemas.models import TenantMixin

class Tenant(TenantMixin):
    name = models.CharField(max_length=100)

    auto_create_schema = True

class Task(models.Model):
    name = models.TextField(max_length=100)
    done = models.BooleanField(default=False)

    def __str__(self):
        if self.done:
            return "%s (done)" % self.name
        else:
            return self.name
    def get_absolute_url(self):
        return reverse('list')