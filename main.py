import os
from pathlib import Path


INVALID_CHARACTERS = ["-", "*", "\\", "/", "~", "&", ":", ";", "?", "\"",
                      ">", "<", "|", "=", "%", "#", "º", "ª", "  "]


def recursive_replace(name: str, search: str, replace: str) -> str:
    """ remplaza todos los caracteres hasta que no quede ninguno"""
    if search == "-": # Caso puntual
        replace = "_"
    while search in name:
        name = name.replace(search, replace)
    return name


if __name__ == "__main__":
    # FICHERO = input("Ingrese la ruta a buscar: ")
    FICHERO = str(input("Ingrese la ruta a corregir: ")).replace("\'", "")
    n = 0 # Contador

    for archivo in Path(FICHERO).glob("**/*"):
        # revisamos si los elementos de INVALID_CHARACTERS estan en archivo.name
        if any(x in archivo.name for x in INVALID_CHARACTERS):
                old_name = archivo.name  # str
                for invalid in INVALID_CHARACTERS:
                        old_name = recursive_replace(old_name, invalid, "")
                new_file = archivo.with_name(old_name)
                # cambiamos de nombre en el sistema
                os.rename(archivo, new_file)
                # print(archivo.name)
                n += 1

        # Caso cuando el archivo comienza con un espacio
        if archivo.name[0] == " ":
            # definimos un new_name sin el primer espacio
            new_name = archivo.name[1:]
            new_file = archivo.with_name(new_name)
            os.rename(archivo, new_file)
            n += 1
        # TODO: Casos en los que queden espacios al final. EJ: "archivo    .txt" o "carpeta  "
        

    print("----+----\nCompleted", n, "elementos modificados")
