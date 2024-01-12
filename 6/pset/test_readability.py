from readability import count_letters, count_words, count_sentences


def main():
    test_count_letters()
    test_count_words()
    test_count_sentences()


def test_count_letters():
    assert count_letters("ABC") == 3
    assert count_letters("A B") == 2
    assert count_letters("") == 0


def test_count_words():
    assert count_words("Word1 word2 word3") == 3
    assert count_words("Word1. a. word3") == 3


def test_count_sentences():
    assert count_sentences("Sentence1. Sentence2! Sentence3?") == 3

if __name__ == "__main__":
    main()
