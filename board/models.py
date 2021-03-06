from django.db import models
from django.db.models.fields import AutoField

# Create your models here. 
class Post(models.Model):
    id = models.AutoField(primary_key=True, auto_created=True)
    photo = models.ImageField(upload_to='images')
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    title = models.CharField(max_length=100)
    content = models.TextField(max_length=1000)
    likes = models.PositiveIntegerField(default=0, editable=False)
    slug = models.SlugField(unique=True)
    
    def __str__(self):
        return f'{self.title} - {self.slug}'
    
    def add_like(self):
        self.likes = self.likes + 1
    
class Comment(models.Model):
    id = models.AutoField(primary_key=True, auto_created=True)
    alias = models.CharField(max_length=50,default='Anonymous')
    comment = models.TextField(max_length=1000)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    # replies = models.ForeignKey('self', on_delete=models.CASCADE, related_name='comments', null=True)
    # make a reply model?  
    # watch videos on django model relationships
      
    def __str__(self):
        return f'{self.alias}'