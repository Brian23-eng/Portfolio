from django.db import models
import datetime as dt


class Project(models.Model):
    title = models.CharField(blank=False, max_length=200)
    url = models.CharField(blank=False, max_length=200)
    description = models.TextField(blank=False, max_length=500)
    technology = models.CharField(blank=True, max_length=200)
    image = models.ImageField(blank=False)
    
    def __str__(self):
        return f'{self.title}'

    def save_project(self):
        self.save
        
    def delete_project(self):
        self.delete
        
    class Meta:
        ordering = ['title']
        
    @classmethod
    def get_all_projects(cls):
        images = cls.objects.all()
        return images


