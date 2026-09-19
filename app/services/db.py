import sqlite3


def connect():
    return sqlite3.connect("app.db")


def run_query(sql):
    """SINK: raw SQL string execution (CWE-89)."""
    cur = connect().cursor()
    cur.execute(sql)
    return cur.fetchall()


def run_parameterised(sql, params):
    """DECOY SINK: the same call, but the caller must pass parameters separately."""
    cur = connect().cursor()
    cur.execute(sql, params)
    return cur.fetchall()
