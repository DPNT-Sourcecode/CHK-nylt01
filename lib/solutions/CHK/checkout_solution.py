

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    runningtotal =0

    number_of_A = sum(1 for letter in skus if letter == 'A')
    runningtotal += (number_of_A // 3) * 130 + (number_of_A % 3) * 50

    number_of_B = sum(1 for letter in skus if letter == 'B')
    runningtotal += (number_of_B // 2) * 45 + (number_of_B % 2) * 30

    number_of_C = sum(1 for letter in skus if letter == 'C')
    runningtotal += number_of_C * 20

    number_of_C = sum(1 for letter in skus if letter == 'D')
    runningtotal += number_of_C * 15

    return runningtotal
