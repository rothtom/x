import csv

def main():
    with open("students.csv", "r") as file:
        reader = csv.DictReader(file)
        ids = []
        names = []
        houses = []
        heads = []
        for row in reader:
            ids.append(row["id"])
            names.append(row["student_name"])
            houses.append(row["house"])
            heads.append(row["head"])
    save_name(ids, names)
    save_house(houses)
    save_head(heads)




def save_names(ids, names):
    students = []
    for i in range(len(ids)):
        students.append({"id": ids[i], "name": names[i]})

    with open("names.csv", "w") as file:
        writer = csv.DictWriter(file, fieldnames=["id", "name"])
        writer.writeheader()
        for row in students:
            writer.writerow(row)


def save_house(house_list):
    with open("houses.csv", "w") as file:
        writer = csv.DictWriter(file, fieldnames=["house"])
        writer.writeheader()

        for house in house_list:
            writer.writerow({"house": house})


def save_head(head_list):
    with open("heads.csv", "w") as file:
        writer = csv.DictWriter(file, fieldnames=["head"])
        writer.writeheader()

        for head in head_list:
            writer.writerow({"head": head})












if __name__ == "__main__":
    main()
