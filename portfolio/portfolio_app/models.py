from django.db import models

# Create your models here.
class Job(models.Model):
    image = models.ImageField(upload_to = 'images/')
    image_2 = models.ImageField(upload_to = 'images/',blank = True)
    image_3 = models.ImageField(upload_to = 'images/',blank = True)
    title = models.CharField(max_length = 255)
    urls = models.CharField(max_length = 255)
    description = models.TextField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def create_date_pretty(self):
        return self.created_at.strftime('%b %e %Y')

# create a Blog model here.
# properties: title, created at, description, image
class Blog(models.Model):
    title = models.CharField(max_length = 255)
    description = models.TextField(max_length=255)
    image = models.ImageField(upload_to = 'images/')
    pub_date = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def summary(self):
        return self.description[:100]

    def pub_date_pretty(self):
        return self.pub_date.strftime('%b %e %Y')

