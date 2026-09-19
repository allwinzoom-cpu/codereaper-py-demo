import subprocess

TEMPLATES = {"welcome": "w.tpl", "reset": "r.tpl", "receipt": "x.tpl"}


def send(kind):
    # Reached only with a value the caller already restricted to a closed set.
    return subprocess.check_output("cat /srv/tpl/" + TEMPLATES[kind], shell=True).decode()
