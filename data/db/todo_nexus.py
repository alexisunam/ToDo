import sqlite3


class ToDoNexus:

    def __init__(self):
        self.db_name = 'data/db/todo.db'
        self._create_table()

    def _create_table(self):
        with sqlite3.connect(self.db_name) as conn:
            c = conn.cursor()
            c.execute('''CREATE TABLE IF NOT EXISTS todos (id INTEGER PRIMARY KEY, title VARCHAR(20),
             description TEXT, done BOOLEAN DEFAULT 0, due_date VARCHAR(11),
              created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP)''')
            conn.commit()

    def add(self, title: str, description: str, due_date: str):
        with sqlite3.connect(self.db_name) as conn:
            c = conn.cursor()
            c.execute('INSERT INTO todos (title, description, due_date) VALUES (?, ?, ?)',
                      (title, description, due_date))
            conn.commit()
            c.execute('INSERT INTO todos (title, description, due_date) VALUES (?, ?, ?)',
                           (title, description, due_date))
            conn.commit()

    def get_all(self) -> list:
        with sqlite3.connect(self.db_name) as conn:
            c = conn.cursor()
            c.execute('SELECT * FROM todos')
            return c.fetchall()

    def get_one(self, identifier: int):
        with sqlite3.connect(self.db_name) as conn:
            c = conn.cursor()
            c.execute('SELECT * FROM todos WHERE id=?', (identifier,))
            return c.fetchone()

    def update(self, identifier: int, title: str, description: str, done: bool, due_date: str):
        with sqlite3.connect(self.db_name) as conn:
            c = conn.cursor()
            c.execute('UPDATE todos SET title=?, description=?, done=?, due_date=? WHERE id=?',
                           (title, description, done, due_date, identifier))
            conn.commit()

    def delete(self, identifier: int):
        with sqlite3.connect(self.db_name) as conn:
            c = conn.cursor()
            c.execute('DELETE FROM todos WHERE id=?', (identifier,))
            conn.commit()

