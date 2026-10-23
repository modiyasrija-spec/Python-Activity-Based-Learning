n = int(input("Enter number of products: "))

products = []

for i in range(n):
    print("\nProduct", i + 1)

    name = input("Enter product name: ")
    opening = int(input("Enter opening stock: "))
    incoming = int(input("Enter incoming quantity: "))
    dispatched = int(input("Enter dispatched quantity: "))
    closing = int(input("Enter actual closing stock: "))

    expected = opening + incoming - dispatched
    discrepancy = closing - expected

    if expected < 0:
        status = "Invalid stock movement"
        replenishment = 0
    elif discrepancy != 0:
        status = "Stock discrepancy detected"
        replenishment = max(0, -discrepancy)
    else:
        status = "Stock reconciled"
        replenishment = 0

    products.append(
        (name, opening, incoming, dispatched, closing,
         expected, discrepancy, status, replenishment)
    )

print("\n===== INVENTORY RECONCILIATION REPORT =====")

for product in products:
    name, opening, incoming, dispatched, closing, expected, discrepancy, status, replenishment = product

    print("\nProduct:", name)
    print("Expected closing stock:", expected)
    print("Actual closing stock:", closing)
    print("Discrepancy:", discrepancy)
    print("Status:", status)
    print("Replenishment required:", replenishment)