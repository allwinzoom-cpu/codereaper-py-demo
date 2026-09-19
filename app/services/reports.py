import subprocess
import shlex


def build(target):
    # HOP -> SINK: shell=True with concatenated attacker input (CWE-78).
    return subprocess.check_output("ping -c 1 " + target, shell=True).decode()


def build_safe(target):
    # DECOY: quoted, and not a shell at all.
    return subprocess.check_output(["ping", "-c", "1", shlex.quote(target)]).decode()
