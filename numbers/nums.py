
class Number:
    def __init__(self, number: int):
        self.number = number

    # Basically, can the number be read the same backwards and forwards
    # I take a string version of the number and compare it to a reverse
    # List of itself. In retrospect, does the number string equal the
    # number list string in reverse and if so, then it's a palindrome
    def is_number_palindrome(self):
        return str(self.number) == str(self.number)[::-1]

    # Is the number a prime? (divisible by 2). Take a number. If the number
    # is '1' or odd, then it is not divisible by 2 else, it is prime
    def is_number_prime(self):
        if self.number == 1:
            return False
        for i in range(2, self.number):
            if self.number % i == 0:
                return False
        return True