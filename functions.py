
from tkinter import filedialog
import os
from tkinter import messagebox

def select_file(callback):
    # Loop for repeated asking
    while True:
        path = filedialog.askopenfilename()
        # File was selected
        if path:
            # Get file extension
            file, extension = os.path.splitext(path)

            if extension == ".pdf":
                callback(path)
                break
            # Wrong file format
            else:
                messagebox.showerror("File selection error.", "You must select a pdf file.")
        # Not selecting a file
        else:
            break


def get_language_code(language: str) -> str:
    if language == "English":
        return "EN-US"
    elif language == "German":
        return "DE"
    elif language == "Czech":
        return "CS"
    elif language == "Spanish":
        return "ES"
    elif language == "French":
        return "FR"
    else:
        raise Exception("Unsupported language")