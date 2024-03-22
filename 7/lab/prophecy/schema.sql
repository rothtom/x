CREATE TABLE names (
    id INTEGER NOT NULL,
    name TEXT NOT NULL,
    PRIMARY KEY(id)
);

CREATE TABLE houses (
    house TEXT NOT NULL,
    house_id INTEGER,
    FOREIGN KEY(house_id) REFERENCES names(id)
);

CREATE TABLE heads (
    head TEXT NOT NULL,
    head_id INTEGER,
    FOREIGN KEY(head_id) REFERENCES names(id)
);



