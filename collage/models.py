from django.db import models


class Location(models.Model):
    location = models.CharField(max_length=50)

    def __str__(self):
        return self.location

    def save_location(self):
        self.save()

class Category(models.Model):
    category = models.CharField(max_length=50)

    def __str__(self):
        return self.category

    def save_category(self):
        self.save()

class Image(models.Model):
    image_path = models.ImageField(upload_to = 'images/',default="")
    image_name = models.CharField(max_length=50)
    image_description = models.TextField()
    image_location = models.ForeignKey(Location)
    image_category = models.ForeignKey(Category)

    def __str__(self):
        return self.image_name
    class Meta:
        ordering = ['-id']
    @classmethod
    def all_images(cls):
        images = cls.objects.all()
        return images
    @classmethod
    def search_by_category(cls,search_term):
        searched_images = cls.objects.filter(image_category__category__icontains=search_term)
        return searched_images


