import os
from PIL import Image
from flask import current_app


def product_pic(pic_upload, name):

    filename = pic_upload.filename
    ext_type = filename.split('.')[-1]
    storage_filename = str(name) + '.' + ext_type
    filepath = os.path.join(current_app.root_path, 'static\sitepics\pands_pics', storage_filename)
    output_size = (300, 300)

    pic = Image.open(pic_upload)
    pic.thumbnail(output_size)
    pic.save(filepath)

    return storage_filename
