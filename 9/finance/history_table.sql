CREATE TABLE history (
    purchase_id INTEGER NOT NULL,
    user_id INTEGER,
    name TEXT NOT NULL,
    shares INTEGER NOT NULL,
    stock_price INTEGER NOT NULL,
    value INTEGER NOT NULL,
    time_stamp NUMBER NOT NULL,
    trans_type TEXT NOT NULL,
    PRIMARY KEY (purchase_id),
    FOREIGN KEY (user_id) REFERENCES users(id)
);
