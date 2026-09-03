
#diff match menu vs if -> if
# match case -> design pattern  
#match case
#branch
#subbranch
#food name
#price
#description
#منو بنویسید 5 تا منو داشته باشه اول کافه دوم رستوران سوم فست فود چهارم بار پنجم گیم برد و اگزیت
print("welcom to chakavak cafe house")
print("cafe and resturant")

while True:

    menu = input("1.coffee bar 2.italian 3.persian 4.bar 5.gameboard 6.exit:")
    while True:
        match menu:
            case "1":
                menu_cafe=input("1.latte 350 2.cake 300 3.tea 100 4.exit:")
                match menu_cafe:
                    case"1":
                        num_latte=int(input("how many?"))
                        price_latte = num_latte * 350 
                        price_latte_tax = price_latte * 1.1
                        print("late----350")
                        print(price_latte)
                    case"2":
                        num_cake=int(input("how many?"))
                        price_cake = num_cake * 300 
                        price_cake_tax = price_cake * 1.1
                        print("cake----300")
                        print(price_cake)
                    case"3":
                        num_tea=int(input("how many?"))
                        price_tea = num_tea * 100 
                        price_tea_tax = price_tea * 1.1
                        print("tea----100")
                        print(price_tea)
                    case _:
                        break 
            
            case"2":
                menu_italian=input("1.pizza 450 2.pasta 550 3.sandwich 650 4.exit:")
                match menu_italian:
                    case"1":
                        num_pizza=int(input("how many?"))
                        price_pizza = num_pizza * 450 
                        price_pizza_tax = price_pizza * 1.1
                        print("pizza----450")
                        print(price_pizza)
                    case"2":
                        num_pasta=int(input("how many?"))
                        price_pasta = num_pasta * 550 
                        price_pasta_tax = price_pasta * 1.1
                        print("pasta----550")
                        print(price_pasta)
                    case"3":
                        num_sandwich=int(input("how many?"))
                        price_sandwich = num_sandwich * 650 
                        price_sandwich_tax = price_sandwich * 1.1
                        print("sandwich----650")
                        print(price_sandwich)
                    case _:
                        break
            case"3":
                menu_persian=input("1.polo 500 2.kabab 800 3.khoresh 650 4.salad 350  5.exit:")
                match menu_persian:
                    case"1":
                        num_polo=int(input("how many?"))
                        price_polo = num_polo * 500 
                        price_polo_tax = price_polo * 1.1
                        print("polo----500")
                        print(price_polo)
                    case"2":
                        num_kabab=int(input("how many?"))
                        price_kabab = num_kabab * 800 
                        price_kabab_tax = price_kabab * 1.1
                        print("kabab----800")
                        print(price_kabab)
                    case"3":
                        num_khoresh=int(input("how many?"))
                        price_khoresh = num_khoresh * 650 
                        price_khoresh_tax = price_khoresh * 1.1
                        print("khoresh----650")
                        print(price_khoresh)
                    case"4":
                        num_salad=int(input("how many?"))
                        price_salad = num_salad * 350 
                        price_salad_tax = price_salad * 1.1
                        print("salad----350")
                        print(price_salad)
                    case _:
                        break
            case"4":
                menu_bar=input("1.bear 100 2.white wine 200 3.red wine 200 4.vodka 300  5.exit:")
                match menu_bar:
                    case"1":
                        num_bear=int(input("how many?"))
                        price_bear = num_polo * 100 
                        price_bear_tax = price_bear * 1.1
                        print("bear----100")
                        print(price_bear)
                    case"2":
                        num_whitewine=int(input("how many?"))
                        price_whitewine = num_whitewine * 200 
                        price_whitewine_tax = price_whitewine * 1.1
                        print("whitewine----200")
                        print(price_whitewine)   
                    case"3":
                        num_redwine=int(input("how many?"))
                        price_redwine = num_redwine * 200 
                        price_redwine_tax = price_redwine * 1.1
                        print("redwine----650")
                        print(price_redwine)
                    case"4":
                        num_vodka=int(input("how many?"))
                        price_vodka = num_vodka * 300 
                        price_vodka_tax = price_vodka * 1.1
                        print("vodka----300")
                        print(price_vodka)
                    case _:
                        break   
            case"5":
                menu_gameboard=input("1.lodo 100 2.monopoly 200 3.onu 200 4.exit:")
                match menu_gameboard:
                    case"1":
                        num_lodo=int(input("how many?"))
                        price_lodo = num_lodo * 100 
                        price_lodo_tax = price_lodo * 1.1
                        print("lodo----100")
                        print(price_lodo)
                    case"2":
                        num_whitewine=int(input("how many?"))
                        price_whitewine = num_whitewine * 200 
                        price_whitewine_tax = price_whitewine * 1.1
                        print("whitewine----200")
                        print(price_whitewine)
            case _:
                break
    
    break


