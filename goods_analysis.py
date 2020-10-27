def goods_analysis(*args, in_sale = lambda x: 'молоко' in x['название'].lower()):
    sale = []
    for i in range(len(args)):
        a = args[i]
        if in_sale(a):
            sale.append(a)
    sale = sorted(sale, key=lambda s: s['цена'])
    return sale[0], sale[1], sale[2]

p1, p2, p3 = goods_analysis(
{'название': 'Шоколад молочный', 'цена': 55, 'количество': 100},
{'название': 'Шоколад горький', 'цена': 54, 'количество': 100},
{'название': 'Шоколадное масло', 'цена': 53, 'количество': 100},
{'название': 'Медведь шоколадный', 'цена': 52, 'количество': 100},
{'название': 'Батончик ШОК', 'цена': 51, 'количество': 10},
in_sale=lambda x: x['количество'] > 10
)
print(*sorted([p1, p2, p3], key=lambda x: x['название']), sep='\n')
