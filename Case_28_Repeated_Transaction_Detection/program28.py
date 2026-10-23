n = int(input("Enter number of transactions: "))

transactions = []
repeated = []

for i in range(n):
    transaction_id = input("Enter transaction ID: ")

    if transaction_id in transactions:
        if transaction_id not in repeated:
            repeated.append(transaction_id)
    else:
        transactions.append(transaction_id)

print("\n===== TRANSACTION AUDIT REPORT =====")

if len(repeated) == 0:
    print("No repeated transactions found.")
else:
    print("Repeated transaction IDs:")
    for transaction_id in repeated:
        print(transaction_id)