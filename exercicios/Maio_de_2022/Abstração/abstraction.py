class AdvancedArithmetic(object):
    def divisorSum(number):
        raise NotImplementedError

class Calculator(AdvancedArithmetic):
    def divisorSum(self, number):
        result = []
        for indice in range(1, number + 1):
            if number % indice == 0:
                result.append(indice)
        return sum(result)

number = int(input())
my_calculator = Calculator()
sum_numbers = my_calculator.divisorSum(number)
print("I implemented: " + type(my_calculator).__bases__[0].__name__)
print(sum_numbers)