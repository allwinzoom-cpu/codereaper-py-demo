import os

BASE = "/srv/files"


def fetch(name):
    # HOP -> SINK: joined straight onto a base path (CWE-22).
    with open(os.path.join(BASE, name)) as fh:
        return fh.read()


def fetch_safe(name):
    # DECOY: the basename strips any traversal before the join.
    safe = os.path.basename(name)
    with open(os.path.join(BASE, safe)) as fh:
        return fh.read()
