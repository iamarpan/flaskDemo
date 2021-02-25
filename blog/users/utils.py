import os
import secrets
from PIL import Image
from flask import current_app

def save_pic(form_picture):
    _, f_ext = os.path.splitext(form_picture.filename)
    file_name = secrets.token_hex(8) + f_ext
    picture_path = os.path.join(current_app.root_path, 'static/profile_pic', file_name)
    size = (125,125)
    i = Image.open(form_picture)
    form_picture = i.resize(size)

    form_picture.save(picture_path)
    return file_name