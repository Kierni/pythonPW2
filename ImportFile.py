import json
from pathlib import Path

path = Path("phones.json")

if path.exists():
    f = open(path, "r")
    phones = json.load(f)
    f.close();
    print(phones)
else:
    phones = {};

