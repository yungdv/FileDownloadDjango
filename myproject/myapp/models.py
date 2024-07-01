from django.db import models

class Section(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Group(models.Model):
    name = models.CharField(max_length=100)
    section = models.ForeignKey(Section, related_name='groups', on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class File(models.Model):
    name = models.CharField(max_length=100)
    file = models.FileField(upload_to='files/')
    group = models.ForeignKey(Group, related_name='files', on_delete=models.CASCADE)

    def __str__(self):
        return self.name