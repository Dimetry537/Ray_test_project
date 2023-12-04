import os
import shutil

from celery import Celery
from dotenv import load_dotenv


load_dotenv(".env")

celery = Celery(__name__)
celery.conf.broker_url = os.environ.get("CELERY_BROKER_URL")
celery.conf.result_backend = os.environ.get("CELERY_RESULT_BACKEND")

@celery.task
def say_hello():
    print("Celery & Redis работают нормально!")

say_hello.delay()

@celery.task 
def copy_photo(src, dst):
    filename = src.split('/')[-1]
    shutil.copy2(src, f'{dst}/{filename}')
    return f'Copied {src} to {dst}/{filename}'

@celery.task
def copy_all_photos(src_dir, dst_dir):
    for filename in os.listdir(src_dir):
        if filename.lower().endswith('.jpg'):
            src_file = f'{src_dir}/{filename}'  
            copy_photo.delay(src_file, dst_dir)
    return 'Copy operation initiated'
