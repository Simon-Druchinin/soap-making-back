from django.db import models


class Flavour(models.Model):
    name = models.CharField(max_length=255, verbose_name="Название")
    price = models.PositiveIntegerField(verbose_name="Цена")
    photo = models.ImageField(verbose_name="Фотография")

    class Meta:
        verbose_name = "Отдушка"
        verbose_name_plural = "Отдушки"

    def __str__(self) -> str:
        return f"<Flavour name={self.name} price={self.price}>"


class Color(models.Model):
    name = models.CharField(max_length=255, verbose_name="Название")
    price = models.PositiveIntegerField(verbose_name="Цена")
    photo = models.ImageField(verbose_name="Фотография")

    class Meta:
        verbose_name = "Цвет"
        verbose_name_plural = "Цвета"

    def __str__(self) -> str:
        return f"<Color name={self.name} price={self.price}>"


class Shape(models.Model):
    name = models.CharField(max_length=255, verbose_name="Название")
    price = models.PositiveIntegerField(verbose_name="Цена")
    photo = models.ImageField(verbose_name="Фотография")
    is_filling_allowed = models.BooleanField(verbose_name="Возможен выбор наполнителя", default=False)

    class Meta:
        verbose_name = "Форма"
        verbose_name_plural = "Формы"

    def __str__(self) -> str:
        return f"<Shape name={self.name} price={self.price}>"


class Filling(models.Model):
    name = models.CharField(max_length=255, verbose_name="Название")
    price = models.PositiveIntegerField(verbose_name="Цена")
    photo = models.ImageField(verbose_name="Фотография")

    class Meta:
        verbose_name = "Наполнитель"
        verbose_name_plural = "Наполнители"

    def __str__(self) -> str:
        return f"<Filling name={self.name} price={self.price}>"
