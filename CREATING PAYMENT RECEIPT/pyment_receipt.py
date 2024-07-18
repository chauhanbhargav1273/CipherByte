from datetime import datetime

def collect_payment_details():
    payment_details = {}
    payment_details['date'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    payment_details['customer_name'] = input("Enter customer name: ")
    payment_details['amount'] = float(input("Enter amount paid: "))
    payment_details['payment_method'] = input("Enter payment method (e.g., cash, credit card, etc.): ")
    payment_details['transaction_id'] = input("Enter transaction ID: ")
    return payment_details

def format_receipt(payment_details):
    receipt = f"""
    ----------------------------------------
               PAYMENT RECEIPT
    ----------------------------------------
    Date: {payment_details['date']}
    
    Customer Name: {payment_details['customer_name']}
    Amount Paid: ${payment_details['amount']:.2f}
    Payment Method: {payment_details['payment_method']}
    Transaction ID: {payment_details['transaction_id']}
    
    Thank you for your payment!
    ----------------------------------------
    """
    return receipt

def save_receipt_to_file(receipt, filename):
    with open(filename, 'w') as file:
        file.write(receipt)
    print(f"Receipt saved to {filename}")

def main():
    print("Welcome to the Payment Receipt Generator")
    payment_details = collect_payment_details()
    receipt = format_receipt(payment_details)
    print(receipt)
    save_receipt_to_file(receipt, "payment_receipt.txt")

if __name__ == "__main__":
    main()
