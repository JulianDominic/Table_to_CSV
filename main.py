import cv2
import PIL
from PIL import Image
from pillow_heif import register_heif_opener
import pytesseract
import os,sys
from pathlib import Path

def open_image(image_path:str):
    Image.open(image_path)

def main():
    IMAGE_EXTENSIONS = (".png", ".jpg", ".jpeg", ".heif", ".heic")
    current_dir = Path(".")
    data_dir = current_dir / "data"
    data_files = filter(lambda file: file.endswith(IMAGE_EXTENSIONS), os.listdir(data_dir))
    temp_dir = current_dir / "temp"

    for data_file in data_files:
        file_name, file_ext = data_file.split(".")
        filepath = data_dir / data_file
        
        if file_ext.lower().endswith((".heif", ".heic")):
            register_heif_opener()

        try:
            new_format = False
            im = Image.open(filepath)
            save_format = "jpeg" if new_format else file_ext
            filepath = file_name + '.' + save_format
            im.save(temp_dir / filepath, save_format)
        except (FileNotFoundError, PIL.UnidentifiedImageError, ValueError, TypeError) as error:
            error_name = type(error).__name__
            if error_name == "FileNotFoundError":
                print("File cannot be found. Check path.")
            elif error_name == "PIL.UnidentifiedImageError":
                print("Image cannot be opened and identified. Try using a different format.")
            elif error_name == "ValueError":
                print("Ensure that the mode argument is 'r', and don't use a StringIO instance as the filepath.")
            elif error_name == "TypeError":
                print("The formats argument can only be None, a list, or a tuple.")

        

if __name__ == "__main__":
    main()
