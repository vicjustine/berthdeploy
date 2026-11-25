# berthdeploy

Berth manifest totals for the container terminal, deployed to staging and
production.

## Layout

| Path | What it is |
|---|---|
| `src/berthdeploy/manifest.py` | TEU totals and reefer share across the berth fleet |
| `tests/test_manifest.py` | Assertions on the fleet totals |

## Running the tests

```
python3 -m venv .venv
.venv/bin/pip install -e ".[dev]"
.venv/bin/pytest -q
```

## Deployment

Staging deploys on every push to `main`. Production is gated behind a required
reviewer. Neither environment stores a cloud credential.
