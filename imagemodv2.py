from PIL import Image


def alter_image(fptr, iteration, threshold):
    '''
    A function to alter an image to have more contrast
    **Parameters**
        fptr: *str*
            the filename
        iteration: *int*
            the iteration in counting droplets/circles
        threshold: *int*
            the threshold value of adjusting the contrast
    '''
    if iteration == 1:
        img = Image.open(fptr + '.jpg').convert('RGB')
        new_img = Image.open(fptr  + '.jpg').convert('RGB')
    else:
        # print('here')
        img = Image.open(fptr + '.jpg').convert('RGB')
        new_img = Image.open(fptr + '.jpg').convert('RGB')
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
    # print(average_RGB)
    for x in range(width):
        for y  in range(height):
            pxl = list(img.getpixel((x, y)))
            if pxl[0] <= (average_RGB[0] + threshold):
                new_img.putpixel((x, y), (0, 0, 0))
    new_img.save(fptr + '_altered' + str(iteration) + '.jpg')
    
def draw_filled(filename, iteration, ref_img):
    '''
    Function to draw in previously detected droplets
    **Parameters**
        filename: *str*
            the name of the file to be edited
        iteration: *int*
            the iteration of detecting droplets
        ref_img: *str*
            the image referred to in order to draw in previously detected droplets
    **Returns**
        None
    '''
    img = Image.open(filename)
    prev_img = Image.open(ref_img)
    # prev_img.show()
    # print(type(img))
    width, height = img.size
    for x in range(width):
        for y in range(height):
            # prev_img.show()
            pxl = [prev_img.getpixel((x, y))]
            # print(pxl)
            # obtain pixel value of calculated image before
            if pxl[0] == 0:
                # if the area is black, fill it in for the new image
                img.putpixel((x, y), (0, 0, 0))
                # print('placed pixel')
    
    img.save('img_filled' + str(iteration - 1) + '.jpg')

if __name__ == '__main__':
    alter_image('img')
