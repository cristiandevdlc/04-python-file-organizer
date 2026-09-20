import argparse
import shutil
from pathlib import Path


def organize(folder, apply=False):
    folder = Path(folder).expanduser().resolve()
    if not folder.is_dir():
        raise SystemExit(f"No existe la carpeta: {folder}")
    for item in sorted(folder.iterdir()):
        if not item.is_file() or item.name.startswith("."):
            continue
        group = item.suffix.lower().lstrip(".") or "sin-extension"
        target = folder / group
        destination = target / item.name
        print(f"{item.name} -> {group}/")
        if apply:
            target.mkdir(exist_ok=True)
            shutil.move(str(item), str(destination))


parser = argparse.ArgumentParser()
parser.add_argument("folder")
parser.add_argument("--apply", action="store_true")
args = parser.parse_args()
organize(args.folder, args.apply)
