def goods_analysis(*args,
                   in_sale=lambda x: 'молоко' in x['название'].lower()):
    sale = []
    for i in range(len(args)):
        a = args[i]
        if in_sale(a):
            sale.append(a)
    sale = sorted(sale, key=lambda s: s['цена'])
    return sale[0], sale[1], sale[2]
