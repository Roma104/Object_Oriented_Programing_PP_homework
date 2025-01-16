from account import BankAccount


def main():
    my_account = BankAccount(account_number="12 3456 5555 9090 1111 0000 7722")
    print("Initial Account Balance:")
    my_account.display_account_info()
    print()

    my_account.deposit(25.30)
    print("Account Balance After Deposit:")
    my_account.display_account_info()
    print()

    my_account.withdraw(31.70)
    print("Account Balance After First Withdrawal:")
    my_account.display_account_info()
    print()

    my_account.withdraw(14)
    print("Final Account Balance:")
    my_account.display_account_info()


if __name__ == "__main__":
    main()