from django import forms

from .models import ColorPickerImageHolder

# В этом разделе создаются формы для html-страниц

# Создаем класс формы, который связан с моделью ColorPickerImageHolder из базы данных


class ImageUploadForm(forms.ModelForm):
    class Meta:

        # Связываем данную форму с моделью ColorPickerImageHolder из базы данных
        # Берем поля модели за основу формы

        model = ColorPickerImageHolder

        # Отображаем только следующие поля модели

        fields = ("image_title", "image_file", )

        # Видоизменяем поля модели в поля формы и добавляем стороние атрибуты

        widgets = {

            # Текстовое поле

            "image_title": forms.TextInput(
                attrs={'type': 'text', 'class': 'form-control mt-1', 'placeholder': 'Название изображения',
                       'name': 'image_title',
                       'required': 'required'}),

            # Поле выбора файлов

            "image_file": forms.ClearableFileInput(
                attrs={'type': 'file', 'class': 'form-control mt-2', 'name': 'image-for-color-picker-path',
                       'accept': 'image/png, image/jpeg',
                       'required': 'required'}),

        }
