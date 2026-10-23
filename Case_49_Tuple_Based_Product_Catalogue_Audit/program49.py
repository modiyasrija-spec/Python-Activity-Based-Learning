# Case Study 49: Tuple-Based Product Catalogue Audit

n = int(input("Enter number of products: "))

products = []

for i in range(n):
    print("\nProduct", i + 1)

    product_id = input("Enter product ID: ")
    name = input("Enter product name: ")
    price = float(input("Enter product price: "))
    stock = int(input("Enter stock quantity: "))

    products.append((product_id, name, price, stock))

print("\n===== PRODUCT CATALOGUE AUDIT =====")

if len(products) == 0:
    print("No products available for audit.")
else:
    seen_ids = []
    duplicate_ids = []
    low_stock = []

    for product in products:
        product_id, name, price, stock = product

        if product_id in seen_ids:
            if product_id not in duplicate_ids:
                duplicate_ids.append(product_id)
        else:
            seen_ids.append(product_id)

        if stock < 5:
            low_stock.append((product_id, name, stock))

    print("\nTotal product records:", len(products))

    if len(duplicate_ids) == 0:
        print("Duplicate product IDs: None")
    else:
        print("Duplicate product IDs:", duplicate_ids)

    if len(low_stock) == 0:
        print("Low-stock products: None")
    else:
        print("\nLow-stock products:")
        for item in low_stock:
            product_id, name, stock = item
            print(product_id, "-", name, "- Stock:", stock)

    print("\nComplete catalogue:")
    for product in products:
        product_id, name, price, stock = product
        print(product_id, name, "Price:", price, "Stock:", stock)