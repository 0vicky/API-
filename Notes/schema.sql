CREATE TABLE IF NOT EXISTS notes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    content TEXT NOT NULL,
    type TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL,
    password TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS shared_notes (
    note_id INTEGER,
    user_id INTEGER,
    FOREIGN KEY (note_id) REFERENCES notes (id),
    FOREIGN KEY (user_id) REFERENCES users (id)
);
