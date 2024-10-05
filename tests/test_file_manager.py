import unittest
import os
import sys
import shutil
from datetime import datetime

# Add the parent directory of 'src' to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.file_manager import FileManager


class TestFileManager(unittest.TestCase):
    
    def setUp(self):
        """Set up a temporary folder and files for testing."""
        self.test_folder = "data/sample_files"
        os.makedirs(self.test_folder, exist_ok=True)
        self.test_file1 = os.path.join(self.test_folder, "test1.txt")
        self.test_file2 = os.path.join(self.test_folder, "test2.txt")
        
        # Create test files
        with open(self.test_file1, 'w') as f:
            f.write("This is a test file1.")
        
        with open(self.test_file2, 'w') as f:
            f.write("This is a test file2.")
            
        # Create FileManager instance
        self.file_manager = FileManager(self.test_folder)
        
    def tearDown(self):
        """Remove the temporary test folder and its contents."""
        shutil.rmtree(self.test_folder) 
        
    def test_scan_folder(self):
        """Test that scan_folder correctly lists all files."""
        files = self.file_manager.scan_folder()
        self.assertIn(self.test_file1, files)
        self.assertIn(self.test_file2, files)
        
    def test_get_file_metadata(self):
        """Test that get_file_metadata correctly retrieves file metadata."""
        metadata = self.file_manager.get_file_metadata("test1.txt")
        self.assertEqual(metadata['name'], "test1.txt")
        self.assertEqual(metadata['type'], ".txt")
        self.assertTrue(metadata['size'] > 0)
        self.assertIsInstance(metadata['created'], datetime)
        self.assertIsInstance(metadata['modified'], datetime)
        
    def test_file_not_found(self):
        """Test that get_file_metadata raises an error for non-existent files."""
        with self.assertRaises(FileNotFoundError):
            self.file_manager.get_file_metadata("non_existent_file.txt")
            
    def test_read_file(self):
        """Test that read_file correctly reads the content of a file."""
        content = self.file_manager.read_file("test1.txt")
        self.assertEqual(content, "This is a test file1.")
        
    def test_write_file(self):
        """Test that write_file creates a new file or overwrites an existing one."""
        new_file = "test3.txt"
        self.file_manager.write_file(new_file, "This is a new test file.")
        
        # Check if the file was created and its content
        self.assertTrue(os.path.isfile(os.path.join(self.test_folder, new_file)))
        content = self.file_manager.read_file(new_file)
        self.assertEqual(content, "This is a new test file.")
        
        # Test overwriting the file
        self.file_manager.write_file(new_file, "This file has been overwritten.")
        content = self.file_manager.read_file(new_file)
        self.assertEqual(content, "This file has been overwritten.")

    def test_delete_file(self):
        """Test that delete_file correctly removes a file."""
        self.file_manager.delete_file("test1.txt")
        self.assertFalse(os.path.isfile(self.test_file1))  # test1.txt should be deleted

        # Test deleting a non-existent file
        with self.assertRaises(FileNotFoundError):
            self.file_manager.delete_file("non_existent_file.txt")


if __name__ == "__main__":
    unittest.main()
