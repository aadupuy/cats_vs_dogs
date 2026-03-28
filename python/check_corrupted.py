from pathlib import Path
from PIL import Image

data_dir = Path("./PetImages")

bad_files = []

for class_dir in ["Cat", "Dog"]:
    folder = data_dir / class_dir
    for img_path in folder.iterdir():
        try:
            with Image.open(img_path) as img:
                img.verify()
        except Exception:
            bad_files.append(img_path)

print(f"Found {len(bad_files)} corrupted files")

for path in bad_files:
    path.unlink()

print("Corrupted files removed")