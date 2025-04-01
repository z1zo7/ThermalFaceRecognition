# import customtkinter as ctk
from tkinter import *
from tkinter import filedialog
from tkinter import messagebox    
import os
from datetime import datetime
from PIL import ImageTk, Image
import shutil
import pyodbc                                           # pip install tinter Pillow pyodbc
import io  # For converting byte array to image data


#-------- Globals --------
global BG , FC, Button_mode, imagePath, Button_help
BG = "#26242f"
FC = "#f0f0f0"
Button_mode = True
Button_help = True
imagePath = " "


def copy_image(image_filename, destination_path):
  # Check if the image file exists in the current directory
  if not os.path.isfile(image_filename):
    raise ValueError(f"Image file '{image_filename}' not found in the current directory.")

  # Get the full path of the image file (assuming it's in the current directory)
  image_path = os.path.join(os.getcwd(), image_filename)

  # Ensure the destination path exists (create it if necessary)
  os.makedirs(destination_path, exist_ok=True)  # Create directories if they don't exist

  # Copy the image using shutil.copy2 to preserve metadata (optional)
  try:
    shutil.copy2(image_path, destination_path)
    print(f"Image '{image_filename}' copied successfully to '{destination_path}'.")
  except OSError as e:
    raise OSError(f"Error copying image: {e}")

def delete_images(folder_path):

  # Supported image extensions (adjust if needed)
  image_extensions = [".jpg", ".jpeg", ".png", ".bmp", ".gif"]

  try:
    for filename in os.listdir(folder_path):
      # Check if it's a file and has a supported image extension
      if os.path.isfile(os.path.join(folder_path, filename)) and filename.lower().endswith(tuple(image_extensions)):
        os.remove(os.path.join(folder_path, filename))
        print(f"Deleted image: {filename}")
  except OSError as e:
    raise OSError(f"Error deleting images: {e}")