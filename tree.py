from pathlib import Path


entries = Path('D:/')
for entry in entries.iterdir():
    print (entry.name)


entries = Path('D:/Python')
for entry in entries.iterdir():
    print (entry.name)

entries = Path('D:/Python/Introduction')
for entry in entries.iterdir():
    print (entry.name)


entries = Path('D:/Python/Modularization')
for entry in entries.iterdir():
    print (entry.name)

entries = Path('D:/Python/PHANTOM')
for entry in entries.iterdir():
    print (entry.name)

entries = Path('D:/Python/WEB')
for entry in entries.iterdir():
    print (entry.name)

entries = Path('C:/')
for entry in entries.iterdir():
    print (entry.name)
