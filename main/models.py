from django.db import models


class Task(models.Model):
    title_task = models.CharField('Name of task', max_length=100)
    description_task = models.CharField('Description', max_length=200)
    complete = models.BooleanField(default=False)

    def __str__(self):
        return self.title_task
