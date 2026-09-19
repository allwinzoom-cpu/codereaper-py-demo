---
okf_version: "0.2"
---

# Knowledge bundle

- [SQL injection: untrusted input reaches 'sql_execute_var' sink](/findings/F-0001.md) `finding` — Deterministic detector: a SQL sink ('sql_execute_var') co-occurs with a query built from untrusted input in `app/services/db.py`. Evidence line 11: cur.execute(sql)
- [OS command injection: untrusted input reaches a shell command](/findings/F-0002.md) `finding` — Deterministic detector: taint proves untrusted input reaches a shell command in `app/services/reports.py`. Evidence line 7: return subprocess.check_output("ping -c 1 " + target, shell=True).decode()
- [Path traversal: user-controlled path reaches a file sink](/findings/F-0003.md) `finding` — Deterministic detector: taint proves untrusted input reaches a path_open sink in `app/services/storage.py`. Evidence line 8: with open(os.path.join(BASE, name)) as fh:
- [Server-side template injection (SSTI): untrusted input is compiled as a template](/findings/F-0004.md) `finding` — Deterministic detector: Python taint proves untrusted input reaches a ssti sink in `app/main.py`. Evidence line 34: return render_template_string("<h1>" + tpl + "</h1>")
