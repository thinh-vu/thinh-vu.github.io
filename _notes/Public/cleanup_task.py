import re
import os

# Define functions
def remove_lines_with_pattern(file_path, pattern):
    """
    Remove lines that match a specified pattern from a file.

    Args:
        file_path (str): The path to the file to modify.
        pattern (str): A regular expression pattern that matches the lines to remove.

    Returns:
        None
    """
    with open(file_path, 'r') as f:
        lines = f.readlines()

    with open(file_path, 'w') as f:
        for line in lines:
            if not re.match(pattern, line):
                f.write(line)


def replace_string_in_files(folder_path, search_for, replace_with):
    """
    Recursively replace all instances of a string in markdown files within a specific folder.

    Args:
        folder_path (str): The path to the folder containing the markdown files.
        search_for (str): The string to replace.
        replace_with (str): The replacement string.

    Returns:
        None
    """
    for subdir, dirs, files in os.walk(folder_path):
        for file in files:
            if file.endswith('.md'):
                file_path = os.path.join(subdir, file)
                with open(file_path, 'r') as f:
                    content = f.read()
                content = content.replace(search_for, replace_with)
                with open(file_path, 'w') as f:
                    f.write(content)

# Apply functions

note_folder = '/Users/thinh.vu/Library/CloudStorage/OneDrive-Personal/Github/thinh-vu.github.io/_notes/Public'
replace_string_in_files(note_folder, '[[pages/Index]]', '[[Index]]')