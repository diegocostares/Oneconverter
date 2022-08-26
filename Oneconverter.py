import os
from pathlib import Path


INVALID_CHARACTERS = ["-", "*", "\\", "/", "~", "&", ":", ";", "?", "\"",
                      ">", "<", "|", "=", "%", "#", "º", "ª", "  "]


def recursive_replace(name: str, search: str, replace: str) -> str:
    """ remplaza todos los caracteres hasta que no quede ninguno"""
    while search in name:
        name = name.replace(search, replace)
    return name


# BUG 1: No funciona si hay mas de un INVALID_CHARACTERS

if __name__ == "__main__":
    # FICHERO = input("Ingrese la ruta a buscar: ")
    FICHERO = input("Ingrese la ruta a corregir: ")

    for archivo in Path(FICHERO).glob("**/*"):
        # SI el archivo tiene un "-" se remplaza por " "
        for invalid in INVALID_CHARACTERS:
            if invalid in archivo.name:
                old_name = archivo.name  # str
                new_name = recursive_replace(old_name, invalid, "")
                new_name = recursive_replace(new_name, "  ", " ")

                new_file = archivo.with_name(new_name)
                # cambiamos de nombre en el sistema
                os.rename(archivo, new_file)

        # Caso cuando el archivo comienza con un espacio
        if archivo.name[0] == " ":
            # definimos un new_name sin el primer espacio
            new_name = archivo.name[1:]
            new_file = archivo.with_name(new_name)
            os.rename(archivo, new_file)

        # print(archivo)
    print("----+----\nCompleted")
