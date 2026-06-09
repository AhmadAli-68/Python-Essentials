import os

# Specify the directory path (you can change it to any directory you want)
directory_path = '.'  # '.' refers to the current directory

try:
    # Get the list of entries in the directory
    contents = os.listdir(directory_path)

    print(f"Contents of '{directory_path}':")
    for item in contents:
        print(item)

except FileNotFoundError:
    print(f"The directory '{directory_path}' was not found.")
except PermissionError:
    print(f"Permission denied to access '{directory_path}'.")