import pudb

class CreditCard:
    def __init__(self, card_number):
        self.card_number = card_number
        self.card_type = "a string"
        self.valid = False
        self.determine_card_type()
        self.check_length()
        self.validate()

# Create and add your method called `determine_card_type` to the CreditCard class here:
    def determine_card_type(self):
        card_number = self.card_number
        if card_number[0] == "4":
            self.card_type = "VISA"
            return self.card_type
        elif card_number[0:2] == "51" or card_number[0:2] == "52" or card_number[0:2] == "53" or card_number[0:2] == "54" or card_number[0:2] == "55":
            self.card_type = "MASTERCARD"
            return self.card_type
        elif card_number[0:2] == "34" or card_number[0:2] == "37":
            self.card_type = "AMEX"
            return self.card_type
        elif card_number[0:4] == "6011":
            self.card_type = "DISCOVER"
            return self.card_type
        else:
            self.card_type = "INVALID"
            return self.card_type

# Create and add your method called `check_length` to the CreditCard class here:
    def check_length(self):
        if self.card_type != "INVALID":    
            if len(self.card_number) == 16 and self.card_type == "VISA" or self.card_type == "MASTERCARD" or self.card_type == "DISCOVER":
                self.valid = True
                return self.valid
            elif len(self.card_number) == 15 and self.card_type == "AMEX":
                self.valid = True
                return self.valid

# Create and add your method called 'validate' to the CreditCard class here:
    def validate(self):
        if self.valid == True:
            card_number = self.card_number
            card_number = list(card_number)
            for i in range(0,len(card_number)):
                card_number[i] = int(card_number[i])
            j = len(card_number) - 2
            while j >= 0:
                card_number[j] *= 2
                j -= 2
            card_number = ' '.join(str(e) for e in card_number)
            card_number = card_number.replace(" ","")
            card_number = list(card_number)
            for k in range(0,len(card_number)):
                card_number[k] = int(card_number[k])
            x = card_number[0]
            for l in range(1,len(card_number)):
                x += card_number[l]
            if x % 10 == 0:
                self.valid = True
                return self.valid
            else:
                self.valid = False
                self.card_type = "INVALID"
                return self.valid
                return self.card_type
        else:
            self.card_type = "INVALID"
            return self.card_type


#do not modify assert statements
cc = CreditCard('9999999999999999')

assert cc.valid == False, "Credit Card number cannot start with 9"
assert cc.card_type == "INVALID", "99... card type is INVALID"

cc = CreditCard('4440')

assert cc.valid == False, "4440 is too short to be valid"
assert cc.card_type == "INVALID", "4440 card type is INVALID"

cc = CreditCard('5515460934365316')

assert cc.valid == True, "Mastercard is Valid"
assert cc.card_type == "MASTERCARD", "card_type is MASTERCARD"

cc = CreditCard('6011053711075799')

assert cc.valid == True, "Discover Card is Valid"
assert cc.card_type == "DISCOVER", "card_type is DISCOVER"

cc = CreditCard('379179199857686')

assert cc.valid == True, "AMEX is Valid"
assert cc.card_type == "AMEX", "card_type is AMEX"

cc = CreditCard('4929896355493470')

assert cc.valid == True, "Visa Card is Valid"
assert cc.card_type == "VISA", "card_type is VISA"

cc = CreditCard('4329876355493470')

assert cc.valid == False, "This card does not meet mod10"
assert cc.card_type == "INVALID", "card_type is INVALID"

cc = CreditCard('339179199857685')

assert cc.valid == False, "Validates mod10, but invalid starting numbers for AMEX"
assert cc.card_type == "INVALID", "card_type is INVALID"
