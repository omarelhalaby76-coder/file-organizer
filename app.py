import os
import shutil

stats = {}

extensions = {
    '.jpg': 'Images',
    '.jpeg': 'Images',
    '.png': 'Images',
    '.pdf': 'Documents',
    '.txt': 'Documents',
    '.mp3': 'Audio/Music',
    '.mp4': 'Videos',
    '.py': 'Python Files'
}

path_to_folder = input("Path to folder: ")


def organize_files(path_to_folder):

    for item in os.listdir(path_to_folder):

        item_path = os.path.join(path_to_folder, item)

        if (
            os.path.basename(item_path) in extensions.values()
            or os.path.basename(item_path) == "Others"
            or os.path.basename(item_path).startswith(".")
        ):
            continue

        if os.path.isfile(item_path):

            filename, extension = os.path.splitext(item)
            folder_name = extensions.get(extension, "Others")
            folder_path = os.path.join(path_to_folder, folder_name)
            
            if os.path.basename('folder_path') == folder_name:
                continue

            if not os.path.exists(folder_path):
                os.makedirs(folder_path)

            counter = 1
            new_name = item

            while os.path.exists(os.path.join(folder_path, new_name)):
                new_name = f"{filename} ({counter}){extension}"
                counter += 1

            shutil.move(item_path, os.path.join(folder_path, new_name))
            stats[folder_name] = stats.get(folder_name, 0) + 1
            print(f"Moved: {item} -> {folder_name}")

        elif os.path.isdir(item_path):

            organize_files(item_path)


if __name__ == "__main__":
    organize_files(path_to_folder)
    print("\nSummary")
    print("-" * 20)
    
    total = 0
    
    for category, count in stats.items():
        print(f"{category}: {count} files")
        total += count
    print("-" * 20)
    print(f"\nTotal files organized: {total}")