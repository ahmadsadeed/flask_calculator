
class Operation:
    def __init__(self, a, b, op):
        self.result = None
        self.a = a
        self.b = b
        self.op = op

    def operate(self):
        try:
            self.a = float(self.a)
            self.b = float(self.b)

            if self.op == "+":
                self.result = self.a + self.b
            elif self.op == "-":
                self.result = self.a - self.b
            elif self.op == "/":
                self.result = self.a / self.b
            else:
                self.result = self.a * self.b
        except ZeroDivisionError:
            raise ZeroDivisionError
        except ValueError:
            raise ValueError
