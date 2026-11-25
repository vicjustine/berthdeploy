import json
import sys
import pathlib

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1] / "scripts"))

from build_site import render  # noqa: E402


def test_page_carries_the_totals():
    html = render()
    assert "7,800 TEU" in html
    assert "3 berths" in html
    assert "69.2% reefer" in html


def test_every_berth_has_a_row():
    html = render()
    for berth in ("B1", "B2", "B3"):
        assert f"<td>{berth}</td>" in html


def test_reefer_column_is_rendered_as_words():
    html = render()
    assert "<td>yes</td>" in html
    assert "<td>no</td>" in html
