from django.db import models


class Task(models.Model):
    description = models.CharField(max_length=250)
    created_at = models.DateTimeField(auto_now_add=True)
    deadline = models.DateTimeField(null=True, blank=True)
    completed = models.BooleanField(default=False)
    tags = models.ManyToManyField("Tag", related_name="tasks")

    class Meta:
        ordering = ("completed", "-created_at",)

    def __str__(self) -> str:
        return self.description


class Tag(models.Model):
    name = models.CharField(max_length=250)

    def __str__(self) -> str:
        return self.name
