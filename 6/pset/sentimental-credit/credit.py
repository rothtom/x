import re
import sys

def main():
    card_num = get_card_num()
    valid = validate(card_num)
    if valid == False:
        sys.exit("Invaid!")
    #print(get_type(card_num))


def get_card_num():
    num = input("card number: ")

    if num_passed := re.search(r"([0-9]{13})([0-9]{2,3})?", num):
        return num

    get_card_num()


def validate(num):
    second = []
    for digit in range(len(str(num))):
        try:
            second.append(int(num[(-(digit + 1) * 2)]))
        except IndexError:
            break

    sum1 = 0
    for digit in second:
        digit = digit * 2
        if digit >= 10:
            sum1 += 1
        sum1 += digit % 10


    other = []
    for digit in range(len(str(num))):
        try:
            print(num[((digit + 1) * 2)])
            other.append(int(num[((digit + 1) * 2)]))
        except IndexError:
            break

    sum2 = 0
    for digit in other:
        sum2 += digit

    total = sum1 + sum2
    print(f"sum1 = {sum1}, sum2 = {sum2}, total = {total}")
    print(total % 10)
    if (sum1 + sum2) % 10 == 0:
        print("YES")
        return True

    else:
        return False


def get_type(num):
    if num[:1] in [[3, 4], [3, 7]]:
        return "AMEX"
    elif num[:1] in [51, 52, 53, 54, 55]:
        return "MASTERCARD"
    elif num[1] != 4:
        return "INVALID"
    else:
        return "VISA"



if __name__ == "__main__":
    main()
