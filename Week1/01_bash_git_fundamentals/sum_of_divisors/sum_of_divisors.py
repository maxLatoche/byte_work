import pudb

class Divisor:

    def __init__(self, num):
        self.num = num
        self.divisors = []
        self.find_divisors()
        self.sum_of_divisors()

    def find_divisors(self):
        divisors = self.divisors
        num = self.num
        for i in range(1,num+1):
            if num % i == 0:
                divisors.append(i)

    def sum_of_divisors(self):
        divisors = self.divisors
        i = 0
        for j in range(0,len(divisors)):
            i += divisors[j]
        sum_total = i
        print(divisors,"\n",sum_total,"\n",len(divisors))

divisor = Divisor(60)