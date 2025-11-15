def calculate_due(bill_amount, amount_paid):
    if amount_paid > bill_amount:
        return f"Return to customer: {amount_paid - bill_amount}"
    elif amount_paid == bill_amount:
        return "No due. Bill fully paid."
    else:
        return f"Customer still owes: {bill_amount - amount_paid}"
bill = float(input("Enter the bill amount: "))
paid = float(input("Enter the amount paid: "))
result = calculate_due(bill, paid)
print(result)
