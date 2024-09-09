from django.db import models
from django.utils.text import slugify


class Phone(models.Model):
    id = models.AutoField(primary_key=True)  # Поле id, которое является основным ключом модели
    name = models.CharField(max_length=255)  # Поле для названия телефона
    price = models.DecimalField(max_digits=10, decimal_places=2)  # Поле для цены телефона
    image = models.URLField(max_length=200, blank=True)  # Поле для ссылки на изображение телефона
    release_date = models.DateField()  # Поле для даты выпуска телефона
    lte_exists = models.BooleanField(default=False)  # Поле для флага наличия LTE
    slug = models.SlugField(max_length=255, unique=True, blank=True)  # Поле slug

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super(Phone, self).save(*args, **kwargs)

    def __str__(self):
        return self.name
