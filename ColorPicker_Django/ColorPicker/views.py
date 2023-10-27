from django.shortcuts import render, redirect
from ColorPicker.forms import ImageUploadForm

from .models import ColorPickerImageHolder, ColorHolder

from django.http import JsonResponse, HttpResponseRedirect


# Create your views here.

# Главная функция представления, которая рендериться при запуске главной страницы приложения

def main(request):

    # Подключаемся к базе данных и возвращаем все объекты таблицы ColorPickerImageHolder, сортируем все записи по их id
    # ColorPickerImageHolder хранить в себе изображение, из которого считывается colorpicker-ом цвета
    # а также название изображения и дату создания записи

    image_holders = ColorPickerImageHolder.objects.all().order_by('id')

    # Формируем обязательный словарь, который передаст полученные данные на страницу

    context = {
        "ImageHolders": image_holders,
    }

    # Формируем страницу из html-документа и передаем ему данные базы данных

    return render(request, "ColorPicker/Color_Picker_images_table.html", context=context)


# Функция, вызываемая при удалении записи определенного изображения из базы данных

def delete_image_from_database(request):

    # Через Ajax-запрос получает id записи изображения, которое нужно удалить

    image_pk = request.GET.get("image_pk")

    # С помощью id находим запись в базе данных и удаляем ее

    ColorPickerImageHolder.objects.filter(id=image_pk).delete()

    # Формирует словарь, передаваемый в виде ответа на ajax-запрос

    response = {
        "message": "Successfully removed image from database!",
    }

    # Возвращаем Json-объект обратно на страницу, как ответ на запрос

    return JsonResponse(response, safe=False)


# View-функция, вызываемая при запуске страницы загрузки изображения
# либо когда на странице произошли изменения в форме загрузки изображения


def load_picture(request):
    # Если пользователь добавил данные в форму и отправил их через кнопку submit (протокол POST), то

    if request.method == 'POST':

        # Загружаем форму из заготовки, описанной в forms.py,
        # и передаем в нее данные со страницы в том числе и файл изображения

        form = ImageUploadForm(request.POST, request.FILES)

        # Если данные со страницы соответсвуют структуре формы из forms.py, то есть валидные

        if form.is_valid():

            # Сохраняем данные как запись в базе данных,
            # поскольку заготовка из forms.py, построена на основе модели из базы данных

            saved_form_data = form.save()

            # И переадресовываем пользователя на страницу отображения изображения,
            # на которую будут переданы данные новой записи из формы

            return redirect('color-pick-picture', image_pk=saved_form_data.id)

    # Иначе, если ввода данные не произошло, то есть требуется просто сформировать и вернуть страницу с формой, то

    else:

        # Создаем туже форму без введенных данных

        form = ImageUploadForm()

    # Формируем словарь элементов и информации, которая будет передана на страницу, то есть форма

    context = {
        "ImageUploadForm": form,
    }

    # Отренденриваем страницу из html-заготовки и данных словаря context

    return render(request, "ColorPicker/Color_Picker_select_picture.html", context=context)

# View-функция, вызываемая при запуске страницы выбора цвета на изображении
# Из адресной строки сайта получаем id изображения


def color_picker(request, image_pk):

    # С помощью id находим запись в базе данных из таблицы,
    # в которой храниться информация об изображении и других данных

    image_record = ColorPickerImageHolder.objects.filter(id=image_pk)[0]

    # Формируем словарь context, который состоит из id изображения,
    # записи самого изображения и списка всех цветов, полученных с помощью подбора цвета с картинки
    # и отсортированных в обратном порядке

    context = {
        'image_pk': image_pk,
        'image_record': image_record,
        'image_colors': image_record.colorholder_set.all().order_by("-id"),
    }

    # Формируем страницу и передаем ей словарь данных context

    return render(request, "ColorPicker/Color_Picker.html", context=context)

# Функция выполняет ajax-запрос, который добавляет в таблицу, хранящую цвет с изображения, новую запись


def add_color_to_database(request):
    # Подгружаем все данные из ajax-запроса в функцию
    # Все данные предстваляют собой цвет в разных формах его предствления

    image_pk, hex_color, rgb_color, cmyk_color, xyz_color, lab_color, hsv_color, yuv_color, hsl_color = request.GET.get("image_pk"), \
                                                 request.GET.get("hex_color"), \
                                                 request.GET.get("rgb_color"), \
                                                 request.GET.get("cmyk_color"), \
                                                 request.GET.get("xyz_color"), \
                                                 request.GET.get("lab_color"), \
                                                 request.GET.get("hsv_color"), \
                                                 request.GET.get("yuv_color"), \
                                                 request.GET.get("hsl_color")

    # Формируем запись на основе полученных данных
    # ImageHolder - это ForeignKey-элемент, который связует цвет с определенным изображением

    current_color = ColorHolder(ImageHolder=ColorPickerImageHolder.objects.filter(id=image_pk)[0],
                                HEX=hex_color,
                                RGB=rgb_color,
                                CMYK=cmyk_color,
                                XYZ=xyz_color,
                                LAB=lab_color,
                                HSV=hsv_color,
                                YUV=yuv_color,
                                HSL=hsl_color)

    # Сохраняем запись в базе данных

    current_color.save()

    # Формируем ответ, который вернется пользователю

    response = {
        "message": "Successfully saved color to database!",
        "color_id": current_color.id,
    }

    # Отправляет запрос

    return JsonResponse(response, safe=False)


# Функция, вызываемая ajax-запросом, удаляет цвет из базы данных

def delete_color_from_database(request):

    # Подгружаем id цвета в базе данных

    color_pk = request.GET.get("color_pk")

    # Находит цвет в базе и удаляем его

    ColorHolder.objects.filter(id=color_pk).delete()

    # Формируем ответ пользователю на ajax-запрос

    response = {
        "message": "Successfully removed color from database!",
    }

    # Отправляем ответ

    return JsonResponse(response, safe=False)
