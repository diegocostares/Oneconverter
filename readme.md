# Oneconverter

Programa que lee el arbol de archivos y carpetas que se le entrega de input, identifica archivos con nombres invalidos que One Drive no permite subir y los renombra quitando los simbolos bloqueados.

## Ejecusion

```shell
python main.py
```

## Caracteres remplazados

- \*
- \
- /
- :
- ?
- <
- \>
- |
- á
- é
- í
- ó
- ú

## Caracteres opcionales

Se pueden incorporar de forma complementaria los siguientes caracteres, modificando la linea 5 de `main.py`

- ,
- ~
- &
- ;
- ¿
- =
- %
- \#
- º
- ª

Quedando la linea como:

```python
INVALID_CHARACTERS = ["*","\'", "~", "&", ";", "¿", "=", "%", "#", "º", "º", "+", "\\", "/", ":", "?", "\"", ">", "<", "^", "|", "  "]
```
