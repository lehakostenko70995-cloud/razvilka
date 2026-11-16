# -*- coding: utf-8 -*-
"""Обложка 1200x630 для превью ссылки в Telegram/соцсетях."""
from PIL import Image, ImageDraw, ImageFont

W, H = 1200, 630
BG = (246, 244, 239)
TX = (31, 35, 40)
MUT = (107, 112, 120)
AC = (47, 93, 98)

FONTS = r"C:\Windows\Fonts"
def f(name, size):
    return ImageFont.truetype(rf"{FONTS}\{name}", size)

f_kick  = f("segoeuib.ttf", 22)
f_title = f("segoeuib.ttf", 62)
f_sub   = f("segoeui.ttf", 30)
f_foot  = f("segoeui.ttf", 26)

img = Image.new("RGB", (W, H), BG)
d = ImageDraw.Draw(img)

PAD = 72

def tracked(draw, xy, text, font, fill, track=4):
    x, y = xy
    for ch in text:
        draw.text((x, y), ch, font=font, fill=fill)
        x += draw.textlength(ch, font=font) + track
    return x

# верхняя метка
tracked(d, (PAD, PAD), "РАЗВИЛКА", f_kick, MUT, track=5)

# акцентная черта
d.rectangle([PAD, PAD + 44, PAD + 64, PAD + 48], fill=AC)

# заголовок
lines = ["Карта решений:", "раздел, наследство,", "продажа"]
y = 176
for ln in lines:
    d.text((PAD, y), ln, font=f_title, fill=TX)
    y += 78

# подзаголовок
d.text((PAD, y + 16), "16 вопросов — и видно, что делать", font=f_sub, fill=MUT)

# нижняя линия и подпись
d.line([PAD, H - 132, W - PAD, H - 132], fill=(220, 216, 207), width=2)
d.text((PAD, H - 108), "Алексей · риелтор · Ростов-на-Дону", font=f_foot, fill=MUT)
d.text((PAD, H - 70), "развод · раздел · конфликты · срочный выкуп · оценка", font=f_foot, fill=MUT)

img.save(r"C:\Users\Admin\Desktop\DeepseekHarness\razvilka-site\og.png", optimize=True)
print("saved", img.size)
