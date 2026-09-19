import subprocess


def render(host):
    # A new command injection introduced by THIS pull request (CWE-78).
    return subprocess.check_output("host " + host, shell=True)
