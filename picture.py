def p2p(path):
    import matplotlib.pyplot as plt
    import os, sys
    from PIL import Image,ImageFont,ImageDraw
    os.chdir(sys.path[0])
    pic = plt.imread(path)
    raw_height,raw_width,_=pic.shape
    width = int(raw_width/ 6)
    height = int(raw_height / 15)
    #这两个数字是调出来的

    ascii_char = list("$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. ")
    #生成一个ascii字符列表
    char_len = len(ascii_char)

    #使用plt.imread方法来读取图像，对于彩图，返回size = heigth*width*3的图像
    #matplotlib 中色彩排列是R G B
    #opencv的cv2中色彩排列是B G R
    #获取图像的高、宽

    gray = 0.2126 * pic[:,:,0] + 0.7152 * pic[:,:,1] + 0.0722 * pic[:,:,2]
    #RGB转灰度图的公式 gray = 0.2126 * r + 0.7152 * g + 0.0722 * b
    #思路就是根据灰度值，映射到相应的ascii_char
    im = Image.new("RGB", (raw_width,raw_height), (255, 255, 255))
    dr = ImageDraw.Draw(im)

    font = ImageFont.load_default().font
    out_x,out_y=0,0
    font_w,font_h=font.getsize(ascii_char[15])
    font_h *= 1.37 #调整字体大小
    for i in range(height):
        #根据比例映射到对应的像素
        y = int(i * raw_height / height)
        for j in range(width):
            x = int(j * raw_width / width)
            dr.text((out_x, out_y), ascii_char[int(gray[y][x] * (char_len-1))], font=font, fill=(int(pic[y,x,0]*256),int(pic[y,x,1]*256),int(pic[y,x,2]*256)))
            out_x+=font_w
        out_y+=font_h
        out_x=0


    im.show()
    im.save('output.png')
