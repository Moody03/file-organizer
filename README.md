
# File Organizer

**File Organizer** is a Python-based application that helps you organize files in a folder by file type or modification date. You can also filter files by date ranges and automatically move them into categorized folders.

## Features

- **Sort by File Type**: Categorize files based on their extensions and move them into appropriate subfolders.
- **Sort by Date**: Organize files by their creation or modification date.
- **Date Filters**: Filter files within a specified date range.
- **Interactive Prompts**: A user-friendly command-line interface with rich text formatting.
- **Extensible Design**: Easily modify or extend the functionality with custom classifiers and sorters.
- **Command-Line Interface**: User-friendly CLI for easy interaction with the application.

---

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Folder Structure](#folder-structure)
- [Classes and Modules](#classes-and-modules)
- [Contributing](#contributing)
- [Security](#security)
- [License](#license)

---

## Requirements

- Python 3.x
- Additional packages listed in `requirements.txt`

## Installation

1. Clone the repository:

   ```bash
   git clone [https://github.com/mohammad-abukhass/file-organizer.git](https://github.com/Moody03/file-organizer.git)
   cd file-organizer
   ```

2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

---

## Usage

1. Run the main script:

   ```bash
   python cli.py
   ```

2. Follow the on-screen prompts to specify the folder you want to organize. You can choose to:
   - Sort files by **type** or **date**.
   - Organize them into categorized subfolders.
   - Filter files by date range.

### Commands

| Command   | Description                               |
|-----------|-------------------------------------------|
| `help`    | Displays available commands and usage.    |
| `sort`    | Sort files by either 'type' or 'date'.    |
| `organize`| Organize files into categorized folders.  |
| `filter`  | Filter files by a date range.             |
| `exit`    | Exit the application.                     |

---

## Folder Structure

The project follows a modular design, separating different responsibilities:

```plaintext
file-organizer/
│
├── src/
│   ├── file_classifier.py          # File classification logic
│   ├── file_manager.py             # File system operations (read, write, metadata)
│   ├── file_sorter.py              # Sorting logic for files by type or date
│   ├── folder_structure.py         # Folder creation and file organization
│   ├── cli.py                      # Command-line interface for user interactions
│   └── utils.py                    # Utility functions for logging and error handling
├── tests/                          # Unit tests for each module
├── README.md                       # Project documentation
└── requirements.txt                # Python dependencies
```

---

## Classes and Modules

### `CLI.py`

This is the main script that provides a CLI for organizing your files. It uses the following modules:

- **FileClassifier**: Classifies files based on their extensions.
- **FileManager**: Scans directories, retrieves file metadata, reads/writes files.
- **FileSorter**: Sorts files by either type or date.
- **FolderStructure**: Organizes files into subfolders by either file type or date.

### `FileManager` (`file_manager.py`)

Handles file system operations like scanning directories, reading/writing files, and retrieving metadata.

**Key Methods:**

- `scan_folder()`: Scans the folder for files (supports nested folders).
- `get_file_metadata()`: Retrieves metadata such as file size, creation date, etc.
- `read_file()`: Reads the content of a file.
- `write_file()`: Writes content to a file, creating directories if needed.

### `FileClassifier` (`file_classifier.py`)

Responsible for classifying files based on their type (extension).

**Key Method:**

- `classify_files(files)`: Classifies a list of files into categories (e.g., documents, images, videos).

### `FileSorter` (`file_sorter.py`)

Sorts files either by type or date.

**Key Method:**

- `sort_files(files, folder)`: Sorts and returns a list of files ready for organization.

### `FolderStructure` (`folder_structure.py`)

Handles the organization of files into categorized folders. Also supports organizing by date.

**Key Methods:**

- `organize_files(files)`: Organizes files into folders by type.
- `organize_files_by_date(start_date, end_date)`: Organizes files into folders by their modification date.

### `Utils` (`src/utils.py`)

Contains utility functions for logging, error handling, and date parsing.

**Key Methods:**

- `setup_logger()`: Initializes the logger for the application.
- `handle_error(logger, error_message)`: Handles exceptions and logs errors.
- `parse_date(date_string)`: Parses a string into a datetime object.

---

## Contributing

Contributions are welcome! Here's how you can help:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes and commit (`git commit -m 'Add some feature'`).
4. Push to the branch (`git push origin feature-branch`).
5. Open a pull request.

Please ensure that your code follows best practices and includes tests for any new features or bug fixes.

---

## Security

We take security seriously. If you find any vulnerabilities or issues, please report them immediately by opening an issue or sending an email to [mohabukhass@hotmail.com].

To keep the project secure:

- Ensure any external packages or dependencies are regularly updated.
- Avoid committing any sensitive data (such as personal information or credentials) to the repository.

---

## License

This project is licensed under the MIT License. See the `LICENSE` file for more details.
