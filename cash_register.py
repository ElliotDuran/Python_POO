#!/usr/bin/env python

class CashRegister():
    """ A simple class that represents the contents of a cash register """

    def __init__(self, name, dollars, quartes, dimes):
        if is_number(dollars) and is_number(quartes) and is_number(dimes):
            self.dollars = dollars
            self.quartes = quartes
            self.dimes = dimes
        else:
            raise TypeError("Only numbers")

        if not_empty_string(name):
            self.name = name
        else:
            raise ValueError("Empty String")

    def total(self):
        return (self.dimes * 0.1) + (self.quartes * 0.25) + self.dollars

    def __gt__(self, other):
        return self.total() > other.total()

    def __str__(self):
        return self.name + ": there are " + str(self.dollars) + " dollars, " + \
                str(self.quartes) + " quarters and " + str(self.dimes) + \
                " dimes."


def is_number(value):
    return isinstance(value, (int, float))


def not_empty_string(string):
    if len(string) is not 0:
        return True


if __name__ == "__main__":
    c1 = CashRegister("Cash register 01", 4, 7, 4)      # $5.15
    c2 = CashRegister("Cash register 02", 3, 11, 8)     # $6.55
    c3 = CashRegister("Cash register 03", 10, 1, 2)     # $10.45
    c4 = CashRegister("Cash register 04", 2, 6, 1)      # $3.60
    c5 = CashRegister("Cash register 05", 13, 9, 14)     # $10.9
    
    cash_list = [c1, c2, c3, c4, c5]
    sorted_cash_list = sorted(cash_list)

    for i in sorted_cash_list:
        print(i)