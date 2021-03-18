# foods = ['Pasta', 'Curry', 'Sushi']

# for food in foods:
#     print('好きな食べ物は ' + food + ' です')


# fruits = {'apple': 'red', 'banana': 'yellow', 'grape': 'purple'}

# for fruit in fruits:
#     print(fruit + ' の色は ' + fruits[fruit]+ ' です')

foods = {'Pasta': 800, 'Curry': 600, 'Sushi': 1000}

for food in foods:
    print('--------------------')
    print(food + 'は'  +str(foods[food]) +'円です。')

    input_count = input('購入する' + food + 'の個数を入力してください。')
    print('購入する' + food + 'の数は、 '+ input_count + ' 個です')

    count = int(input_count)

    food_price = foods[food] * count

    print('支払金額は' + str(food_price)+ '円です。')
    
