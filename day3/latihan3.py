print("""
Welcome to Pizza land!

                     ____
               _,--~~    ~~--._
            ,/'  m%%%%%%=@%%m  `\.
           /' m%%o(_)%%o%%%%o%%m `\\
         /' %%@=%o%%%o%%%o%(_)o%%% `\\
        /  %o%%%%%=@%%%(_)%%o%%@=%%  \\
       |  (_)%(_)%%o%%%o%%%%=@(_)%%%  |
       | %%o%%%%o%%%(_)%%o%%o%%%%o%%% |
       | %%o%(_)%%%%%o%(_)%%%o%%o%o%% |
       |  (_)%%=@%(_)%o%o%%(_)%o(_)%  |
        \ ~%%o%%%%%o%o%=@%%o%%@%%o%~ /
         \. ~o%%(_)%%%o%(_)%%(_)o~ ,/
           \_ ~o%=@%(_)%o%%(_)%~ _/
             `\_~~o%%%o%%%%%~~_/'
                `--..____,,--
""")

bill = 0
order = 0

while order != 15:
    order = int(input(f"""Silahkan pilih pesanan anda
    - Pizza
    1. Super Supreme Chicken Pan Pizza
    2. Super Supreme Chicken Stuffed Crust Pizza Keju
    3. Super Supreme Chicken Stuffed Crust Pizza Sosis
    4. Super Supreme Chicken Crown Crust
    5. Super Supreme Chicken Cheesy Bites
    - Nasi
    6. Black Pepper Chicken
    7. Oriental Chicken
    8. Meatballs - Beef Mushroom Sauce
    - Dessert
    9. Ice Cream Mix 4 Fun
    10. Ice Cream Happy Melody
    - Drink
    11. Green Tea Shake
    12. Green Tea Yakult
    13. Cold Milk Tea
    14. Orange
    Harga pembayaran: RP{bill}
    jika sudah selesai maka masukan angka 15: """))


    if order < 6:
        size = input("pilih ukuran pizza P(personal),R(regular),L(Large): ")
        if size == "P":
            bill += 50000
        elif size == "R":
            bill += 65000
        elif size == "L":
            bill += 85000
    elif order < 9:
        bill += 15000
    elif order < 11:
        bill += 10000
    else:
        bill += 5000

print(f" Total harganya yaitu: Rp{bill}")

