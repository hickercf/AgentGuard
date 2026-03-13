import sqlite3

conn = sqlite3.connect("agent_guard.db")

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE reports (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    task TEXT,
    report TEXT
)
""")

conn.commit()
conn.close()

print("数据库创建成功")