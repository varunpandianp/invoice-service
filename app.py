def calculate_invoice(subtotal, tax_rate):
    tax = subtotal * tax_rate / 100
    total = subtotal + tax
    return total

def format_currency(amount):
    return f"₹{amount:,.2f}"

print(format_currency(invoice_total))

invoice_total = calculate_invoice(1000, 18)

print(f"Invoice Total : {invoice_total}")
