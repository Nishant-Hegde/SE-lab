"""Manage apartment society dues, payments, and late fees."""

import sqlite3

conn = sqlite3.connect(":memory:")
conn.execute(
    "CREATE TABLE dues (flat TEXT, month TEXT, "
    "amount INTEGER, paid INTEGER)"
)


def add_due(flat, month, amount, history=None):
    """Add a dues record and track it in the supplied history."""
    if history is None:
        history = []

    conn.execute(
        "INSERT INTO dues VALUES (?, ?, ?, 0)",
        (flat, month, amount),
    )
    history.append((flat, month))
    return history


def collect(flat, month):
    """Mark a dues record as paid and return its amount, or None."""
    row = conn.execute(
        "SELECT amount FROM dues WHERE flat = ? AND month = ?",
        (flat, month),
    ).fetchone()

    if row is None:
        return None

    conn.execute(
        "UPDATE dues SET paid = 1 WHERE flat = ? AND month = ?",
        (flat, month),
    )
    return row[0]


def penalty(rate, months_late):
    """Calculate a late fee from a rate and the number of late months."""
    if rate < 0 or months_late < 0:
        raise ValueError("Rate and months late must be non-negative")

    return rate * months_late


def pending():
    """Return the flat identifiers for unpaid dues."""
    rows = conn.execute(
        "SELECT flat FROM dues WHERE paid = 0"
    ).fetchall()
    return [row[0] for row in rows]


def main():
    """Demonstrate adding dues, collecting payment, and checking balances."""
    add_due("A-101", "Oct", 2500)
    add_due("A-102", "Oct", 2500)
    print(collect("A-101", "Oct"))
    print(penalty(50, 2))
    print(pending())


if __name__ == "__main__":
    main()
