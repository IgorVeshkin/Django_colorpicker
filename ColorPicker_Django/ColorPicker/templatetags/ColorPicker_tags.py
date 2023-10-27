from django import template

register = template.Library()

# В данном разделе формируются кастомные теги пользователя

# Формируем "простой" пользовательский тег с именем get_last_color,
# ему передается запись текущего изображения в базе данных в виде аргумента


@register.simple_tag(name="get_last_color")
def get_last_color(image_holder):

    # Запускаем проверку try-except
    try:
        # Если у текущего изображения есть хотя бы один цвет, связанный с ним
        # То мы берем последный из них по id (с самым большим id)

        HEX_color = image_holder.colorholder_set.all().latest("id")

        # И возвращаем его

        return HEX_color.HEX

    # Иначе, возвращаем текст

    except:
        return "No Last Color"
