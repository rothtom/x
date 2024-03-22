from cs50 import get_string

def main():
    text = get_string("Text: ").strip()
    letters = count_letters(text)
    words = count_words(text)
    sentences = count_sentences(text)
    l = letters / (words / 100)
    s = sentences / (words / 100)
    readability = 0.0588 * l - 0.296 * s - 15.8
    print(string_grade(readability))


def count_letters(text):
    letters = 0
    for char in text:
        if char.isalpha() == True:
            letters += 1
    return letters




def count_words(text):
    words = 1
    for char in text:
        if char == " ":
            words += 1
    return words



def count_sentences(text):
    sentences = 0
    endings = [".", "?", "!"]
    for i in range(len(endings)):
        for char in text:
            if char == endings[i]:
                sentences += 1

    return sentences


def string_grade(value):
    if value % 1 < 0.5:
        value = value - value % 1
    else:
        value = value + value % 1
    value = int(value)

    if value < 1:
        return "Before Grade 1"
    elif value > 16:
        return "Grade: 16+"
    else:
        return f"Grade: {value}"


if __name__ == "__main__":
    main()

