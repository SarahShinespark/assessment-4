from django.db import models
from datetime import datetime

class Category(models.Model):
    category_name = models.CharField(max_length=40)
    def __str__(self):
        return f"{self.category_name}"

class Post(models.Model):
    pub_date = models.DateTimeField('date published', default=datetime.now)
    post_text = models.CharField(max_length=900)
    #Belongs to a Category
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='posts')
    def __str__(self):
        formatted_date = self.pub_date.strftime("%A %B %d, %Y - %H:%M:%S")
        return f"Published {formatted_date}: {self.post_text}"
        
    
