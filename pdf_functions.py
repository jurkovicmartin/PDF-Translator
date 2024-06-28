
import pymupdf # PyMuPDF


def extract_text(path: str) -> list[str]:
    """
    Extract text from pdf file.

    Returns
    ----
    List with string items (each item is a text of one page)
    """
    doc = pymupdf.open(path)
    
    text = []
    for page in doc:
        text.append(page.get_text())
    
    doc.close()
    return text


def new_pdf(new_path: str, text: list[str]):
    """
    Creates a new pdf file as a copy of the original and text replacement.

    Parameters
    -----
    text: each item of the list has text of one page
    """
    new_doc = pymupdf.open()

    # Text starting point (formating)
    point = pymupdf.Point(50, 72)

    for page in range(len(text)):
        new_page = new_doc.new_page()
        # Using "custom" font for showing more characters (czech)
        new_page.insert_font(fontfile="res/font/arial.ttf", fontname="MyFont")
        # str() used because API does not return simple string object
        new_page.insert_text(point, str(text[page]), fontname="MyFont", fontsize = 12)

    new_doc.save(new_path)
    new_doc.close()
