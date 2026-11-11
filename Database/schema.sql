CREATE TABLE IF NOT EXISTS users (
    user_id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL UNIQUE,
    password TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS daily_health (
    health_id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER NOT NULL,
    entry_date TEXT NOT NULL,
    steps INTEGER NOT NULL DEFAULT 0,
    calories INTEGER NOT NULL DEFAULT 0,

    FOREIGN KEY (user_id) REFERENCES users(user_id),
    UNIQUE (user_id, entry_date)
);