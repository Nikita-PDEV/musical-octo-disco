import os
from django.conf import settings
from django.core.files.storage import FileSystemStorage

def get_path_upload_photos(photo_file):
    """
    Функция для обработки загружаемого фото и сохранения его в нужную папку.
    Возвращает путь к загруженному файлу.
    """
    # Определяем путь для сохранения загруженных фотографий
    upload_path = os.path.join(settings.MEDIA_ROOT, 'photos/')
    
    # Создаем папку, если она не существует
    if not os.path.exists(upload_path):
        os.makedirs(upload_path)

    # Создаем экземпляр FileSystemStorage
    fs = FileSystemStorage(location=upload_path)

    # Сохраняем файл и возвращаем путь
    filename = fs.save(photo_file.name, photo_file)
    return fs.url(filename)