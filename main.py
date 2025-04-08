import glob
import os

# Request the path to the files from the user
path = input('Введите путь к вашим файлам, включая подкаталоги: ')

# Ensure the drive letter is uppercase
if len(path) > 1 and path[1] == ':':
    path = path[0].upper() + path[1:]

# Specify the path to your files, including subdirectories
all_files = glob.glob(rf'{path}\**\*.py', recursive=True)

# Filter out files from venv and .idea directories
filtered_files = [f for f in all_files if 'venv' not in f and '.idea' not in f]

try:
    combined_file_path = os.path.join(path, 'combined.py')
    with open(combined_file_path, 'a', encoding='utf-8') as outfile:
        for filename in filtered_files:
            try:
                with open(filename, encoding='utf-8') as infile:
                    outfile.write(infile.read() + '\n')  # Adds a new line between files
            except Exception as e:
                print(f'Error reading {filename}: {e}')
    # Ensure the drive letter is uppercase in the output message
    path = path[0].upper() + path[1:]
    print(f'File combined.py updated successfully in {path}.')
except Exception as e:
    print(f'Error writing to combTined.py: {e}')
