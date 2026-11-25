"""Render the berth manifest as a static site for GitHub Pages."""
import json
import pathlib

from berthdeploy.manifest import FLEET, manifest

OUT = pathlib.Path("site")

CSS = """
  :root { color-scheme: light dark; }
  body { font-family: system-ui, sans-serif; max-width: 42rem;
         margin: 3rem auto; padding: 0 1rem; line-height: 1.6; }
  table { border-collapse: collapse; width: 100%; margin-top: 1.5rem; }
  th, td { border: 1px solid #8884; padding: .5rem .75rem; text-align: left; }
  th { background: #8881; }
  td:nth-child(2) { font-variant-numeric: tabular-nums; }
  .totals { color: #666; }
"""


def render() -> str:
    m = manifest()
    rows = "\n".join(
        f"      <tr><td>{s.berth}</td><td>{s.teu:,}</td>"
        f"<td>{'yes' if s.reefer else 'no'}</td></tr>"
        for s in FLEET
    )
    return f"""<!doctype html>
<html lang="en">
<meta charset="utf-8">
<title>Berth manifest</title>
<meta name="viewport" content="width=device-width,initial-scale=1">
<style>{CSS}</style>
<h1>Berth manifest</h1>
<p class="totals">{m['berths']} berths &middot; {m['total_teu']:,} TEU &middot;
   {m['reefer_share']:.1%} reefer</p>
<table>
  <thead><tr><th>Berth</th><th>TEU</th><th>Reefer</th></tr></thead>
  <tbody>
{rows}
  </tbody>
</table>
</html>
"""


if __name__ == "__main__":
    OUT.mkdir(exist_ok=True)
    (OUT / "index.html").write_text(render())
    (OUT / "manifest.json").write_text(json.dumps(manifest(), indent=2))
    print(f"built site/ with {len(FLEET)} berths")
