def get_expense():
    while True:
        user_input = input("Enter an expense amount (or type 'done' to finish): ").strip()
        if user_input.lower() == "done":
            return None
        try:
            amount = float(user_input)
            if amount < 0:
                print("Expense amount cannot be negative.")
                continue
            return amount
        except ValueError:
            print("Please enter a valid number.")


def main():
    print("===== EXPENSE TRACKER =====")

    total = 0
    expense_count = 0

    while True:
        expense = get_expense()
        if expense is None:
            break

        total = total + expense
        expense_count += 1
        print(f"Added expense: {expense:.2f} | Running Total: {total:.2f}")

    print("\n===== SUMMARY =====")
    print(f"Total Expenses Entered: {expense_count}")
    print(f"Total Spent: {total:.2f}")


if __name__ == "__main__":
    main()