import os
from datetime import datetime

from django.utils.deconstruct import deconstructible

@deconstructible
class PathAndRenamer(object):
    def __init__(self, sub_path):
        self.sub_path = sub_path

    def __call__(self, instance, filename):
        ext = filename.split('.')[-1]
        filename = filename.split('.')[0]
        today = datetime.now().strftime('%Y-%m-%d')
        filename = f"{filename}_{today}.{ext}"
        return os.path.join(self.sub_path, filename)