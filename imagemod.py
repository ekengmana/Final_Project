from PIL import Image


def alter_image():
    img = Image.open('img.jpg').convert('RGB')
    new_img = Image.open('img.jpg').convert('RGB')
    width, height = img.size
    total_RGB = [0, 0, 0]
    for x in range(width):
        for y in range(height):
            pxl = list(img.getpixel((x, y)))
            total_RGB[0] += pxl[0]
            total_RGB[1] += pxl[1]
            total_RGB[2] += pxl[2]
    
    total_pix = width * height
    average_RGB = [0, 0, 0]
    for i in range(len(total_RGB)):
        average_RGB[i] = int(total_RGB[i] / total_pix)
    print(average_RGB)
    for x in range(width):
        for y  in range(height):
            pxl = list(img.getpixel((x, y)))
            if pxl[0] <= (average_RGB[0] + 50):
                new_img.putpixel((x, y), (0, 0, 0))
    new_img.save('altered3.jpg')
    


if __name__ == '__main__':
    alter_image()
