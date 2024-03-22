import csv
import sys



def main():

    # TODO: Check for command-line usage
    cla_usage, database_file, sequence_file = check_cla()
    if cla_usage != True:
        sys.exit("Incorrect argument count!")

    # TODO: Read database file into a variable
    database = load_database(database_file)
    # TODO: Read DNA sequence file into a variable
    dna_sequence = load_dna_sequence(sequence_file)
    # TODO: Find longest match of each STR in DNA sequence
    longest_match = {}
    for str in database[0].keys():
        if str != "name":
            longest_run = get_longest_match(dna_sequence, str)
            longest_match[str] = longest_run
    # TODO: Check database for matching profiles
    matching_person = check_database_match(longest_match, database)
    if matching_person:
        print(f"Matches {matching_person}")
    else:
        print("No matches found!")

    return


def check_cla():
    if len(sys.argv) == 3:
        return True, sys.argv[1], sys.argv[2]

def load_database(file):
    with open(file, "r") as database_address:
        if database_address:
            database = []
            reader = csv.DictReader(database_address)
            for row in reader:
                database.append(row)

            return database

        else:
            return "Couldn't open database!"


def load_dna_sequence(file):
    with open(file, "r") as address:
        sequence = address.read()
        sequence = sequence.replace("\n", "")
    try:
        return sequence
    except IndexError:
        return "Couldn't open dna sequence file!"



def get_longest_match(sequence, subsequence):
    """Returns length of longest run of subsequence in sequence."""

    # Initialize variables
    longest_run = 0
    subsequence_length = len(subsequence)
    sequence_length = len(sequence)

    # Check each character in sequence for most consecutive runs of subsequence
    for i in range(sequence_length):

        # Initialize count of consecutive runs
        count = 0

        # Check for a subsequence match in a "substring" (a subset of characters) within sequence
        # If a match, move substring to next potential match in sequence
        # Continue moving substring and checking for matches until out of consecutive matches
        while True:

            # Adjust substring start and end
            start = i + count * subsequence_length
            end = start + subsequence_length

            # If there is a match in the substring
            if sequence[start:end] == subsequence:
                count += 1

            # If there is no match in the substring
            else:
                break

        # Update most consecutive matches found
        longest_run = max(longest_run, count)

    # After checking for runs at each character in seqeuence, return longest run found
    return longest_run


def check_database_match(dict, database):
    for person in database:
        matching_sequences = 0
        for key in dict.keys():
            if int(dict[key]) == int(person[key]):
                matching_sequences += 1
        if matching_sequences == len(dict.keys()):
            return person["name"]




if __name__ == "__main__":
    main()
