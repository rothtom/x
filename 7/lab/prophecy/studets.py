from cs50 import SQL

def main():
    db = SQL("sqlite:///roster.db")
    print(db)

    name = db.execute("CREATE TABLE name (
                      id INEGER,
                      student_name TEXT NOT NULL,
                      PRIMARY(id))')

    house =db.execute("CREATE TABLE house (
                      house_if INTEGER,
                      house TEXT NOT NULL,
                      FOREIGN(house_id) REFERENCES(id)
                      );")
    print(name, house)


main()
