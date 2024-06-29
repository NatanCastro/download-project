import os
from downloader.config import IMAGE_FILE_EXTENSIONS, VIDEO_FILE_EXTENSIONS, BASE_DIR_PATH


def remove_query_params(url: str) -> str:
    return url.split('?')[0]


def create_save_directory(dir: str, sub_dir: str = None) -> str:
    dir_path = os.path.join(BASE_DIR_PATH, dir, sub_dir) if sub_dir else dir
    os.makedirs(dir_path, exist_ok=True)
    return dir_path


def get_file_extension(url: str) -> str:
    return os.path.splitext(url)[1].lower()


def get_file_type(file_extension: str) -> str:
    if file_extension in VIDEO_FILE_EXTENSIONS:
        return "video"
    elif file_extension in IMAGE_FILE_EXTENSIONS:
        return "image"
    else:
        return "other"


def get_sub_directory(file_extension: str) -> str:
    file_type = get_file_type(file_extension)

    match file_type:
        case "video":
            return "videos"
        case "image":
            return "images"
        case _:
            return "others"
