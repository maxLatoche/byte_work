import pudb
import fractions

class Totative:

    def __init__(self, num):
        self.num = num
        self.totatives = []
        self.find_totatives()
        self.sum_of_totatives()

    def find_totatives(self):
        totatives = self.totatives
        num = self.num
        i = 0
        while i < num:
            gcd = fractions.gcd(i,num)
            if gcd == 1:
                totatives.append(i)
            i += 1

    def sum_of_totatives(self):
        totatives = self.totatives
        i = 0
        for j in range(0,len(totatives)):
            i += totatives[j]
        totient = i
        print(totatives,"\n",totient,"\n",len(totatives))

totative = Totative(60)