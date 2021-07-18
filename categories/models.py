from django.db import models

class Category(models.Model):
    category_name = models.CharField(max_length=40)
    def __str__(self):
        return f"Category: {self.category_name}"

class Post(models.Model):
    pub_date = models.DateTimeField('date published')
    post_text = models.CharField(max_length=900)
    #Belongs to a Category
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='posts')
    def __str__(self):
        return f"Post: Published {self.pub_date}: {self.post_text}"
        
    
