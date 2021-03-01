from PIL import Image
import os.path

def avg_img_color(slice):

    h = slice.histogram()

    r = h[0:256]
    g = h[256:256*2]
    b = h[256*2: 256*3]

    rr = sum( slice*w for slice, w in enumerate(r) ) / sum(r)
    gg = sum( slice*w for slice, w in enumerate(g) ) / sum(g)
    bb = sum( slice*w for slice, w in enumerate(b) ) / sum(b)

    return (
        round(rr),
        round(gg),
        round(bb))


def get_avg_pix(width,height,pixels):
    total_rgb = [0, 0, 0]

    for x in range(width):
        for y in range(height):
            for i in range(3):
                total_rgb[i] += int(pixels[x, y][i])

    return [float(x)/(width*height) for x in total_rgb]

def get_concat_h(im1, im2):
    dst = Image.new('RGB', (im1.width + im2.width, im1.height))
    dst.paste(im1, (0, 0))
    dst.paste(im2, (im1.width, 0))
    return dst

def get_concat_v(im1, im2):
    dst = Image.new('RGB', (im1.width, im1.height + im2.height))
    dst.paste(im1, (0, 0))
    dst.paste(im2, (0, im1.height))
    return dst

def slice(grid, im, step_w, step_h):
    img_slice = [[] for i in range(grid)]

    for i in range(grid):
        for j in range(grid):
            img_slice[i].append(im.crop((i * step_w, j * step_h, (i + 1) * step_w, (j + 1) * step_h)))  # x1,y1,x2,y2
    return img_slice

def compose(grid, img_slice):

    for k in range(grid):
        for l in range(grid - 1):
            if l == 0:
                temp = get_concat_v(img_slice[k][l], img_slice[k][l + 1])
            else:
                temp = get_concat_v(temp, img_slice[k][l + 1])
        if k == 0:
            image = temp
        else:
            image = get_concat_h(image, temp)
    return image


def grab_photo(path):
    imgs = []
    valid_images = [".jpg", ".png"]
    for f in os.listdir(path):
        ext = os.path.splitext(f)[1]
        if ext.lower() not in valid_images:
            continue
        im = Image.open(os.path.join(path, f))
        im = im.resize((50,50), Image.ANTIALIAS)
        imgs.append(im)
    return imgs



def force_color(im,imavg):
    AVERAGE = imavg

    im = im.convert("RGB")
    width, height = im.size
    pixels = {(x, y): list(im.getpixel((x, y)))
              for x in range(width) for y in range(height)}

    curr_avg = get_avg_pix(width, height, pixels)

    while tuple(int(x) for x in curr_avg) != AVERAGE:

        non_capped = [0, 0, 0]
        total_rgb = [0, 0, 0]

        for x in range(width):
            for y in range(height):
                for i in range(3):
                    if curr_avg[i] < AVERAGE[i] and pixels[x, y][i] < 255:
                        non_capped[i] += 1
                        total_rgb[i] += int(pixels[x, y][i])

                    elif curr_avg[i] > AVERAGE[i] and pixels[x, y][i] > 0:
                        non_capped[i] += 1
                        total_rgb[i] += int(pixels[x, y][i])

        ratios = [1 if z == 0 else
                  x/(y/float(z))
                  for x,y,z in zip(AVERAGE, total_rgb, non_capped)]

        for x in range(width):
            for y in range(height):
                col = []

                for i in range(3):
                    new_col = (pixels[x, y][i] + 0.01) * ratios[i]
                    col.append(min(255, max(0, new_col)))

                pixels[x, y] = tuple(col)

        curr_avg = get_avg_pix(width, height, pixels)

    for pixel in pixels:
        im.putpixel(pixel, tuple(int(x) for x in pixels[pixel]))

    return im