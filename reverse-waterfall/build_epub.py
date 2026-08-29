from __future__ import annotations

import zipfile
from pathlib import Path

HERE = Path(__file__).resolve().parent
SRC = HERE / "epub-src"
OUTPUT = HERE / "reverse-waterfall-demo.epub"
FIXED_TIME = (2026, 8, 29, 0, 0, 0)


def add_file(zf: zipfile.ZipFile, source: Path, arcname: str, *, stored: bool = False) -> None:
    info = zipfile.ZipInfo(arcname, FIXED_TIME)
    info.compress_type = zipfile.ZIP_STORED if stored else zipfile.ZIP_DEFLATED
    info.external_attr = 0o100644 << 16
    zf.writestr(info, source.read_bytes())


def main() -> None:
    if OUTPUT.exists():
        OUTPUT.unlink()

    with zipfile.ZipFile(OUTPUT, "w") as zf:
        add_file(zf, SRC / "mimetype", "mimetype", stored=True)

        for path in sorted((SRC / "META-INF").rglob("*")):
            if path.is_file():
                add_file(zf, path, path.relative_to(SRC).as_posix())

        for path in sorted((SRC / "EPUB").rglob("*")):
            if path.is_file():
                add_file(zf, path, path.relative_to(SRC).as_posix())

    print(OUTPUT)


if __name__ == "__main__":
    main()
