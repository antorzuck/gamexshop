from django.db import models
from django.utils.text import slugify
from django_ckeditor_5.fields import CKEditor5Field
from django.contrib.auth.models import User



class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Profile(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    active_code = models.CharField(max_length=10)



class Banner(BaseModel):
    image = models.FileField(upload_to='banner')
    seo_text = models.CharField(max_length=200)

    def __str__(self):
        return self.seo_text





class Category(BaseModel):
    name = models.CharField(max_length=100, unique=True)
    description = CKEditor5Field()
    slug = models.SlugField(unique=True, blank=True)
    icon_code = models.CharField(null=True, blank=True, max_length=200)

    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = slugify(self.name)
            slug = base_slug
            counter = 1
            while Category.objects.filter(slug=slug).exists():
                slug = f"{base_slug}-{counter}"
                counter += 1
            self.slug = slug
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name





class Item(BaseModel):
    thumbnail = models.FileField(upload_to='thumbnails')
    title = models.CharField(max_length=100)
    description = CKEditor5Field()
    slug = models.SlugField(unique=True, blank=True)
    categories = models.ForeignKey(Category, on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title



class ItemPackage(BaseModel):
    item = models.ForeignKey(Item, related_name='packages', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.name} - {self.item.title}"
