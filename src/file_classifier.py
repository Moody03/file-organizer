import os
from typing import Dict, List, Union, Any

class FileClassifier:
    def __init__(self):
        # Predefined categories with common files extensions
       self.file_types = {
            'images': ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff'],
            'videos': ['.mp4', '.avi', '.mkv', '.mov', '.wmv'],
            'documents': ['.txt', '.doc', '.docx', '.pdf'],
            'audio': ['.mp3', '.wav', '.aac', '.flac'],
            'archives': ['.zip', '.rar', '.tar', '.gz'],
            'scripts': ['.py', '.js', '.html', '.css'],
            'others': []
        }
       
       
    def classify_files(self, files: List[str]) -> Dict[str, List[str]]:
        """Classify a list of files into categories."""
        classified_files = {category: [] for category in self.file_types.keys()}
        for file in files:
            category = self.categorize_by_extension(file)
            classified_files[category].append(file)
        return classified_files   
       
       
    def categorize_by_extension(self, file_name):
        """Categorizes a file based on its extension"""
        file_ext = os.path.splitext(file_name)[1].lower() # Get the file extension
        
        for category, extenstions in self.file_types.items():
            if file_ext in extenstions:
                return category
        
        # If no category is found, return 'others'
        return 'others'
    
    
    def extend_with_ai(self, file_name):
        """Future extension method for AI-based classification"""
        # This can be extended with a model that classifies files based on content
        raise NotImplementedError("AI-based classification is not implemented yet.")        