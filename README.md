# mosaic-app
Image processing desktop application providing 4 modes of mosaic making. Also has part providing sharp and blurry image bases for mosaic purposes. PyQt based GUI.

[![Generic badge](https://img.shields.io/badge/python-3.7.7-blue.svg)](https://shields.io/)   [![Generic badge](https://img.shields.io/badge/anaconda-2019.10-green.svg)](https://shields.io/)   [![Generic badge](https://img.shields.io/badge/Pillow-7.0.0-orange)](https://shields.io/)
[![License](http://img.shields.io/:license-mit-blue.svg?style=flat-square)](http://badges.mit-license.org)

## Parts of application

### Detect_blur
The part responsible for providing image base in working directory, decides if photos from certain location are blurry or not and splits them into two folders.

### PIX mode
Prepares a grid and fills every grid part with mean value of RGB of that area in original picture.

### RAW mode
This mode converts RGB to HSV color base and searches in chosen folder for picture that fits best for the grid element, and replaces that area of original picture with found picture.

### RAW+ mode
This mode works basically the same as the previous one, but also considers difference in H value between part of original image and the found one to match them.

### RAND+ mode
In this case program gets random image for every grid part and matches H value for grid part and inserted random picture.

## Using
To start application it is needed just to interpret main.py with Python interpreter.
In the right bottom you will find detect_blur button, which activates detect_blur method. The only thing that should be done is to choose folder which contains pictures that we want to include. Script automatically creates certain folders in working directory.
All other functionalities are enabled after setting image that we want to process and folder that contains images needed to prepare mosaic. Then there is a possibility to chose mode and grid size, and after clicking start scripts will make their work.

## Anaconda packages being used
* PyQt
* PIL
* opencv
* sys
* glob

## Credits
The project has been developed by:
- [Michał Kliczkowski](https://github.com/michal090497)
- [Marcin Ostrowski](https://github.com/ostrowskimarcin)

## License
 
The MIT License (MIT)

Copyright (c) 2020 Michał Kliczkowski, Marcin Ostrowski

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
