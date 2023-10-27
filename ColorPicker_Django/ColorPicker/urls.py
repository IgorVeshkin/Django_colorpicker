from django.urls import path

from . import views

from django.conf import settings
from django.conf.urls.static import static

# В этом разделе прописываются url-адреса и какие страницу будет отрендерены при переходе по этим адресам

urlpatterns = [

    # При переходе по адресу http://127.0.0.1:8000/, запуститься функция main
    path('', views.main, name="main"),

    # При переходе по адресу http://127.0.0.1:8000/load-picture/, запуститься функция load_picture
    path('load-picture/', views.load_picture, name="load-picture"),

    # При переходе по адресу http://127.0.0.1:8000/color-pick-image/<int: image_pk>, запуститься функция color_picker,
    # отображающая страницу с изображением и выбором/отображением цветов
    path('color-pick-image/<int:image_pk>', views.color_picker, name="color-pick-picture"),

    # При переходе этому адресу адресу, добавляется цвет в базы данных (ajax-запрос)
    path('add-color-to-database/', views.add_color_to_database, name="add-color-to-database"),

    # При переходе этому адресу адресу, удаляется цвет из базы данных (ajax-запрос)
    path('delete-color-from-database/', views.delete_color_from_database, name="delete-color-from-database"),

    # При переходе этому адресу адресу, удаляется изображение из базы данных (ajax-запрос)
    path('delete-image-from-database/', views.delete_image_from_database, name="delete-image-from-database"),
]

# В случаях реальных хостингов процесс поиска изображений там уже отлажен
# В целях работы с изображениями на локальном сервере компьютера в режиме отладки
# необходимо прописать отдельный статический путь до медиа-файлов в соответсвующих дерикториях проекта

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
