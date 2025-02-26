import os

defaultDir = os.getenv("windir")

def get_folder_size(folder):
    total_size = 0
    for dirpath, _, filenames in os.walk(folder):
        for f in filenames:
            fp = os.path.join(dirpath, f)
            if os.path.exists(fp):
                total_size += os.path.getsize(fp)
    return total_size

def scan_and_sort_folders(folder = defaultDir):
    current_dir = folder
    folder_sizes = []

    for item in os.listdir(current_dir):
        item_path = os.path.join(current_dir, item)
        if os.path.isdir(item_path):
            size = get_folder_size(item_path)
            folder_sizes.append((item, size))

    folder_sizes.sort(key=lambda x: x[1], reverse=True)

    print("\nCarpetas ordenadas por tamaño (de mayor a menor):\n")
    for folder, size in folder_sizes:
        print(f"{folder}: {size / (1024 * 1024):.2f} MB")

