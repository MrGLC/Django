import os
import shutil
import pathlib
import argparse

def create_new_folder(folder_name):
    """Creates a new folder in the Documents directory with the given name"""
    documents_dir = pathlib.Path.home() / "Documents"
    new_folder = documents_dir / folder_name
    new_folder.mkdir(exist_ok=True)
    return new_folder

def get_files_with_keyword(directory, keyword):
    """Returns a list of files in the given directory that contain the keyword in their name"""
    files_with_keyword = []
    for file in os.listdir(directory):
        if keyword in file:
            files_with_keyword.append(file)
    return files_with_keyword

def move_files(files_to_move, source_dir, dest_dir, folder_by_extension=False):
    """Moves the given files from the source directory to the destination directory, optionally moving files into folders by extension"""
    for file in files_to_move:
        src_path = os.path.join(source_dir, file)
        if folder_by_extension:
            dest_extension_folder = dest_dir / os.path.splitext(file)[1][1:]
            if not dest_extension_folder.exists():
                dest_extension_folder.mkdir(exist_ok=True)
            dst_path = os.path.join(dest_extension_folder, file)
        else:
            dst_path = os.path.join(dest_dir, file)
        shutil.move(src_path, dst_path)

def create_extension_folders(files_to_move, dest_dir):
    """Creates subfolders in the destination directory based on the extensions of the files"""
    extensions = set()
    for file in files_to_move:
        _, ext = os.path.splitext(file)
        extensions.add(ext[1:])  # remove the dot from the extension
    created_folders = 0
    for ext in extensions:
        ext_folder = dest_dir / ext
        if not ext_folder.exists():
            ext_folder.mkdir(exist_ok=True)
            created_folders += 1
    print(f"Created {created_folders} folders.")

def organize_downloads(keyword):
    """Main function that scans the downloads folder, moves files with the keyword, and creates a new folder"""
    downloads_dir = pathlib.Path.home() / "Downloads"
    new_folder_name = "Kitten Files"

    files_with_keyword = get_files_with_keyword(downloads_dir, keyword)
    if not files_with_keyword:
        print("No files found with the keyword.")
        return

    new_folder = create_new_folder(new_folder_name)
    create_extension_folders(files_with_keyword, new_folder)
    move_files(files_with_keyword, downloads_dir, new_folder, folder_by_extension=True)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Organize files in the downloads folder')
    parser.add_argument('keyword', type=str, help='Keyword to search for in file names')
    args = parser.parse_args()

    organize_downloads(args.keyword)
