import os
import re


def kebab_case(filename):
    # Convert the filename to lowercase, replace spaces with hyphens, and remove special characters
    return re.sub(r"[^a-z0-9]+", "-", filename.lower()).strip("-")


def clean_filename(filename):
    # Remove the hash part (alphanumeric sequence at the end of the name) and .md extension
    splitfilename = filename.split(".")[0].split("-")[:-2]
    return "-".join(splitfilename)


def rename_files(folder_path):
    for filename in os.listdir(folder_path):
        # Check if it's a markdown file
        if filename.endswith(".md"):
            # Remove the hash part using regex and remove extension for kebab casing
            new_filename = f"{clean_filename(filename)}.md"
            print(new_filename)

            # Get full paths for renaming
            old_path = os.path.join(folder_path, filename)
            new_path = os.path.join(folder_path, new_filename)

            # Rename the file
            os.rename(old_path, new_path)
            print(f'Renamed "{filename}" to "{new_filename}"')


# Example usage:
folder_path = "./notion_export/recipes"  # Replace with your folder path
rename_files(folder_path)
