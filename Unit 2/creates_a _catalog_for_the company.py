def create_catalog():
    item1_price = 200.0
    item2_price = 400.0
    item3_price = 600.0

    combo1_price = (item1_price + item2_price) * 0.9
    combo2_price = (item2_price + item3_price) * 0.9
    combo3_price = (item1_price + item3_price) * 0.9
    gift_pack_price = (item1_price + item2_price + item3_price) * 0.75

    catalog = "Online Store\n"
    catalog += "-------------------------\n"
    catalog += "Product (S)\t\t\tprice\n"
    catalog += "Item 1\t\t\t\t{:.1f}\n".format(item1_price)
    catalog += "Item 2\t\t\t\t{:.1f}\n".format(item2_price)
    catalog += "Item 3\t\t\t\t{:.1f}\n".format(item3_price)
    catalog += "\n"
    catalog += "Combo 1(Item 1 + 2)\t\t{:.1f}\n".format(combo1_price)
    catalog += "Combo 2(Item 2 + 3)\t\t{:.1f}\n".format(combo2_price)
    catalog += "Combo 3(Item 1 + 3)\t\t{:.1f}\n".format(combo3_price)
    catalog += "Combo 4(Item 1 + 2 + 3)\t\t{:.1f}\n".format(gift_pack_price)
    catalog += "--------------------------------------------\n"
    catalog += "For delivery Contact : 98764678899"

    return catalog

catalog = create_catalog()

print(catalog)
