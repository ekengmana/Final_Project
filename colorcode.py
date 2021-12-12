from PIL import Image

def recolor(img, RGB):
    new_img = img
    fptr = str
    filter_color = (0, 0, 0)
    if RGB == 'G':
        filter_color = (0, 0.8, 0)
        fptr = 'green_after.jpg'
    elif RGB == 'B':
        filter_color = (0, 0, 1)
        fptr = 'blue_after.jpg'
    else:
        filter_color = (1, 0, 0)
        fptr = 'red_after.jpg'
    width, height = img.size
    for x in range(width):
        for y in range(height):
            pxl = img.getpixel((x, y))
            average_pixel_RGB = int((pxl[0] + pxl[1] + pxl[2]) / 3)
            new_img.putpixel((x, y), ((int(average_pixel_RGB * filter_color[0]), 
                    int(average_pixel_RGB * filter_color[1]), 
                    int(average_pixel_RGB * filter_color[2]))))
    new_img.show()
    new_img.save('recolor/' + fptr)
    return new_img

    

def merge(img1, img2):
    # assumes images  are same size
    new_img = img1
    # new_img.size = img1.size
    width, height = img1.size
    for x in range(width):
        for y in range(height):
            pxl1 = img1.getpixel((x, y))
            pxl2 = img2.getpixel((x, y))
            new_img.putpixel((x, y), (pxl1[0] + pxl2[0], pxl1[1] + pxl2[1], pxl1[2] + pxl2[2]))
    new_img.show()
    new_img.save('recolor/merged.jpg')
    



if __name__ == '__main__':
    img1 = Image.open('recolor/green_before.jpg').convert('RGB')
    img2 = Image.open('recolor/blue_before.jpg').convert('RGB')
    recolor_img1 = recolor(img1, 'G')
    recolor_img2 = recolor(img2, 'B')
    merge(recolor_img1, recolor_img2)
