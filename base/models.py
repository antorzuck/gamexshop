from django.db import models


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True



class Banner(BaseModel):
    image = models.FileField(upload_to='banner')
    seo_text = models.CharField(max_length=200)

    def __str__(self):
        return self.seo_text


class Item(BaseModel):
    thumbnail = models.FileField(upload_to='banner')
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.title


class ItemPackage(BaseModel):
    item = models.ForeignKey(Item, related_name='packages', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.name} - {self.item.name}"
