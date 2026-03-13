import sqlite3
import os


def init_database():
    db_path = os.path.join(
        os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))),
        "agent_guard.db"
    )
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS reports (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        task TEXT,
        report TEXT,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    """)

    # Migrate existing tables: add created_at column if missing
    cursor.execute("PRAGMA table_info(reports)")
    columns = [col[1] for col in cursor.fetchall()]
    if "created_at" not in columns:
        cursor.execute(
            "ALTER TABLE reports ADD COLUMN created_at TIMESTAMP DEFAULT NULL"
        )

    conn.commit()
    conn.close()
    print("数据库创建成功")


if __name__ == "__main__":
    init_database()
