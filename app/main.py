"""Entry points. Every route here is an attacker-controlled source."""
from flask import Flask, request, render_template_string

from app.services import reports, search, storage, mailer

app = Flask(__name__)


@app.route("/search")
def do_search():
    # FLOW 1 (cross-file, 2 hops): request -> search.lookup -> db.run_query -> SQL sink
    term = request.args.get("q", "")
    return search.lookup(term)


@app.route("/report")
def do_report():
    # FLOW 2 (cross-file, 2 hops): request -> reports.build -> shell sink
    target = request.args.get("host", "")
    return reports.build(target)


@app.route("/download")
def do_download():
    # FLOW 3 (cross-file): request -> storage.fetch -> open() path traversal
    name = request.args.get("name", "")
    return storage.fetch(name)


@app.route("/preview")
def do_preview():
    # FLOW 4 (same-file): request -> render_template_string -> SSTI
    tpl = request.args.get("tpl", "")
    return render_template_string("<h1>" + tpl + "</h1>")


@app.route("/notify")
def do_notify():
    # DECOY 1: the value is validated against a closed allow-list before the sink.
    kind = request.args.get("kind", "")
    if kind not in ("welcome", "reset", "receipt"):
        return "bad kind", 400
    return mailer.send(kind)


@app.route("/stats")
def do_stats():
    # DECOY 2: a constant, never attacker-controlled, reaching the same sink as FLOW 1.
    return search.lookup_exact("daily")
