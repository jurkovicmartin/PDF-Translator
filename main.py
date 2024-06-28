
import customtkinter as ctk
from PIL import Image
import os

from functions import select_file, get_language_code
from translation import translation, load_auth_key
from pdf_functions import extract_text, new_pdf

def main():

    def file_selection_callback(path: str):
        nonlocal source_path
        source_path = path
        # Show path of selected file
        selected_label.configure(text=f"{source_path}")


    def translate():
        # Source path not provided
        if not source_path:
            return
        
        pdf_text =  extract_text(source_path)
        target_lang = get_language_code(language_combobox.get())

        translated_text = translation(api_key, target_lang, pdf_text)
        # Error with translation
        if translated_text is None:
            return

        # Creating a new pdf with translated text
        file, extension = os.path.splitext(source_path)
        # Add _copy to file name
        file = file + "_copy"
    
        new_path = file + extension

        new_pdf(new_path, translated_text)
        # Show path of translate file
        translated_label.configure(text=new_path)
        

    # "Global" variables
    api_key = load_auth_key()
    source_path = ""

    root = ctk.CTk()
    root.title("PDF Translator")
    root.geometry("500x400")
    ctk.set_default_color_theme("dark-blue")

    root.grid_columnconfigure((0,1), weight=1)

    # DeepL logo
    logo = ctk.CTkImage(light_image=Image.open("res/img/deepl_logo.png"), dark_image=Image.open("res/img/deepl_logo.png"), size=(200,100))
    logo_label = ctk.CTkLabel(root, text="", image=logo)
    logo_label.grid(row=0, column=0, columnspan=2, pady=10)
    note_label = ctk.CTkLabel(root, text="Note: DeepL is used for the translation.")
    note_label.grid(row=1, column=0, columnspan=2)

    # File selection
    select_btn = ctk.CTkButton(root, text="Select File", command=lambda: select_file(file_selection_callback))
    select_btn.grid(row=2, column=0, rowspan=2, padx=10, pady=10)
    select_label = ctk.CTkLabel(root, text="Selected file:")
    select_label.grid(row=2, column=1, padx=10, pady=10)
    selected_label = ctk.CTkLabel(root, text="")
    selected_label.grid(row=3, column=1, padx=10)

    # Language selection
    languages = [
        "English",
        "German",
        "Czech",
        "Spanish",
        "French"
    ]

    language_label = ctk.CTkLabel(root, text="Select desired language")
    language_label.grid(row=4, column=0, padx=10, pady=10)
    language_combobox = ctk.CTkComboBox(root, values=languages)
    language_combobox.set(languages[0])
    language_combobox.grid(row=4, column=1, padx=10, pady=10)

    # Translation
    translate_btn = ctk.CTkButton(root, text="Translate", command=translate)
    translate_btn.grid(row=5, column=0, rowspan=2, padx=10, pady=10)
    translate_label = ctk.CTkLabel(root, text="Translated file:")
    translate_label.grid(row=5, column=1, padx=10, pady=10)
    translated_label = ctk.CTkLabel(root, text="")
    translated_label.grid(row=6, column=1, padx=10)


    root.mainloop()

    
    

if __name__ == "__main__":
    main()