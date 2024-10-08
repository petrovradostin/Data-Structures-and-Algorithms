import os

def traverse_directories(path: str):
    files = []
    for item in os.listdir(path):
        item_path = os.path.join(path, item)
        if os.path.isdir(item_path):
            files.append(item)
            files.extend(traverse_directories(item_path))
        else:
            files.append(item)
    return files


def find_files(path: str, extension: str):
    files = []
    for item in os.listdir(path):
        item_path = os.path.join(path, item)
        if os.path.isdir(item_path):
            files.extend(find_files(item_path, extension))
        elif item.endswith("."+extension):
            files.append(item)
    return files


def file_exists(path: str, file_name: str):
    count = 0
    for item in os.listdir(path):
        item_path = os.path.join(path, item)
        if os.path.isdir(item_path):
            count += file_exists(item_path, file_name)
        elif item == file_name:
            count +=1
    if count:
        return True
    return False


def directory_stats(path, stats=None):
    if stats is None:
        stats = {}

    for item in os.listdir(path):
        item_path = os.path.join(path, item)
        if os.path.isfile(item_path):
            _, extension = os.path.splitext(item)
            stats[extension] = stats.get(extension, 0) + 1
        elif os.path.isdir(item_path):
            directory_stats(item_path, stats)

    return stats

