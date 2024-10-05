import os
from datetime import datetime


from file_classifier import FileClassifier

class FileManager:
    def __init__(self, folder_path):
        self.folder_path = folder_path
        self.file_classifier = FileClassifier()

    def scan_folder(self) -> list:
        """
        Recursively scan the folder and return a list of all files, including in subdirectories.
        
        :return: List of file paths
        """
        if not os.path.isdir(self.folder_path):
            raise ValueError(f"{self.folder_path} is not a valid directory.")
        
        file_list = []
        for root, _, files in os.walk(self.folder_path):
            for file in files:
                file_list.append(os.path.join(root, file))
        return file_list

    def get_file_metadata(self, file_name: str) -> dict:
        """
        Retrieve metadata of a specific file.
        
        :param file_name: Name or path of the file
        :return: Dictionary with file metadata
        """
        file_path = os.path.join(self.folder_path, file_name)
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"{file_name} does not exist in {self.folder_path}")
        
        # Retrieve metadata
        file_stats = os.stat(file_path)
        metadata = {
            'name': file_name,
            'type': os.path.splitext(file_name)[1],
            'size': file_stats.st_size,  # Size in bytes
            'created': datetime.fromtimestamp(file_stats.st_ctime),  # Creation time
            'modified': datetime.fromtimestamp(file_stats.st_mtime),  # Last modified time
        }
        return metadata

    def read_file(self, file_name: str) -> str:
        """
        Read and return the contents of a file.
        
        :param file_name: File name or path of the file to be read
        :return: Contents of the file as a string
        """
        file_path = os.path.join(self.folder_path, file_name)
        if not os.path.isfile(file_path):
            raise FileNotFoundError(f"{file_name} does not exist in {self.folder_path}")
        
        with open(file_path, 'r') as file:
            return file.read()

    def write_file(self, file_name: str, content: str) -> None:
        """
        Write content to a file. If the file exists, it will be overwritten.
        
        :param file_name: File name or path where the content will be written
        :param content: Content to write into the file
        """
        file_path = os.path.join(self.folder_path, file_name)
        
        # Create directory if it doesn't exist
        file_dir = os.path.dirname(file_path)
        if not os.path.exists(file_dir):
            os.makedirs(file_dir, exist_ok=True)
        
        with open(file_path, 'w') as file:
            file.write(content)

    def delete_file(self, file_name: str) -> None:
        """
        Deletes a specific file.
        
        :param file_name: Name or path of the file to delete
        """
        file_path = os.path.join(self.folder_path, file_name)
        if not os.path.isfile(file_path):
            raise FileNotFoundError(f"{file_name} does not exist in {self.folder_path}")
        
        os.remove(file_path)
