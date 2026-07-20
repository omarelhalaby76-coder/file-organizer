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


def organize_files(current_folder, root_target_folder=None):
    # If no root target is set, assume the current folder is the root
    if root_target_folder is None:
        root_target_folder = current_folder

    for item in os.listdir(current_folder):
        item_path = os.path.join(current_folder, item)

        # Skip target organizational folders so we don't look inside them
        if (
            item in extensions.values()
            or item == "Others"
            or item.startswith(".")
        ):
            continue

        if os.path.isfile(item_path):
            filename, extension = os.path.splitext(item)
            
            # Fix case-sensitivity by lowering the extension string
            folder_name = extensions.get(extension.lower(), "Others")
            
            # Group everything relative to the main root folder
            folder_path = os.path.join(root_target_folder, folder_name)

            if not os.path.exists(folder_path):
                os.makedirs(folder_path)

            counter = 1
            new_name = item

            # Handle duplicate file names gracefully
            while os.path.exists(os.path.join(folder_path, new_name)):
                new_name = f"{filename} ({counter}){extension}"
                counter += 1

            shutil.move(item_path, os.path.join(folder_path, new_name))
            stats[folder_name] = stats.get(folder_name, 0) + 1
            print(f"Moved: {item} -> {folder_name}")

        elif os.path.isdir(item_path):
            # Pass the root target folder down so subfolder items move to the top-level categories
            organize_files(item_path, root_target_folder)


if __name__ == "__main__":
    if os.path.exists(path_to_folder):
        organize_files(path_to_folder)
        print("\nSummary")
        print("-" * 20)
        
        total = 0
        for category, count in stats.items():
            print(f"{category}: {count} files")
            total += count
        print("-" * 20)
        print(f"\nTotal files organized: {total}")
    else:
        print("The provided path does not exist.")
