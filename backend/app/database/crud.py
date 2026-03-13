from app.database.db import get_connection


def save_report(task, report):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT INTO reports (task, report)
        VALUES (?, ?)
        """,
        (task, str(report))
    )

    conn.commit()
    conn.close()


def get_reports():

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "SELECT id, task, report FROM reports ORDER BY id DESC"
    )

    rows = cursor.fetchall()

    conn.close()

    return rows