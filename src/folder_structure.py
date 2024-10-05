import os
import shutil
from datetime import datetime
from typing import Dict, List

class FolderStructure:
    def __init__(self, base_folder):
        self.base_folder = base_folder

    def create_directory(self, folder_path: str) -> None:
        """Creates a directory if it doesn't exist."""
        os.makedirs(folder_path, exist_ok=True)

    def get_file_creation_date(self, file_path: str) -> str:
        """Returns the creation date of a file as a string (YYYY-MM-DD)."""
        timestamp = os.path.getctime(file_path)
        return datetime.fromtimestamp(timestamp).strftime('%Y-%m-%d')

    def categorize_file(self, file_name: str) -> str:
        """Categorize the file based on its extension."""
        ext = os.path.splitext(file_name)[1].lower()
        if ext in ['.jpg', '.jpeg', '.png', '.gif']:
            return 'images'
        elif ext in ['.mp4', '.avi', '.mov', '.mkv']:
            return 'videos'
        elif ext in ['.txt', '.pdf', '.docx', '.xlsx']:
            return 'documents'
        else:
            return 'other'  # For files that don't fit predefined categories

    def resolve_duplicate_file(self, dest_path: str) -> str:
        """
        Resolves file name conflicts by appending a numeric suffix to the file name.
        
        :param dest_path: Destination path where the file would be moved.
        :return: New destination path with a unique file name if necessary.
        """
        if not os.path.exists(dest_path):
            return dest_path

        base, ext = os.path.splitext(dest_path)
        counter = 1

        while os.path.exists(dest_path):
            dest_path = f"{base} ({counter}){ext}"
            counter += 1

        return dest_path

    def organize_files(self, sorted_files: Dict[str, Dict[str, List[str]]], start_date=None, end_date=None) -> bool:
        """
        Organizes files into folders based on the sorted file dictionary.
        
        :param sorted_files: Dictionary of sorted files with structure {category: {date: [files]}}
        :param start_date: Optional start date for filtering files
        :param end_date: Optional end date for filtering files
        :return: True if organization is successful
        """
        for category, dates in sorted_files.items():
            for date, files in dates.items():
                # Filter by start and end date if provided
                if start_date and date < start_date:
                    continue
                if end_date and date > end_date:
                    continue

                for file in files:
                    file_folder, file_name = os.path.split(file)
                    relative_folder = os.path.relpath(file_folder, self.base_folder)
                    dest_folder = os.path.join(self.base_folder, category, date, relative_folder)
                    
                    self.create_directory(dest_folder)
                    
                    dest_path = os.path.join(dest_folder, file_name)
                    dest_path = self.resolve_duplicate_file(dest_path)
                    
                    shutil.move(file, dest_path)
        return True

    def organize_files_by_date(self, start_date: str = None, end_date: str = None) -> bool:
        """
        Organizes files into folders by their creation date, optionally filtering by start and end date.
        
        :param start_date: Filter files created after this date (YYYY-MM-DD)
        :param end_date: Filter files created before this date (YYYY-MM-DD)
        :return: True if organization is successful
        """
        for root, dirs, files in os.walk(self.base_folder):
            for file_name in files:
                file_path = os.path.join(root, file_name)

                # Skip hidden files
                if file_name.startswith('.'):
                    continue

                if os.path.isfile(file_path):
                    creation_date = self.get_file_creation_date(file_path)

                    # Apply date filtering if specified
                    if start_date and creation_date < start_date:
                        continue
                    if end_date and creation_date > end_date:
                        continue

                    # Preserve relative folder structure in the target directory
                    relative_folder = os.path.relpath(root, self.base_folder)
                    date_folder = os.path.join(self.base_folder, creation_date, relative_folder)
                    self.create_directory(date_folder)
                    
                    dest_path = os.path.join(date_folder, file_name)
                    dest_path = self.resolve_duplicate_file(dest_path)
                    
                    shutil.move(file_path, dest_path)

        return True

    def remove_empty_folders(self) -> None:
        """
        Recursively removes empty directories in the base folder.
        """
        for root, dirs, _ in os.walk(self.base_folder, topdown=False):
            for dir_name in dirs:
                dir_path = os.path.join(root, dir_name)
                if not os.listdir(dir_path):
                    os.rmdir(dir_path)
