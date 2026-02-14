pip install pysqlite3
import sqlite3
conn = sqlite3.connect(&quot;school.db&quot;)
cur = conn.cursor()
cur.execute(&quot;&quot;&quot;
CREATE TABLE IF NOT EXISTS Students (
ID INTEGER PRIMARY KEY AUTOINCREMENT,
Name TEXT,
Age INTEGER,
Grade TEXT
)
&quot;&quot;&quot;)
data = [
(&quot;Alice&quot;, 20, &quot;A&quot;),
(&quot;Bob&quot;, 21, &quot;B&quot;)
]
cur.executemany(
&quot;INSERT INTO Students (Name, Age, Grade) VALUES (?, ?, ?)&quot;,
data
)
conn.commit()
print(&quot;Students:&quot;)
for row in cur.execute(&quot;SELECT * FROM Students&quot;):
print(row)
cur.execute(&quot;DELETE FROM Students WHERE ID = 1&quot;)
conn.commit()
print(&quot;\nAfter Deletion:&quot;)

for row in cur.execute(&quot;SELECT * FROM Students&quot;):
print(row)
conn.close()
OUTPUT:-
Students:
(1, &#39;Alice&#39;, 20, &#39;A&#39;)
(2, &#39;Bob&#39;, 21, &#39;B&#39;)
After Deletion:
(2, &#39;Bob&#39;, 21, &#39;B&#39;)
