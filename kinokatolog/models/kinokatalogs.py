from django.db import models

class Kinokatalog(models.Model):
    name=models.CharField("Название", max_length=100)
    adress=models.CharField("Адрес", max_length=100)
    phone=models.IntegerField()
    email=models.CharField("Email", max_length=50)

    class Meta:
        verbose_name="Кинокаталоги"
        verbose_name_plural="Кинокаталог"

    def __str__(self)-> str:
        return self.name