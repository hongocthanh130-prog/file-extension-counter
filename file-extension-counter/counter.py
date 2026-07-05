import os


def count_extensions(folder):
    result = {}
    for filename in os.listdir(folder):
        path = os.path.join(folder, filename)
        if os.path.isfile(path):
            ext = os.path.splitext(filename)[1].lower() or 'no_extension'
            result[ext] = result.get(ext, 0) + 1
    return result
