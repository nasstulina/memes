from PIL import Image, ImageDraw, ImageFont

print('Генератор мемов запущен!')

top_text = input('Введите верхний текст: ')
bottom_text = input('Введите нижний текст: ')

# print(top_text, bottom_text)

print('Список картинок:')
print('1.Кот в очках')
print('2.Кот улыбается')

image_number = int(input('Введите номер картинки: '))

if image_number == 1:
    image_file = 'cat_with_glasses.png'
elif image_number == 2:
    image_file = 'cat_smile.png'

# print(image_file)

image = Image.open(image_file)
width, height = image.size

draw = ImageDraw.Draw(image)

font = ImageFont.truetype('arial.ttf', size=70)

text = draw.textbbox((0, 0), top_text, font)
text_wigth = text[2]
draw.text(((width - text_wigth) / 2, 0), top_text, font=font, fill='black')

text = draw.textbbox((0, 0), bottom_text, font)
text_wigth = text[2]
text_hight = text[3]
draw.text(((width - text_wigth) / 2, (height - text_hight - 10)), bottom_text, font=font, fill='black')

image.save("new_meme.jpg")