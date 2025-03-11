from django.db import models

class Task(models.Model):
    title = models.CharField(max_length=200)  # Task Name
    completed = models.BooleanField(default=False)  # Checkbox (Done or Not)
    created_at = models.DateTimeField(auto_now_add=True)  # Timestamp

    def __str__(self):
        return self.title
