# Process shopping cart with discounts

cart = [("Lime", 1.2, 3), ("Butter", 2.5, 1), ("Bun", 1.8, 2)]
total = 0.0
discount_threshold = 10

print("Receipt:")
for item in cart:
    name, price, quantity = item
    subtotal = price * quantity
    total += subtotal
    print(f"- {name} x{quantity}: ${subtotal:.2f}")

if total > discount_threshold:
    discount = total * 0.1
    total -= discount
    print(f"Discount applied: -${discount:.2f}")

print(f"Total due: ${total:.2f}")