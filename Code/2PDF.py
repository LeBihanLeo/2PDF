import sys
import os
from docx2pdf import convert as convert_docx_to_pdf
from img2pdf import convert as convert_img_to_pdf

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

    valid_extensions = {'.docx', '.png', '.jpg'}
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


if __name__ == "__main__":
    # Check if command-line arguments are provided correctly
    if len(sys.argv) != 2:
        print("Usage: python convert_to_pdf.py <input_file>")
        sys.exit(1)

    # Get input file path from command-line arguments
    input_file_path = sys.argv[1]
    
    # Check if the input file exists
    if not os.path.exists(input_file_path):
        print("Error: Input file not found.")
        sys.exit(1)

    # Call the conversion function with the provided input file
    convert_to_pdf(input_file_path)
