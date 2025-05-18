import os
from PIL import Image

def process_image(path, TARGET_WIDTH, TARGET_HEIGHT):
    print(path)
    try:
        with Image.open(path) as img:
            img = img.convert("RGB")
            img = img.resize((TARGET_WIDTH, TARGET_HEIGHT), Image.LANCZOS)
            img.save(path, format="JPEG", quality=95)
    except Exception as e:
        print(f"Failed to process {path}: {e}")

def resize():
    directories = [
        r"E:\plant_images",
        r"E:\plant_images_not",
        r"E:\plant_images_not2",
    ]

    # Desired size
    TARGET_WIDTH = 640
    TARGET_HEIGHT = 480
    for dir_path in directories:
        if not os.path.isdir(dir_path):
            print(f"Directory not found, skipping: {dir_path}")
            continue
        for root, _, files in os.walk(dir_path):
            for fname in files:
                if fname.lower().endswith((".png", ".jpg", ".jpeg")):
                    full_path = os.path.join(root, fname)
                    new_path = os.path.splitext(full_path)[0] + ".jpg"
                    process_image(full_path, TARGET_WIDTH, TARGET_HEIGHT)
                    if new_path != full_path:
                        os.replace(full_path, new_path)


