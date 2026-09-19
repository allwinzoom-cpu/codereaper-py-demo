from app.services import db


def lookup(term):
    # HOP: builds the injectable SQL and hands it to the sink in another module.
    return db.run_query("SELECT id, title FROM docs WHERE title LIKE '%" + term + "%'")


def lookup_exact(term):
    # DECOY: parameterised -- the value never becomes part of the statement.
    return db.run_parameterised("SELECT id, title FROM docs WHERE title = ?", (term,))
