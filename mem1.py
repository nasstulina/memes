from PIL import Image, ImageDraw, ImageFont

print('Генератор мемов запущен!')

top_text = input('Введите верхний текст: ')  # вводим верхний и нижний текст
bottom_text = input('Введите нижний текст: ')

print('Список картинок:') # выводи список имеющихся картинок
print('1.Кот в очках')
print('2.Кот улыбается')
print('3.Недовольный кот')

image_number = int(input('Введите номер картинки: '))

if image_number == 1:
    image_file = 'cat_with_glasses.png'
elif image_number == 2:
    image_file = 'cat_smile.png'
elif image_number == 3:
    image_file = 'orig.webp'


image = Image.open(image_file) # открываем картинку
width, height = image.size # устанавливаем размеры(ширина, высота) изображения равные выбранной картинке

draw = ImageDraw.Draw(image)

font = ImageFont.truetype('arial.ttf', size=50) # настраиваем шрифт

text = draw.textbbox((0, 0), top_text, font) # draw.textbbox() возвращает (left, top, right, bottom), (0, 0) - начинаем отсчет с левого верхнего угла
text_wigth = text[2] - text[0] # вычисляем ширину текста: left - fight
draw.text(((width - text_wigth) / 2, 0), top_text, font=font, fill='white', stroke_width=2, stroke_fill='black') # stroke_width=2, stroke_fill='black' - обводка текста

text = draw.textbbox((0, 0), bottom_text, font)
text_wigth = text[2] - text[0]
text_hight = text[3] - text[1]
draw.text(((width - text_wigth) / 2, (height - text_hight - 30)), bottom_text, font=font, fill='white', stroke_width=2, stroke_fill='black')
# По горизонтали (ось X) текст позиционируется по центру изображения:
# (width - text_wigth) / 2 — это сдвиг, который обеспечивает центрирование текста,
# где width — ширина изображения, а text_wigth — ширина текста в пикселях.
#
# По вертикали (ось Y) текст рисуется ближе к нижнему краю изображения:
# (height - text_hight - 10) — это позиция по вертикали, где height — высота изображения,
# text_hight — высота текста, а 10 — дополнительный отступ от нижнего края.

image.show()
image.save("new_meme.jpg")
