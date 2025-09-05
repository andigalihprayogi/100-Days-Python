import math

# menghitung berapa banyak ember cat yang digunakan untuk luasan dari dinding
def paint_calc(h, w, cover):
    number_of_cons = math.ceil((h * w)/cover)
    return print(f"you need {number_of_cons} cans")


test_h = int(input("input height (m):"))
test_w = int(input("input weidth (m):"))
coverage = 5
paint_calc(h=test_h, w=test_w, cover=coverage)
