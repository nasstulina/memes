from PIL import Image, ImageDraw, ImageFont

print('Генератор мемов запущен!')

top_text = input('Введите верхний текст: ')  # Получаем верхний текст от пользователя
bottom_text = input('Введите нижний текст: ')  # Получаем нижний текст от пользователя

print('Список картинок:') # Выводим список доступных картинок для выбора
print('1. Кот в очках')
print('2. Кот улыбается')
print('3. Недовольный кот')

image_number = int(input('Введите номер картинки: ')) # Получаем номер выбранной картинки от пользователя

# Выбираем файл изображения в зависимости от выбора пользователя
if image_number == 1:
    image_file = 'cat_with_glasses.png'
elif image_number == 2:
    image_file = 'cat_smile.png'
elif image_number == 3:
    image_file = 'orig.webp'

image = Image.open(image_file) # Открываем выбранный файл изображения
width, height = image.size # Получаем ширину и высоту изображения

draw = ImageDraw.Draw(image) # Создаем объект для рисования на изображении

font = ImageFont.truetype('arial.ttf', size=50) # Загружаем шрифт Arial размером 50

# Получаем размеры текста, чтобы центрировать его
text = draw.textbbox((0, 0), top_text, font) # draw.textbbox() возвращает (left, top, right, bottom), (0, 0) - начинаем отсчет с левого верхнего угла
text_wigth = text[2] - text[0] # Вычисляем ширину текста

# Рисуем верхний текст с обводкой, центрируя его по горизонтали
draw.text(((width - text_wigth) / 2, 0), top_text, font=font, fill='white', stroke_width=2, stroke_fill='black') # stroke_width=2, stroke_fill='black' - обводка текста

# Получаем размеры нижнего текста
text = draw.textbbox((0, 0), bottom_text, font)
text_wigth = text[2] - text[0]
text_hight = text[3] - text[1]

# Рисуем нижний текст с обводкой, центрируя его по горизонтали и размещая внизу изображения
draw.text(((width - text_wigth) / 2, (height - text_hight - 30)), bottom_text, font=font, fill='white', stroke_width=2, stroke_fill='black')
# По горизонтали (ось X) текст позиционируется по центру изображения:
# (width - text_wigth) / 2 - это сдвиг, который обеспечивает центрирование текста,
# где width - ширина изображения, а text_wigth - ширина текста в пикселях.
#
# По вертикали (ось Y) текст рисуется ближе к нижнему краю изображения:
# (height - text_hight - 10) - это позиция по вертикали, где height - высота изображения,
# text_hight - высота текста, а 10 - дополнительный отступ от нижнего края.

image.show() # Открываем изображение для просмотра
image.save("new_meme.jpg") # Сохраняем изображение в файл
