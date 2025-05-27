from pathlib import Path

base = Path.home()
guia = Path(base,"Europa","España",Path("Barcelona","sagrada familia.txt"))

print(guia.parent)

