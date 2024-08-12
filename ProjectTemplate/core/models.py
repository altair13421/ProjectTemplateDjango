from django.db import models

class TimeStampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class NameModel(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        abstract = True

class SoftDeleteable(models.Model):
    is_deleted = models.BooleanField(default=False)

    def delete(self, *args, **kwargs):
        self.is_deleted = True,
        self.save()

    class Meta:
        abstract = True

class BaseModel(TimeStampedModel, NameModel):
    class Meta:
        abstract = True
