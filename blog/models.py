from django.db import models

class Post(models.Model):
    title = models.CharField(
        max_length=200,
        help_text="Blog post title"
    )
    slug = models.SlugField(
        max_length=200,
        unique=True
    )
    excerpt = models.TextField()

    content = models.TextField()

    published_date = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        
        return self.title
    class Meta:
        ordering = ['-published_date']
    