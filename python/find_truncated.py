from pathlib import Path
from PIL import Image, ImageFile
import warnings

ImageFile.LOAD_TRUNCATED_IMAGES = False  # stricter check

data_dir = Path("./PetImages")
bad_files = []

for class_dir in ["Cat", "Dog"]:
    folder = data_dir / class_dir
    for img_path in folder.iterdir():
        try:
            with warnings.catch_warnings():
                warnings.simplefilter("error")
                with Image.open(img_path) as img:
                    img.load()   # full decode
        except Exception as e:
            bad_files.append((img_path, repr(e)))

print(f"Found {len(bad_files)} problematic files")
for path, err in bad_files[:20]:
    print(path, err)