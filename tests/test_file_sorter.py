import unittest
import os
import shutil
import sys
from datetime import datetime

# Add the parent directory of 'src' to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.file_sorter import FileSorter

class TestFileSorter(unittest.TestCase):

    def setUp(self):
        """Set up a temporary folder and sample files for testing."""
        self.test_folder = "data/sample_data"
        os.makedirs(self.test_folder, exist_ok=True)

        # Create sample files
        self.sample_files = {
            "image1.jpg": "This is a sample image file",
            "video1.mp4": "Sample video file",
            "doc1.pdf": "Sample document file",
            "audio1.mp3": "Sample audio file",
        }

        for file_name, content in self.sample_files.items():
            with open(os.path.join(self.test_folder, file_name), 'w') as f:
                f.write(content)

        self.sorter = FileSorter()

    def tearDown(self):
        """Remove the test folder and its contents after tests."""
        shutil.rmtree(self.test_folder)

    def test_sort_files(self):
        """Test that files are sorted into type and date folders correctly."""
        # Create a dictionary to simulate categorized files
        categorized_files = { 
            "images": ["image1.jpg"],
            "videos": ["video1.mp4"],
            "documents": ["doc1.pdf"],
            "audios": ["audio1.mp3"]
        }

        # Sort the files
        sorted_files = self.sorter.sort_files(categorized_files, self.test_folder)

        # Check if files have been moved into the correct folders
        for file_name in self.sample_files.keys():
            # Determine the file type based on its extension
            file_type = self.sorter.classifier.categorize_by_extension(file_name)
            
            # Get the creation date for the file
            creation_date = self.sorter.get_file_creation_date(os.path.join(self.test_folder, file_name))

            # Define the expected new folder path based on the type and creation date
            expected_folder = os.path.join(self.test_folder, file_type, creation_date)
            expected_file_path = os.path.join(expected_folder, file_name)

            # Now check if the destination folder exists
            self.assertTrue(os.path.exists(expected_folder), f"Folder {expected_folder} should exist.")
    
            # Check if the file exists in the expected path
            self.assertTrue(os.path.exists(expected_file_path), f"File {file_name} should be in {expected_folder}.")

    def test_get_file_creation_date(self):
        """Test that the creation date is correctly retrieved."""
        file_name = "image1.jpg"
        file_path = os.path.join(self.test_folder, file_name)
        creation_date = self.sorter.get_file_creation_date(file_path)
        
        # Check if the returned creation date is in the correct format
        self.assertEqual(creation_date, datetime.fromtimestamp(os.path.getctime(file_path)).strftime('%Y-%m-%d'))

if __name__ == "__main__":
    unittest.main()
