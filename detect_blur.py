from imutils import paths
import argparse
import cv2
import os
import glob
from PIL import Image
from resizeimage import resizeimage
from pathlib import Path

def variance_of_laplacian(image):
	return cv2.Laplacian(image, cv2.CV_64F).var()

ap = argparse.ArgumentParser()
ap.add_argument("-t", "--threshold", type=float, default=200.0,
	help="ustal prog ostrosci zdecia")
args = vars(ap.parse_args())

def detect_blur(dir1, dir2):

	data_dir0 = os.path.join(os.getcwd(), Path(__file__).parent)
	data_dir1 = os.path.join(data_dir0, 'fotg\*.jpg')
	data_dir2 = os.path.join(data_dir0, 'fotg_cut\*.jpg')
	data_dir3 = os.path.join(data_dir0, 'ready\ostre')
	data_dir4 = os.path.join(data_dir0, 'ready\\rozmazane')

	for imagePath in glob.glob(dir1):
		image = Image.open(imagePath)
		width, height = image.size
		left = (width/2)-200
		top = (height/2)-200
		right = (width/2)+200
		lower = (height/2)+200
		box=(left, top, right, lower)
		image = image.crop(box)
		s_dir = os.path.join(data_dir0, 'fotg_cut')
		s_dir1 = os.path.join(dir2, os.path.basename(imagePath))
		image.save(s_dir1)

	for imagePath in glob.glob(dir1):
		image = cv2.imread(imagePath)
		print(imagePath)
		image = image.astype('uint8')
		gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
		fm = variance_of_laplacian(gray)
		text = "Not Blurry"

		if fm < 200:
			text = "Blurry"
			os.chdir(data_dir4)
			filename = os.path.basename(imagePath)
			cv2.imwrite(filename, image)
		else:
			os.chdir(data_dir3)
			filename = os.path.basename(imagePath)
			cv2.imwrite(filename, image)