class Underscore:
    def map(self, iterable, callback):
        # your code here
    def find(self, iterable, callback):
        # your code here
    def filter(self, iterable, callback):
        # your code
    def reject(self, iterable, callback):
        # your code
# you just created a library with 4 methods!
# let's create an instance of our class
_ = Underscore() # yes we are setting our instance to a variable that is an underscorecopy
evens = _.filter([1, 2, 3, 4, 5, 6], lambda x: x % 2 == 0)
# should return [2, 4, 6] after you finish implementing the code above