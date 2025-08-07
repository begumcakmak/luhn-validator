def verify_card_number(card_number):
    if not card_number.isdigit():
        return False

    sum_of_odd_digits=0
    reversed_card_number=card_number[::-1]
    odd_digits=reversed_card_number[::2]
    for digit in odd_digits:
        sum_of_odd_digits+=int(digit)
    sum_of_even_digits=0
    even_digits=reversed_card_number[1::2]
    for digit in even_digits:
        if int(digit)*2>=10:
            digit=int(digit)*2
            sum_of_even_digits+=int(digit)//10+int(digit)%10
        else:
            sum_of_even_digits+=int(digit)*2
    if (sum_of_odd_digits+sum_of_even_digits)%10==0:
        return True
    return False
def main():
    while True:
        card_number=input("Enter card number (or type 'exit' to quit): ")
        if card_number.lower()=="exit":
            break
        card_translation=str.maketrans({"-":""," ":""})
        translated_card_number=card_number.translate(card_translation)
        if verify_card_number(translated_card_number):
            print("VALID!")
        else:
            print("INVALID!")
        

main()
