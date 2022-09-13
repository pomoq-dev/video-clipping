from PIL import Image
import pyheif


def crop_by(ratio, img_path):
    img = Image.open(img_path)
    indent = ratio * img.width
    box = (math.floor(indent), math.floor(indent), math.floor(img.width - indent), math.floor(img.height - indent))
    img2 = img.crop(box)
    return img2


def heic_2_png(image_path):
    new_name = image_path.replace('heic', 'png')
    heif_file = pyheif.read(image_path)
    data = Image.frombytes(
        heif_file.mode,
        heif_file.size,
        heif_file.data,
        "raw",
        heif_file.mode,
        heif_file.stride,
    )
    data.save(new_name, "PNG")
