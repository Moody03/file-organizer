import logging
import os
from datetime import datetime

def setup_logger():
    """Sets up a logger for the file organizer with a stream handler."""
    logger = logging.getLogger('file_organizer')
    logger.setLevel(logging.INFO)
    
    if not logger.handlers:  # Avoid duplicate handlers
        handler = logging.StreamHandler()
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        handler.setFormatter(formatter)
        logger.addHandler(handler)
    
    return logger

def handle_error(logger, error_message):
    """Logs error messages using the provided logger."""
    logger.error(f"An error occurred: {error_message}")

def parse_date(date_string):
    """Parses a string into a date object in the format YYYY-MM-DD."""
    try:
        return datetime.strptime(date_string, '%Y-%m-%d').date()
    except ValueError:
        raise ValueError(f"Invalid date format. Please use YYYY-MM-DD.")

def validate_file_path(file_path):
    """Validates if the provided file path exists and is a file."""
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"The file path '{file_path}' does not exist.")
    if not os.path.isfile(file_path):
        raise ValueError(f"The path '{file_path}' is not a valid file.")

def get_file_size(file_path):
    """Returns the file size in bytes."""
    try:
        validate_file_path(file_path)
        return os.path.getsize(file_path)
    except Exception as e:
        raise IOError(f"Unable to retrieve the file size: {e}")

def is_valid_file_type(file_name, allowed_extensions):
    """
    Checks if the file extension is in the list of allowed extensions.
    
    Args:
    file_name (str): The name of the file (with extension).
    allowed_extensions (list): A list of allowed file extensions (e.g. ['jpg', 'pdf', 'txt']).
    
    Returns:
    bool: True if the file has a valid extension, False otherwise.
    """
    file_extension = os.path.splitext(file_name)[1][1:].lower()  # Get extension without the dot
    return file_extension in allowed_extensions

# Example logger usage
"""if __name__ == "__main__":
    logger = setup_logger()
    try:
        # Example usage of utility functions
        date = parse_date("2024-10-01")
        logger.info(f"Parsed date: {date}")
        
        file_path = "/path/to/file.txt"
        validate_file_path(file_path)
        logger.info(f"File size: {get_file_size(file_path)} bytes")
        
        allowed_extensions = ['txt', 'pdf']
        if is_valid_file_type(file_path, allowed_extensions):
            logger.info(f"File '{file_path}' is a valid file type.")
        else:
            logger.warning(f"File '{file_path}' is not an allowed file type.")
    except Exception as e:
        handle_error(logger, str(e))
"""