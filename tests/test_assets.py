import os
from pathlib import Path
from bs4 import BeautifulSoup


def test_local_image_sources_exist():
    root = Path(__file__).resolve().parents[1]
    html_file = root / "index.html"
    assert html_file.exists(), "index.html should exist"
    soup = BeautifulSoup(html_file.read_text(encoding="utf-8"), "html.parser")

    for tag in soup.find_all(src=True):
        src = tag['src']
        if src.startswith('images/'):
            img_path = root / src
            assert img_path.exists(), f"Referenced image {src} does not exist"

