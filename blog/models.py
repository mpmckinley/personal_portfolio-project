from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    date = models.DateField()
    content = models.TextField()
    image = models.ImageField(upload_to='portfolio/images/', blank=True)
    link = models.URLField(blank=True)

    def __str__(self):
        return self.title + ' ->  ' + self.description