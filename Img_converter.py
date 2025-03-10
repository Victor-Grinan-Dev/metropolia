from PIL import Image
from pathlib import Path

def convert_img(folder_path, quality=75, from_ext="png", to_ext="webp"):
    folder = Path(folder_path)
    for file in folder.glob("*." + from_ext):
        img = Image.open(file).convert("RGB")
        new_file = file.with_suffix("." + to_ext)
        img.save(new_file, to_ext, quality=quality)
        print(f"Converted: {file.name} → {new_file.name} ({quality}% quality)")

convert_img(r"F:\coding\projects_REACT\bandida\src\assets\images\pmu")