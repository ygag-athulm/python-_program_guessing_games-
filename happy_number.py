def  happy_number_game():
    num = int(input("Enter the digit"))
    while num >= 10:
        digits = [int(dig) ** 2 for dig in str(num)]
        num = sum(digits)
    if num ==1:
        return True
    else:
        return False


print(happy_number_game())

