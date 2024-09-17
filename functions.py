import os
from flask import abort
from werkzeug.utils import secure_filename
from functools import wraps
from flask_login import current_user

UPLOAD_EXTENSIONS = ['.jpg', '.png', '.gif', '.jpeg']
UPLOAD_PATH = 'static/uploads/'

def save_pics(pics):
    filename_list = list()
    for pic in pics:
            print(pic.filename)
            filename = secure_filename(pic.filename)
            if filename != '':
                file_ext = os.path.splitext(filename)[1]
                if file_ext not in UPLOAD_EXTENSIONS:
                    abort(400)
                pic.save(os.path.join(UPLOAD_PATH, filename))
                filename_list.append(os.path.join(UPLOAD_PATH, filename))
    return filename_list
# Create an admin-only decorator
def admin_only(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        # If id is not 1 then return abort with 403 error
        if current_user.id != 1:
            return abort(403)
        # Otherwise continue with the route function
        return f(*args, **kwargs)

    return decorated_function