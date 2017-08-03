
def currency_converter(amount):
    # create empty dict
    currency_dict = {
        "penny": 0,
        "nickel": 0,
        "dime": 0,
        "quarter": 0,
        "$1": 0,
        "$5": 0,
        "$10": 0,
        "$50": 0,
        "$100": 0,
    }

    # calculate combo needed to equal amount
    i = amount*100
    while i > 0:
        if i - 10000 > 0:
            currency_dict["$100"] += 1
            i -= 10000
        elif i - 5000 > 0:
            currency_dict["$50"] += 1
            i -= 5000
        elif i - 1000 > 0:
            currency_dict["$10"] += 1
            i -= 1000
        elif i - 500 > 0:
            currency_dict["$5"] += 1
            i -= 500
        elif i - 100 > 0:
            currency_dict["$1"] += 1
            i -= 100
        elif i - 25 > 0:
            currency_dict["quarter"] += 1
            i -= 25
        elif i - 10 > 0:
            currency_dict["dime"] += 1
            i -= 10
        elif i - 5 > 0:
            currency_dict["nickel"] += 1
            i -= 5
        elif i - 1 >= 0:
            currency_dict["penny"] += 1
            i -= 1 

    # remove 0 value dict items
    for j,v in list(currency_dict.items()):
        if v == 0:
            del currency_dict[j]
    
    # print problem solutions
    for k,x in list(currency_dict.items()):
        print(x, k)

currency_converter(12.33)