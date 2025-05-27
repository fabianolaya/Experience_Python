
from pathlib import Path, PureWindowsPath

carpeta = Path('C:/Users/FabianPC/Desktop/Python/pythonProject1/dia 6/prueba1.txt')

ruta_windows =  PureWindowsPath(carpeta)

if not carpeta.exists():
    print('El archivo no existe')
else:
    print('genial Existe' + '\n')

print(carpeta.read_text())
print(carpeta.name)
print(carpeta.suffix)
print(carpeta.stem)

print(ruta_windows)


