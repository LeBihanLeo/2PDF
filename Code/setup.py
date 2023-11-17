import os
from colorama import init, Fore

# Initialise colorama pour permettre l'utilisation des couleurs ANSI
init(autoreset=True)

def run_reg_file(reg_file_path):
    print(Fore.YELLOW + "Open the windows security notification to autorise the installation")
    print(Fore.YELLOW + "It will install in the windows register the shortcut in the context menu")
    print(Fore.YELLOW + "If you want, you can also run manually the file 'add_to_context_menu.reg'")
    # Use os.system to run the reg file
    return os.system(f"start regedit /s {reg_file_path}")

def supprimer_fichier(chemin_du_fichier):
    try:
        os.remove(chemin_du_fichier)
    except FileNotFoundError:
        print(f"Le fichier {chemin_du_fichier} n'a pas été trouvé.")
    except Exception as e:
        print(f"Une erreur s'est produite lors de la suppression du fichier : {e}")


# Get the absolute path of the current directory
current_path = os.path.abspath(os.getcwd())

# Modify the path by adding '\' before each '\'
modified_path = current_path.replace("\\", "\\\\")
print(modified_path)

# Create the add_to_context_menu.reg file
reg_file_path = os.path.join(current_path, "add_to_context_menu.reg")

# Open the file in write mode
with open(reg_file_path, "w") as reg_file:
    # Write the Windows Registry Editor Version header
    reg_file.write("Windows Registry Editor Version 5.00\n\n")

    # Write the registry entries with the modified path
    reg_file.write("[HKEY_CLASSES_ROOT\\*\\shell\\2PDF]\n")
    reg_file.write("@=\"Convertir en PDF\"\n")
    reg_file.write("\"Icon\"=\"{}\\\\dist\\\\2PDF\\\\2PDF.exe,0\"\n\n".format(modified_path))

    reg_file.write("[HKEY_CLASSES_ROOT\\*\\shell\\2PDF\\command]\n")
    reg_file.write("@=\"\\\"{}\\\\dist\\\\2PDF\\\\2PDF.exe\\\" \\\"%1\\\"\"\n".format(modified_path))

if run_reg_file(reg_file_path):
    print(Fore.YELLOW + "'add_to_context_menu.reg' has been correctly installed")
    print(Fore.YELLOW + "You can run it manually to add 2PDF to the context menu")
else:
    supprimer_fichier(reg_file_path)
    print(Fore.GREEN + "2PDF has been correctly installed")
input("Press enter to close the window...")