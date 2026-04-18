from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"
        ordering = ['name']

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

    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name='posts',
        null=True,
        blank=True
    )

    published_date = models.DateTimeField(
        auto_now_add=True
    )

    author = models.CharField(max_length=100, default="Anonymous")

    def __str__(self):
        
        return self.title
    class Meta:
        ordering = ['-published_date']
    