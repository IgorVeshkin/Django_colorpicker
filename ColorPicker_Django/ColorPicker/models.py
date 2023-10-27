from django.db import models

# Create your models here.

# В данном разделе формируются модели и архитектура базы данных проекта

# Класс, представляющий собой таблицу базы данных,
# хранящую название изображения, само изображение и дату/время создания записи


class ColorPickerImageHolder(models.Model):

    image_title = models.CharField(max_length=255, blank=False)

    image_file = models.ImageField(upload_to='images/')

    upload_datetime = models.DateTimeField(auto_now_add=True)


# Класс, представляющий собой таблицу базы данных,
# хранящую цвет изображения и наиболее распространенные вариации его предстваления (HEX, RGB и так далее)

# Так же этот класс имеет поле связи с исходным изображением, из которого был получен цвет


class ColorHolder(models.Model):

    ImageHolder = models.ForeignKey(ColorPickerImageHolder, on_delete=models.CASCADE, null=False)

    HEX = models.CharField(max_length=50, blank=False)

    RGB = models.CharField(max_length=50, blank=False)

    CMYK = models.CharField(max_length=50, blank=False)

    XYZ = models.CharField(max_length=50, blank=False, default="")

    LAB = models.CharField(max_length=50, blank=False, default="")

    HSV = models.CharField(max_length=50, blank=False, default="")

    YUV = models.CharField(max_length=50, blank=False, default="")

    HSL = models.CharField(max_length=50, blank=False, default="")
