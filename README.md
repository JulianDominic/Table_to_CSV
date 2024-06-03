# Table to CSV

The program takes in a picture of table and it outputs the table's contents into a `.csv` file.

## Technologies Used

1. Python
2. [Pillow](https://pypi.org/project/pillow/) & [Pillow-HEIF](https://pypi.org/project/pillow-heif/)
3. [OpenCV](https://pypi.org/project/opencv-python/)
4. [Tesseract](https://github.com/tesseract-ocr/tesseract) ([PyTesseract](https://pypi.org/project/pytesseract/))
5. Some frontend library/framework (If web, probably React+MUI. If desktop, probably PyQt or Electron?)

> Note: I originally wanted this to be a Windows-only project but the installation of Tesseract from UB-Mannheim will take at least 30min for a 40mb file... Therefore, I am using WSL instead which also works better because npm is already setup in WSL for me.

## Expected Workflow

![Expected Workflow for Image Processing](assets/Image_Processing_Workflow.png)

## Background

My friend was studying from a Chemistry textbook that emphasised the use of Excel to do data manipulation.
Since it was a physical textbook, he has to type out the data by hand which is very time consuming.

The current solutions such as ExtractTable and Nanonets don't work well for him.
Therefore, I took it upon myself to create a program to do it and to teach myself the technologies involved to make this work.

## How I learnt

I searched on YouTube on how to do OCR and I found this [playlist](https://www.youtube.com/playlist?list=PL2VXyKi-KpYuTAZz__9KVl1jQz74bDG7i).
