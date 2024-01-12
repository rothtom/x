import csv

def main():
    with open("students.csv", "r") as file:
        reader = csv.DictReader(file)
        ids = []
        names = []
        houses = []
        heads = []
        students = [names, houses, heads]
        for row in reader:
            ids.append(row["id"])
            names.append(row["student_name"])
            houses.append(row["house"])
            heads.append(row["head"])

    outfile_name = ["names", "houses", "heads"]
    for collumn in range(len(students)):
        save(ids, students[collumn], outfile_name[collumn])




def save(ids, names , outfile_name):
    students = []
    for i in range(len(ids)):
        students.append({"id": ids[i], "name": names[i]})


    with open(outfile_name + ".csv", "w") as file:
        writer = csv.DictWriter(file, fieldnames=["id", "name"])
        writer.writeheader()
        for row in students:
            writer.writerow(row)










if __name__ == "__main__":
    main()
