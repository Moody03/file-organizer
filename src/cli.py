import argparse
import os
from file_classifier import FileClassifier
from file_manager import FileManager
from file_sorter import FileSorter
from folder_structure import FolderStructure
from src.utils import setup_logger, handle_error, parse_date
from colorama import Fore, Style, init
from rich.console import Console
from rich.prompt import Prompt
from rich.table import Table
from enum import Enum

# Initialize Colorama
init(autoreset=True)

class SortOption(Enum):
    TYPE = 'type'
    DATE = 'date'

def display_welcome_message():
    console = Console()
    console.print(Fore.CYAN + "Welcome to File Organizer!", style="bold")
    console.print("This application helps you organize files in a folder by type or date, or both.")
    console.print("You can either sort files, organize them into folders, or apply filters by date.\n")

def display_help_message():
    console = Console()
    table = Table(title="Available Commands")

    table.add_column("Command", style="cyan")
    table.add_column("Description", style="magenta")

    table.add_row("help", "Display this help message")
    table.add_row("exit", "Exit the application")
    table.add_row("sort", "Sort files by 'type' or 'date'")
    table.add_row("organize", "Organize files into folders")
    table.add_row("filter", "Filter files by date range")

    console.print(table)

def prompt_user_for_input():
    folder = Prompt.ask("Please enter the path to the folder you want to organize", default=os.getcwd())
    return folder

def get_sort_option():
    sort_option = Prompt.ask("Do you want to sort by 'type' or 'date'? (leave blank if not applicable)", default="")
    organize_option = Prompt.ask("Do you want to organize files into folders? (yes/no)", choices=["yes", "no"], default="yes")
    start_date = Prompt.ask("Enter the start date for file filtering (YYYY-MM-DD) or leave blank", default="")
    end_date = Prompt.ask("Enter the end date for file filtering (YYYY-MM-DD) or leave blank", default="")
    
    return sort_option, organize_option == "yes", start_date, end_date

def main():
    logger = setup_logger()
    console = Console()

    # Display welcome message
    display_welcome_message()
    
    while True:
        folder = prompt_user_for_input()
        if folder.lower() == 'help':
            display_help_message()
            continue  # Return to the beginning of the loop
        elif folder.lower() == 'exit':
            console.print(Fore.GREEN + "Exiting the application. Goodbye!", style="bold")
            break  # Exit the loop

        # Check if folder is a valid directory
        if not os.path.isdir(folder):
            logger.error(Fore.RED + f"The path '{folder}' is not a valid directory.")
            continue  # Prompt for the folder again

        # Get sorting and organizing options
        sort_option, organize_option, start_date, end_date = get_sort_option()

        try:
            file_manager = FileManager(folder)
            file_classifier = FileClassifier()
            file_sorter = FileSorter()
            folder_structure = FolderStructure(folder)

            start_date = parse_date(start_date) if start_date else None
            end_date = parse_date(end_date) if end_date else None

            files = file_manager.scan_folder()
            logger.info(f"Found {len(files)} files in the folder.")

            if sort_option:
                if sort_option == SortOption.TYPE.value:
                    logger.info("Sorting files by type...")
                    categorized_files = file_classifier.classify_files(files)
                    sorted_files = file_sorter.sort_files(categorized_files, folder)
                    folder_structure.organize_files(sorted_files)
                    logger.info(Fore.GREEN + "Files sorted by type successfully.")
                elif sort_option == SortOption.DATE.value:
                    logger.info("Sorting files by date...")
                    folder_structure.organize_files_by_date(start_date, end_date)
                    logger.info(Fore.GREEN + "Files sorted by date successfully.")
            elif organize_option:
                logger.info("Organizing files...")
                categorized_files = file_classifier.classify_files(files)
                sorted_files = file_sorter.sort_files(categorized_files, folder)
                folder_structure.organize_files(sorted_files, start_date, end_date)
                logger.info(Fore.GREEN + "Files organized successfully.")
            else:
                logger.warning(Fore.YELLOW + "No action specified. Use --sort or --organize.")

        except Exception as e:
            handle_error(logger, str(e))

if __name__ == "__main__":
    main()
