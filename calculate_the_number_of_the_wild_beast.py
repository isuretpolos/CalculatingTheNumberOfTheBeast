print("Here comes the calculation of the number of the wild beast.")
perfect_number = 144000
print(f"The perfect number is {perfect_number}.")
one_thousandth = int(perfect_number / 1000)
print(f"One thousandth of it is {one_thousandth}.")
corrupted_number = perfect_number - one_thousandth
print(f"You corrupt the perfect number {perfect_number} by subtracting one thousandth, which results in {corrupted_number}.")
imperfect_number = 7 - 1
print(f"Then you divide it three times by an imperfect number = {imperfect_number}.")
divide_once = int(corrupted_number / imperfect_number)
print(f"{corrupted_number} / {imperfect_number} = {divide_once} ---> which is also 24000 - 24 (again one thousandth).")
divide_twice = int(divide_once / imperfect_number)
print(f"{divide_once} / {imperfect_number} = {divide_twice} ---> which is also 4000 - 4 (again one thousandth).")
divide_thrice = int(divide_twice / imperfect_number)
print(f"{divide_twice} / {imperfect_number} = {divide_thrice} ---> which is also 666.")
print(f"So, the number of the wild beast is calculated exactly like this.")
