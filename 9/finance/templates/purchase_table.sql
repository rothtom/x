CREATE TABLE purchases (
    user_id INTEGER,
    stock_name TEXT NOT NULL,
    shares INTEGER,
    FOREIGN KEY (user_id) REFERENCES users(id)
);
