import os
import shutil

source_folder = "images_folder"
destination_folder = "jpg_files"

if not os.path.exists(destination_folder):
    os.makedirs(destination_folder)

for filename in os.listdir(source_folder):
    if filename.endswith(".jpg"):
        source_path = os.path.join(source_folder, filename)
        destination_path = os.path.join(destination_folder, filename)
        shutil.move(source_path, destination_path)
        print(f"Moved: {filename}")

print("All .jpg files moved.")
