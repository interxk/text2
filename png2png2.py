def get_char(r,g,b,alpha = 256):
    ascii_char = list("#RMNHQODBWGPZ*@$C&98?32I1>!:-;. ")
    #ascii_char = list("$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:oa+>!:+. ")
    if alpha == 0:
        return ''
    length = len(ascii_char)
    gray = int(0.2126 * r + 0.7152 * g + 0.0722 * b)
    unit = (256.0+1)/len(ascii_char)
    return ascii_char[int(gray/unit)]
def png2png(im):
    from PIL import Image,ImageFont,ImageDraw
    import numpy as np
    raw_height,raw_width,_ = im.shape
    width = int(raw_width/ 6)
    height = int(raw_height / 15)
    color = []
    txt=''
    for x in range(height):
        for y in range(width):
            i=x*15
            j=y*6
            txt +=get_char(int(im[i,j,0]),int(im[i,j,1]),int(im[i,j,2]))
            color.append((int(im[i,j,0]),int(im[i,j,1]),int(im[i,j,2])))
        txt+='\n'
        color.append((255,255,255))

    im_txt = Image.new("RGB",(raw_width,raw_height),(255,255,255))
    dr = ImageDraw.Draw(im_txt)
    #font = ImageFont.truetype('consola.ttf', 10, encoding='unic') #改为这个字体会让图片比例改变
    font = ImageFont.load_default().font
    x,y = 0,0
    font_w,font_h=font.getsize(txt[1])
    font_h *= 1.37 #调整字体大小
    for i in range(len(txt)):
        if(txt[i]=='\n'):
            x += font_h
            y = -font_w
        dr.text((y,x),txt[i] ,fill = color[i])
        y+=font_w   
    return np.asarray(im_txt)

