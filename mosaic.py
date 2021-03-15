from image_fcns import *
from random import randrange


class Mosaic:
    def __init__(self):
        self.im = None
        self.path = None
        self.grid = None
        self.progress = None


    def prepare_slices(self):
        self.width_default, self.height_default = self.im.size
        self.im = self.im.resize((400, 400), Image.ANTIALIAS)

        width, height = self.im.size
        step_w = round(width / self.grid)
        step_h = round(height / self.grid)

        slices = slice(self.grid, self.im, step_w, step_h)
        return slices

    def make_mosaic(self, pbar):

        slices = self.prepare_slices()
        fotos = grab_foto(self.path)

        slice_output = [[] for i in range(self.grid)]
        temp_fotos = fotos
        rand = 0

        pbar.show()

        for i in range(self.grid):
            for j in range(self.grid):

                progress = int(((i * self.grid + j + 1)/ self.grid ** 2) * 100)
                pbar.setProperty("value", progress)

                if len(temp_fotos) == 1:
                    slice_output[i].append(temp_fotos[0])
                    temp_fotos.clear()
                    temp_fotos = grab_foto(self.path)
                else:
                    rand = randrange(len(temp_fotos))

                slice_output[i].append(temp_fotos[rand])
                rgb = avg_img_color(slices[i][j])
                slice_output[i][j] = force_color(slice_output[i][j], rgb)

                del temp_fotos[rand]

        image = compose(self.grid, slice_output, self.width_default, self.height_default)
        image.save('temporary_img.jpg')
        return image
