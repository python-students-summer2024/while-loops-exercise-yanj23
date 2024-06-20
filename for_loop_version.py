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
    for updated_beer_count in range(int(user_num_beer), 0, -1):
        if int(updated_beer_count) > 2:
            print(f"{updated_beer_count} bottles of beer on the wall, {updated_beer_count} bottles of beer.\nTake one down, pass it around, {int(updated_beer_count) - 1} bottles of beer on the wall.\n")
        elif int(updated_beer_count) ==2:
            print(f"{updated_beer_count} bottles of beer on the wall, {updated_beer_count} bottles of beer.\nTake one down, pass it around, {int(updated_beer_count) - 1} bottle of beer on the wall.\n")
        else:
            print(f"{updated_beer_count} bottle of beer on the wall, {updated_beer_count} bottle of beer.\nTake it down, pass it around, no more bottles of beer on the wall!")