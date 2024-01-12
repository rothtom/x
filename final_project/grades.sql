CREATE TABLE grades (
    subject_id INTEGER NOT NULL,
    user_id INTEGER NOT NULL,
    subject TEXT NOT NULL,
    grade FLOAT DEFAULT "",
    written FLOAT DEFAULT "",
    oral FLOAT DEFAULT "",
    input_count NUMBER DEFAULT 0,
    PRIMARY KEY (subject_id)
);

CREATE TABLE users (
    id INTEGER NOT NULL UNIQUE,
    real_name TEXT NOT NULL,
    user_name TEXT NOT NULL UNIQUE,
    password TEXT NOT NULL,
    PRIMARY KEY (id)
);
