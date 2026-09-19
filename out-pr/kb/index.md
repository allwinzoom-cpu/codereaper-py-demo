---
okf_version: "0.2"
---

# Knowledge bundle

- [OS command injection: untrusted input reaches a shell command](/findings/F-0001.md) `finding` — Deterministic detector: taint proves untrusted input reaches a shell command in `app/services/exporter.py`. Evidence line 7: return subprocess.check_output("wkhtmltopdf " + url + " /tmp/o.pdf", shell=True)
- [Server-side template injection (SSTI): untrusted input is compiled as a template](/findings/F-0002.md) `finding` — Deterministic detector: Python taint proves untrusted input reaches a ssti sink in `app/main.py`. Evidence line 34: return render_template_string("<h1>" + tpl + "</h1>")
