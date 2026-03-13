from datetime import datetime

from app.database.db import get_connection


def save_report(task, report):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT INTO reports (task, report, created_at)
        VALUES (?, ?, ?)
        """,
        (task, str(report), datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    )

    conn.commit()
    conn.close()


def get_reports():

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "SELECT id, task, report, created_at FROM reports ORDER BY id DESC"
    )

    rows = cursor.fetchall()

    conn.close()

    return rows
