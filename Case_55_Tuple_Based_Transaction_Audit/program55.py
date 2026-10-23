# Case Study 55: Tuple-Based Transaction Audit

n = int(input("Enter number of transactions: "))

transactions = []

for i in range(n):
    print("\nTransaction", i + 1)

    transaction_id = input("Enter transaction ID: ")
    amount = float(input("Enter transaction amount: "))
    transaction_type = input("Enter type (Credit/Debit): ").strip().lower()

    transactions.append((transaction_id, amount, transaction_type))

print("\n===== TRANSACTION AUDIT REPORT =====")

if len(transactions) == 0:
    print("No transactions available for audit.")
else:
    total_credit = 0
    total_debit = 0
    seen_ids = []
    duplicate_ids = []

    for transaction in transactions:
        transaction_id, amount, transaction_type = transaction

        if transaction_id in seen_ids:
            if transaction_id not in duplicate_ids:
                duplicate_ids.append(transaction_id)
        else:
            seen_ids.append(transaction_id)

        if transaction_type == "credit":
            total_credit += amount
        elif transaction_type == "debit":
            total_debit += amount

    print("Total transactions:", len(transactions))
    print(f"Total credits: {total_credit:.2f}")
    print(f"Total debits: {total_debit:.2f}")
    print(f"Net balance change: {total_credit - total_debit:.2f}")

    if len(duplicate_ids) == 0:
        print("Duplicate transaction IDs: None")
    else:
        print("Duplicate transaction IDs:", duplicate_ids)

    print("\nComplete transaction list:")
    for transaction in transactions:
        transaction_id, amount, transaction_type = transaction
        print(transaction_id, amount, transaction_type.title())