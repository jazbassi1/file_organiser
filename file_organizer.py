import os
import shutil

def organize_files(directory="."):
    # Define file types and folders
    file_types = {
        "Images": [".jpg", ".png", ".gif"],
        "Documents": [".pdf", ".docx", ".txt"],
        "Scripts": [".py", ".sh"],
        "Others": []
    }

    # Create folders if they don't exist
    for folder in file_types.keys():
        path = os.path.join(directory, folder)
        if not os.path.exists(path):
            os.makedirs(path)

    # Move files to folders
    for file in os.listdir(directory):
        if os.path.isfile(os.path.join(directory, file)):
            file_ext = os.path.splitext(file)[1].lower()
            moved = False
            for folder, extensions in file_types.items():
                if file_ext in extensions:
                    shutil.move(
                        os.path.join(directory, file),
                        os.path.join(directory, folder, file)
                    )
                    moved = True
                    break
            if not moved:
                shutil.move(
                    os.path.join(directory, file),
                    os.path.join(directory, "Others", file)
                )

if __name__ == "__main__":
    organize_files()
