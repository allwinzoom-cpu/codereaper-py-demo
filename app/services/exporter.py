import subprocess
import shlex


def to_pdf(url):
    # NEW VULNERABILITY on the PR branch only (CWE-78).
    return subprocess.check_output("wkhtmltopdf " + url + " /tmp/o.pdf", shell=True)


def to_pdf_safe(url):
    # NEW DECOY on the same branch: argv form, no shell.
    return subprocess.check_output(["wkhtmltopdf", shlex.quote(url), "/tmp/o.pdf"])
