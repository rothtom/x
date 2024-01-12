from dna import check_database_match


def main():
    test_check_database_match()


def test_check_database_match():
    assert check_database_match({"AA": 1}, [{"name": "Bob", "AA": 1}]) == "Bob"
    assert check_database_match({"AA": 2}, [{"name": "Bob", "AA": 1}]) == None
