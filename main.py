class Kalkulyator:
    def __init__(self):
        self.history = []

    def add(self, a, b):
        result = a + b
        self.history.append(f"{a} + {b} = {result}")
        return result

    def subtract(self, a, b):
        result = a - b
        self.history.append(f"{a} - {b} = {result}")
        return result

    def multiply(self, a, b):
        result = a * b
        self.history.append(f"{a} * {b} = {result}")
        return result

    def divide(self, a, b):
        if b == 0:
            raise ZeroDivisionError
        result = a / b
        self.history.append(f"{a} / {b} = {result}")
        return result

    def power(self, a, b):
        result = a ** b
        self.history.append(f"{a} ** {b} = {result}")
        return result

    def print_history(self):
        for i, history in enumerate(self.history, start=1):
            print(f"{i}. {history}")

def main():
    kalkulyator = Kalkulyator()
    while True:
        print("\nKalkulyator\n1. Qo'shish\n2. Ayirish\n3. Ko'paytirish\n4. Bo'lish\n5. Daraja\n6. Tarix\n7. Chiqish")
        choice = input("Tanlang: ")
        if choice == "1":
            a = float(input("A = "))
            b = float(input("B = "))
            print(f"{a} + {b} = {kalkulyator.add(a, b)}")
        elif choice == "2":
            a = float(input("A = "))
            b = float(input("B = "))
            print(f"{a} - {b} = {kalkulyator.subtract(a, b)}")
        elif choice == "3":
            a = float(input("A = "))
            b = float(input("B = "))
            print(f"{a} * {b} = {kalkulyator.multiply(a, b)}")
        elif choice == "4":
            a = float(input("A = "))
            b = float(input("B = "))
            try:
                print(f"{a} / {b} = {kalkulyator.divide(a, b)}")
            except ZeroDivisionError:
                print("B = 0 ga bo'lish mumkin emas!")
        elif choice == "5":
            a = float(input("A = "))
            b = float(input("B = "))
            print(f"{a} ** {b} = {kalkulyator.power(a, b)}")
        elif choice == "6":
            kalkulyator.print_history()
        elif choice == "7":
            break
        else:
            print("Noto'g'ri tanlov!")

if __name__ == "__main__":
    main()