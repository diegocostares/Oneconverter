import os
from pathlib import Path


INVALID_CHARACTERS = ["*", "+", "\\", "/", ":", "?", "\"",
                      ">", "<", "^", "|", "á", "é", "í", "ó", "ú", "  "]


def recursive_replace(name: str, search: str, replace: str) -> str:
    """ remplaza todos los caracteres hasta que no quede ninguno"""
    if search == " .": # Caso puntual
      replace = "."
    while search in name:
        name = name.replace(search, replace)
    return name

if __name__ == "__main__":
    n = 0
    FICHERO = input("Ruta de la carpeta a revisar: ")
    for archivo in Path(FICHERO).glob("**/*"):   
        # revisamos si los elementos de INVALID_CHARACTERS estan en archivo.name
        if any(x in archivo.name for x in INVALID_CHARACTERS) or archivo.name[0] == " " or archivo.name[-1] == " ":
            new_name = archivo.name
            # Casos donde comienza o termina con espacios
            while new_name[0] == " ":
                new_name = new_name[1:]
            while new_name[::-1][0] == " ":
                new_name= new_name[:-1]
            # Casos de los caracteres invalidos
            for invalid in INVALID_CHARACTERS:
                new_name = recursive_replace(new_name, invalid, "")
            new_file = archivo.with_name(new_name)
            # cambiamos de nombre en el sistema
            os.rename(archivo, new_file)
            print(f"Modificado: {archivo.name}")
            n += 1
    print(f"\nCompletado: {n} elementos modificados.")