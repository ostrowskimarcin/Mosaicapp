from image_fcns import *
from random import randrange
import math


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

    def make_mosaic(self, pbar, m):

        slices = self.prepare_slices()
        photos = grab_photo(self.path)

        slice_output = [[] for i in range(self.grid)]
        temp_photos = photos
        rand = 0

        pbar.show()
        
        if m == 0:
            progress=0
            counter=0
            self.width_default, self.height_default = self.im.size
            self.im = self.im.resize((400, 400), Image.ANTIALIAS)
            width, height = self.im.size
            step_w = round(width / self.grid)
            step_h = round(height / self.grid)
            sum= (self.grid**2)
            for i in range(self.grid):
                for j in range(self.grid):
                    slices[i][j] = Image.new('RGB', (step_w, step_h), avg_img_color(slices[i][j]))
                    counter = counter + 1

                    progress = (counter/sum)*100
                    pbar.setProperty("value", progress)

            ready_img = compose(self.grid, slices)
            ready_img.save('mosaic.jpg')
            return ready_img

        elif m == 1:

            slice_color = [[] for i in range(self.grid)]
            slice_output = [[] for i in range(self.grid)]
            path_color = []
            dist = []
            n = len(photos)
            counter=0
            progress=0
            act_progress=0
            sum= (self.grid**2) + n + ((self.grid**2)*n)

            for i in range(self.grid):
                for j in range(self.grid):
                    slice_color[i].append(avg_img_color(slices[i][j]))
                    counter=counter+1
                    progress= (counter/sum)*100
                    pbar.setProperty("value", progress)
            act_progress=progress

            for i in range(n):
                path_color.append(avg_img_color(photos[i]))
                counter=counter+1
                progress= act_progress + (counter/sum)*100
                pbar.setProperty("value", progress)

            act_progress=progress

            for i in range(self.grid):
                for j in range(self.grid):
                    for k in range(n):

                        h_coef = 1
                        s_coef = 0.8
                        v_coef = 0.2

                        h = 360 * slice_color[i][j][0] - 360 * path_color[k][0]
                        if h < -180:
                            h = h + 360
                        elif h > 180:
                            h = h - 360
                        h = h / 180

                        s = slice_color[i][j][1] - path_color[k][1]
                        v = (slice_color[i][j][2] - path_color[k][
                            2]) / 100

                        rms = math.sqrt(
                            (h_coef * math.pow(h, 2) + s_coef * math.pow(s, 2) + v_coef * math.pow(v, 2)) / 3)
                        dist.append(rms)
                        counter= counter+1
                        progress = act_progress + (counter/sum)*100
                        pbar.setProperty("value", progress)
                    nr = min(dist)
                    idx = dist.index(nr)

                    slice_output[i].append(photos[idx])
                    dist.clear()

            ready_img = compose(self.grid, slice_output)
            ready_img.save('mosaic.jpg')
            return ready_img

        elif m == 2:

                slice_color = [[] for i in range(self.grid)]
                slice_output = [[] for i in range(self.grid)]
                path_color = []
                dist = []
                n = len(photos)
                counter=0
                progress=0
                act_progress=0
                suma= (self.grid**2) + n + ((self.grid**2)*n)

                for i in range(self.grid):
                    for j in range(self.grid):
                        slice_color[i].append(avg_img_color(slices[i][j]))
                        counter=counter+1
                        progress= (counter/suma)*100
                        pbar.setProperty("value", progress)
                act_progress=progress

                
                for i in range(n):
                    path_color.append(avg_img_color(photos[i]))
                    counter=counter+1
                    progress= act_progress + (counter/suma)*100
                    pbar.setProperty("value", progress)
                act_progress=progress

                for i in range(self.grid):
                    for j in range(self.grid):
                        for k in range(n):
                            h = slice_color[i][j][0] - path_color[k][0]
                            s = slice_color[i][j][1] - path_color[k][1]
                            v = slice_color[i][j][2] - path_color[k][2]

                            rms = math.sqrt((math.pow(h, 2) + math.pow(s, 2) + math.pow(v, 2)) / 3)
                            dist.append(rms)
                            counter=counter+1
                            progress= act_progress + (counter/suma)*100
                            pbar.setProperty("value", progress)

                        nr = min(dist)
                        idx = dist.index(nr)

                        slice_output[i].append(photos[idx])
                        dist.clear()
                        rgb = avg_img_color(slices[i][j])
                        slice_output[i][j] = force_color(slice_output[i][j], rgb)

                ready_img = compose(self.grid, slice_output)
                ready_img.save('mosaic.jpg')
                return ready_img

        elif m == 3:
            for i in range(self.grid):
                for j in range(self.grid):

                    progress = int(((i * self.grid + j + 1)/ self.grid ** 2) * 100)
                    pbar.setProperty("value", progress)

                    if len(temp_photos) == 1:
                        slice_output[i].append(temp_photos[0])
                        temp_photos.clear()
                        temp_photos = grab_photo(self.path)
                    else:
                        rand = randrange(len(temp_photos))

                    slice_output[i].append(temp_photos[rand])
                    rgb = avg_img_color(slices[i][j])
                    slice_output[i][j] = force_color(slice_output[i][j], rgb)

                    del temp_photos[rand]
            
            image = compose(self.grid, slice_output)
            image.save('mosaic.jpg')
            return image