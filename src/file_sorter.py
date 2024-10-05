import os
import shutil
from datetime import datetime
import sys
from typing import Dict, List


# Add the parent directory of 'src' to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.file_classifier import FileClassifier



class FileSorter:
    def __init__(self):
        self.classifier = FileClassifier()  # Use the classifier to determine file types

    def sort_files(self, categorized_files: Dict[str, List[str]], base_folder: str) -> Dict[str, Dict[str, List[str]]]:
        """
        Sorts files into appropriate folders based on type and creation/modification dates.
        
        :param categorized_files: Dictionary of categorized files
        :param base_folder: Base folder path
        :return: Dictionary of sorted files with structure {category: {date: [files]}}
        """
        sorted_files = {}
        for category, files in categorized_files.items():
            sorted_files[category] = {}
            for file in files:
                file_path = os.path.join(base_folder, file)
                creation_date = self.get_file_creation_date(file_path)
                if creation_date not in sorted_files[category]:
                    sorted_files[category][creation_date] = []
                sorted_files[category][creation_date].append(file)
        return sorted_files
    
    @staticmethod
    def get_file_creation_date(file_path: str) -> str:
        """Returns the creation date of a file as a string (YYYY-MM-DD)."""
        timestamp = os.path.getctime(file_path)
        return datetime.fromtimestamp(timestamp).strftime('%Y-%m-%d')



