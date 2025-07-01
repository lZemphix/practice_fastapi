from fastapi_storages import FileSystemStorage

def get_storage():
    return FileSystemStorage(path='src/static/images')