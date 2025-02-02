from MoneyExchange.MoneyExchange import MoneyExchange
class MoneyExchange:
    def __init__(self):
        self.exchange = MoneyExchange()

    def menu_display(self):
        choice = -1
        while not 1 <= choice <= 7:
            print("Money Exchanger")
            print("1. Convert SG($)")
            print("2. Convert SG($)")
            print("3. Convert SG($)")
            print("4. Convert --- to SG($)")
            print("5. Convert --- to SG($)")
            print("6. Convert --- to SG($)")
            print("7. end")

            if not 1 <= choice <= 5:
                print("Invalid, please reenter")
        return
    
    def main(self):
        choice = self.menu_display()

        while choice != 7:
            if choice == 1:
                conv = input("Enter SG amount: ")

            elif choice == 2:
                conv = input("Enter SG amount: ")

            elif choice == 3:
                conv = input("Enter SG amount: ")

            elif choice == 4:
                cnv = input("Enter amount to be converted to SG ($): ")

            elif choice == 5:
                cnv = input("Enter amount to be converted to SG ($): ")

            elif choice == 6:
                cnv = input("Enter amount to be converted to SG ($): ") 
            else:
                print("Invalid choice")

            choice = self.menu_display()


if __name__ == "__menu_display":
    app = MoneyExchange()
    app.main()