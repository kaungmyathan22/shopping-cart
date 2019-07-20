from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from utils.unique_slug_field_generator import unique_slug_generator, random_string_generator
from django.urls import reverse


def image_upload_path(instance, filename):

    name, ext = filename.split('.')

    if instance.slug:

        filename = f'{name}-{instance.slug}.{ext}'

    else:

        random_string = random_string_generator(size=20)

        filename = f'{name}-{random_string}.{ext}'

    return filename


class Category(models.Model):

    title = models.CharField(max_length=50)

    created = models.DateTimeField(auto_now=False, auto_now_add=True)

    updated = models.DateTimeField(auto_now=True, auto_now_add=False)

    slug = models.SlugField(blank=True, null=True)

    class Meta:

        verbose_name_plural = "Categories"

        ordering = ('-created',)

    def __str__(self):

        return self.title


class Product(models.Model):

    category = models.ForeignKey(
        to="Category", on_delete=models.CASCADE, related_name="products")

    title = models.CharField(max_length=50)

    price = models.DecimalField(max_digits=15, decimal_places=2)

    description = models.TextField()

    image = models.ImageField(
        null=True,
        blank=True,
        upload_to=image_upload_path, height_field=None, width_field=None, max_length=None)

    created = models.DateTimeField(auto_now=False, auto_now_add=True)

    updated = models.DateTimeField(auto_now=True, auto_now_add=False)

    slug = models.SlugField(blank=True, null=True)

    class Meta:

        ordering = ('-created',)

    def get_absolute_url(self):
        return reverse('product:detail', kwargs={'slug': self.slug})

    def __str__(self):

        return self.title


@receiver(post_save, sender=Product)
def product_post_save_reciever(sender, instance, created, **kwargs):

    if not instance.slug:

        slug = unique_slug_generator(instance)

        instance.slug = slug

        instance.save()


@receiver(post_save, sender=Category)
def category_post_save_reciever(sender, instance, created, **kwargs):

    if not instance.slug:

        slug = unique_slug_generator(instance)

        instance.slug = slug

        instance.save()
