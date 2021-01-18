import random
from PIL import Image ,ImageDraw,ImageFont
pic = "C:/Users/DELL/Desktop/验证码.png"
def getRandomColor():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)


def getRandomChar():
    random_num = str(random.randint(0, 9))
    random_lower = chr(random.randint(97, 122))
    random_upper = chr(random.randint(65, 90))
    random_char = random.choice([random_num, random_lower, random_upper])
    return random_char

def drawLine(draw):
    for i in range(5):
        x1 = random.randint(0, width)
        x2 = random.randint(0, width)
        y1 = random.randint(0, height)
        y2 = random.randint(0, height)
        draw.line((x1, y1, x2, y2), fill=getRandomColor())


def drawPoint(draw):
    for i in range(50):
        x = random.randint(0, width)
        y = random.randint(0, height)
        draw.point((x,y), fill=getRandomColor())

width = 160
height = 50

def createImg():
    bg_color = getRandomColor()
    img = Image.new(mode="RGB", size=(width, height), color=bg_color)
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype(font="SourceCodePro.ttf", size=36)
    for i in range(5):
        random_txt = getRandomChar()
        txt_color = getRandomColor()
        #print(random_txt)
        while txt_color == bg_color:
            txt_color = getRandomColor()
        draw.text((10 + 30 * i, 3), text=random_txt, fill=txt_color, font=font)
    drawLine(draw)
    drawPoint(draw)
    with open(pic, "wb") as f:
        img.save(f, format="png")

createImg()
