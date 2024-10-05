import unittest
import os
import shutil
import sys

# Add the parent directory of 'src' to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.file_classifier import FileClassifier

class TestFileClassifier(unittest.TestCase):

    def setUp(self):
        """Set up a temporary folder and sample files for testing."""
        self.test_folder = "data/sample_files"
        os.makedirs(self.test_folder, exist_ok=True)

        # Create sample files
        self.sample_files = {
            "image1.jpg": "This is a sample image file",
            "image2.png": "Another sample image file",
            "video1.mp4": "Sample video file",
            "doc1.pdf": "Sample document file",
            "doc2.txt": "Another sample document",
            "audio1.mp3": "Sample audio file",
            "archive1.zip": "Sample archive file",
            "script1.py": "Sample Python script",
            "unknown_file.xyz": "Unknown file type"
        }

        for file_name, content in self.sample_files.items():
            with open(os.path.join(self.test_folder, file_name), 'w') as f:
                f.write(content)

        self.classifier = FileClassifier()

    def tearDown(self):
        """Remove the test folder and its contents after tests."""
        shutil.rmtree(self.test_folder)

    def test_categorize_by_extension(self):
        """Test that categorize_by_extension works as expected for different files."""
        self.assertEqual(self.classifier.categorize_by_extension("image1.jpg"), "images")
        self.assertEqual(self.classifier.categorize_by_extension("video1.mp4"), "videos")
        self.assertEqual(self.classifier.categorize_by_extension("doc1.pdf"), "documents")
        self.assertEqual(self.classifier.categorize_by_extension("audio1.mp3"), "audio")
        self.assertEqual(self.classifier.categorize_by_extension("archive1.zip"), "archives")
        self.assertEqual(self.classifier.categorize_by_extension("script1.py"), "scripts")
        self.assertEqual(self.classifier.categorize_by_extension("unknown_file.xyz"), "others")

    def test_classify_files(self):
        """Test that classify_files categorizes all files correctly."""
        # List of test files in the folder
        test_files = list(self.sample_files.keys())
        
        # Classify the test files
        classified_files = self.classifier.classify_files(test_files)

        self.assertIn("image1.jpg", classified_files['images'])
        self.assertIn("image2.png", classified_files['images'])
        self.assertIn("video1.mp4", classified_files['videos'])
        self.assertIn("doc1.pdf", classified_files['documents'])
        self.assertIn("doc2.txt", classified_files['documents'])
        self.assertIn("audio1.mp3", classified_files['audio'])
        self.assertIn("archive1.zip", classified_files['archives'])
        self.assertIn("script1.py", classified_files['scripts'])
        self.assertIn("unknown_file.xyz", classified_files['others'])

if __name__ == "__main__":
    unittest.main()
