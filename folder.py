import os

IMAGE_EXTENSION = (".jpg", "jpeg", ".png", ".jpeg", ".gif", ".bmp", ".tiff", ".webp")

def format_size(bytes_size):
    for unit in ['B', 'KB', 'MB', 'GB', 'TB']:
        if bytes_size < 1024:
            return f"{bytes_size:.2f} {unit}"
        bytes_size /= 1024

def count_images(folder_path):
    total_count = 0
    total_size = 0
    for root, dirs, files in os.walk(folder_path):
        for f in files:
            if f.lower().endswith(IMAGE_EXTENSION):
                total_count += 1
                full_path = os.path.join(root, f)
                total_size += os.path.getsize(full_path)

    return {
        "Total Pictures": total_count,
        "Total Image Size": format_size(total_size)
    }

counted_images_size = count_images("/home/minhaj/Desktop")


print(counted_images_size)
