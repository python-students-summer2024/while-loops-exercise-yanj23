def get_starting_number():
    is_integer = 0
    while is_integer < 1:
        user_num_beer = input("How many bottles of beer on the wall? ")
        if user_num_beer.isnumeric() is False:
            is_integer = 0
        elif int(user_num_beer) < 1:
            is_integer = 0
        else:
            is_integer = 1
            return user_num_beer

def sing(user_num_beer):
    current_beer = int(user_num_beer)
    flag = True
    while flag:
        if current_beer > 2:
            print(f"{current_beer} bottles of beer on the wall, {current_beer} bottles of beer.\nTake one down, pass it around, {int(current_beer) - 1} bottles of beer on the wall.\n")
            current_beer = current_beer - 1
        elif int(current_beer) ==2:
            print(f"{current_beer} bottles of beer on the wall, {current_beer} bottles of beer.\nTake one down, pass it around, {int(current_beer) - 1} bottle of beer on the wall.\n")
            current_beer = current_beer - 1
        else:
            print(f"{current_beer} bottle of beer on the wall, {current_beer} bottle of beer.\nTake it down, pass it around, no more bottles of beer on the wall!")
            flag = False