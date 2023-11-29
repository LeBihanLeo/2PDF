import sys
import os
import converter
# Check if command-line arguments are provided correctly
if __name__ == "__main__":
    if len(sys.argv) < 2 or len(sys.argv) >= 4:
        print("Usage: python convert_to_pdf.py <input_file> [--pdf-to-png|--pdf-to-jpeg|--pdf-to-docx]")
        sys.exit(1)
    print("test hello world")

    # Get input file path from command-line arguments
    input_file_path = sys.argv[1]
    
    # Check if the input file exists
    if not os.path.exists(input_file_path):
        print("Error: Input file not found.")
        sys.exit(1)

    # Check for additional conversion options
    if len(sys.argv) == 3:
        file_name, file_extension = os.path.splitext(os.path.basename(input_file_path))
        conversion_option = sys.argv[2]
        if conversion_option == "--pdf-to-png":
            converter.convert_pdf_to_images(input_file_path, file_name, "png")

        elif conversion_option == "--pdf-to-jpg":
            converter.convert_pdf_to_images(input_file_path, file_name, "jpg")
        
        
        elif conversion_option == "--pdf-to-docx":
            # Définissez le chemin de sortie du fichier DOCX
            output_docx = f"{input_file_path}.docx"
            
            # Appelez la fonction de conversion PDF vers DOCX
            converter.convert_pdf_to_docx(input_file_path)
        else:
            print("Argument not recognized")
    else:
        print("go pdf cause: "+str(len(sys.argv))+" and "+str(sys.argv))
        converter.convert_to_pdf(input_file_path)