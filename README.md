# codereaper-py-demo

Deliberately vulnerable Python/Flask fixture for CodeReaper end-to-end validation.

Four real flows, every one CROSS-FILE (route -> service -> sink in a third module):

| Flow | Route | Path | Sink |
|---|---|---|---|
| CWE-89  | `/search`   | `main` -> `search.lookup` -> `db.run_query` | `cursor.execute` |
| CWE-78  | `/report`   | `main` -> `reports.build`                   | `subprocess(shell=True)` |
| CWE-22  | `/download` | `main` -> `storage.fetch`                   | `open(os.path.join(...))` |
| CWE-1336| `/preview`  | same file                                   | `render_template_string` |

Three decoys that must stay CLEAN, each proven live by mutation:

| Decoy | Protection | Mutated it fires at |
|---|---|---|
| closed allow-list | `kind not in (...)` | `mailer.py:8` |
| parameterised SQL | `execute(sql, params)` | `db.py:18` |
| basename guard | `os.path.basename` | `storage.py:15` |

Dependencies are pinned to old, known-vulnerable versions on purpose.
