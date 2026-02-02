z1 = 2 + 3j
z2 = 1 + 4j
sum_z = z1 + z2
product_z = z1 * z2
log = f"Sum: {sum_z}, Product: {product_z}".encode("utf-8")
if isinstance(log, bytes):
    print("Operations successful.")
    print("Log:", log)
else:
    print("Logging failed.")