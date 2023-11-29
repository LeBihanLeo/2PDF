import sys
import os
from docx2pdf import convert as convert_docx_to_pdf
from img2pdf import convert as convert_img_to_pdf
from pdf2docx import Converter
import fitz  # PyMuPDF


def convert_to_pdf(input_file):
    """
    Convert input file (docx, png, or jpg) to PDF.

    Parameters:
    - input_file: Path to the input file.
    """
    # Extract file name and extension
    file_name, file_extension = os.path.splitext(os.path.basename(input_file))

    # Define output PDF file path with the same name as input file
    output_file = f"{file_name}.pdf"

    valid_extensions = {'.docx', '.png', '.jpg', '.pdf'}  # Include '.pdf' as a valid extension
    if file_extension.lower() not in valid_extensions:
        print("Error: Invalid file type. Supported types are:", ", ".join(valid_extensions))
        sys.exit(1)

    # Check file type and perform conversion accordingly
    if file_extension.lower() == '.docx':
        convert_docx_to_pdf(input_file, output_file)
    elif file_extension.lower() in {'.png', '.jpg'}:
        try:
            with open(output_file, 'wb') as pdf_file, open(input_file, 'rb') as image_file:
                pdf_file.write(convert_img_to_pdf([image_file]))
        except IOError as e:
            print(f"Erreur d'écriture dans le dossier : {e}")
        except Exception as e:
            print(f"Une erreur inattendue s'est produite : {e}")


def convert_pdf_to_images(input_pdf, filename, extension):
    pdf_document = fitz.open(input_pdf)
    if pdf_document.page_count == 1 :
        page = pdf_document[0]
        image = page.get_pixmap()
        image.save(f"{filename}.{extension}")
        return
    for page_number in range(pdf_document.page_count):
        page = pdf_document[page_number]
        image = page.get_pixmap()
        image.save(f"{filename}_{page_number + 1}.{extension}")


def convert_pdf_to_docx(input_pdf):
    """
    Convertit un fichier PDF en fichier DOCX.

    Parameters:
    - input_pdf: Chemin du fichier PDF en entrée.
    - output_docx: Chemin du fichier DOCX de sortie.
    """
    file_name, file_extension = os.path.splitext(os.path.basename(input_pdf))
    output_docx = file_name+".docx"
    try:
        # Initialiser le convertisseur PDF to DOCX
        cv = Converter(input_pdf)

        # Convertir le PDF en DOCX
        cv.convert(output_docx, start=0, end=None)

        # Fermer le convertisseur
        cv.close()

        print(f"Conversion réussie: {input_pdf} vers {output_docx}")
    except Exception as e:
        print(f"Erreur lors de la conversion de {input_pdf} vers {output_docx}: {e}")
