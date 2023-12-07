from django.db import models
from django.contrib.auth.models import User

POST_STATUS = (
    (0, "Draft"),
    (1, "Publish")
)

class Category(models.Model):
    name = models.CharField(max_length=40)
    
    class Meta: 
        verbose_name = "Category"   
        verbose_name_plural = "Categories"
    def __str__(self):
        return self.name
        

class Posts(models.Model):
    title = models.CharField(max_length=100, unique=True)
    subtitle = models.CharField(max_length=300, blank=True)
    slug = models.SlugField(unique=True)
    content = models.TextField()
    publish_date = models.DateTimeField()
    update_date =models.DateTimeField(auto_now_add=True, null=True)
    author = models.ForeignKey(User, on_delete= models.CASCADE)
    status = models.IntegerField(choices=POST_STATUS, default=0)
    categories = models.ManyToManyField(Category, blank=True)
    meta_description = models.CharField(max_length=200, blank=True)

    class Meta:
        ordering = ['publish_date']
        verbose_name = "Post"   
        verbose_name_plural = "Posts"
    def __str__(self):
        return self.title
    
