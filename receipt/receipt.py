import csv
from datetime import datetime
import random

# Constants for column indices
PRODUCT_KEY_COLUMN_INDEX = 0
QUANTITY_INDEX = 1
PRODUCT_NAME_INDEX = 1
PRODUCT_PRICE_INDEX = 2

def read_dictionary(filename, key_column_index):
    # """
    # Read the contents of a CSV file into a compound dictionary and return the dictionary.

    # Parameters:
    #     filename: the name of the CSV file to read.
    #     key_column_index: the index of the column to use as the keys in the dictionary.
    
    # Return:
    #     A compound dictionary that contains the contents of the CSV file.
    # """
    dictionary = {}

    try:
        with open(filename, "rt") as csv_file:
            reader = csv.reader(csv_file)
            next(reader)

            for row_list in reader:
                key = row_list[key_column_index]
                dictionary[key] = row_list
    except FileNotFoundError as file_err:
        # Print an error message if the file is not found
        print(f"{file_err}\n" + f"The file {filename} was not found or the name provided is not correct.")
        return {}
    except KeyError as key_err:
        # Print an error message if the key is not valid
        print(f"{key_err}\n" + f"Error: unknown product ID in the {filename} file\n{key}")
        return {}

    return dictionary

def process_order(requested_product, quantity, products_dict):
    # """
    # Process an order by retrieving product information from the dictionary.

    # Parameters:
    #     requested_product: the product ID requested in the order.
    #     quantity: the quantity of the product in the order.
    #     products_dict: the dictionary containing product information.

    # Return:
    #     A tuple containing product name, quantity, and price.
    # """
    try:
        product_info = products_dict[requested_product]
        name = product_info[PRODUCT_NAME_INDEX]
        price = float(product_info[PRODUCT_PRICE_INDEX])

        return name, quantity, price
    except KeyError:
        # Print an error message if the product ID is unknown
        print(f"Error: unknown product ID in the request.csv file\n{requested_product}")
        return None, None, None

def generate_receipt(items):
    # """
    # Generate and print a receipt based on the provided items.

    # Parameters:
    #     items: a dictionary containing information about the ordered items.
    # """
    total_of_items, subtotal, sales_tax_perc, discount = items['total_of_items'], items['subtotal'], items['sales_tax_perc'], items['discount']
    name, quantity, price = items['name'], items['quantity'], items['price']
    current_date_and_time = items['current_date_and_time']

    print("Inkom Emporium\n")

    for i in range(len(quantity)):
        print(f"{name[i]}: {quantity[i]} ${price[i]:.2f}")

    sales_tax = subtotal * sales_tax_perc
    total = sales_tax + subtotal

    if current_date_and_time.day == 2:
        total = total * discount

    if current_date_and_time.hour < 11:
        total = total * discount

    print(f"\nNumber of Items: {total_of_items}" + f"\nSubtotal: ${subtotal:.2f}" + f"\nSales Tax: ${sales_tax:.2f}" + f"\nTotal: ${total:.2f}")
    print("\nThank you for shopping at the Inkom Emporium.")

    product_coupon = random.choice(name)

    print("\nCoupon for your next purchase:")
    print(f"Get 10% off on {product_coupon}!\n")

    print("We value your feedback!\nPlease complete this online survey to improve our work!\nhttps://www.surveyinkom.com")

def main():
    # Read product information from the CSV file into a dictionary
    products_dict = read_dictionary("products.csv", PRODUCT_KEY_COLUMN_INDEX)

    # Initialize lists to store ordered items information
    ordered_items_names = []
    ordered_items_quantity = []
    ordered_items_price = []
    total_of_items = 0
    subtotal = 0.0
    sales_tax_perc = 6/100
    discount = 1.0/10.0

    try:
        with open("request.csv") as request_file:
            reader = csv.reader(request_file)
            next(reader)

            # Process each row in the request file
            for row in reader:
                requested_product = row[PRODUCT_KEY_COLUMN_INDEX]
                quantity = int(row[QUANTITY_INDEX])

                # Process the order and retrieve product information
                name, quantity, price = process_order(requested_product, quantity, products_dict)

                # Add product information to the lists
                if name is not None:
                    ordered_items_names.append(name)
                    ordered_items_quantity.append(quantity)
                    ordered_items_price.append(price)

                    total_of_items += quantity
                    subtotal += price * quantity

    except FileNotFoundError as file_err:
        # Print an error message if the file is not found
        print(f"{file_err}\n" + f"The file was not found or the name provided is not correct.")

    # Get the current date and time
    current_date_and_time = datetime.now()

    # Create a dictionary with information about the ordered items
    items = {
        'total_of_items': total_of_items,
        'subtotal': subtotal,
        'sales_tax_perc': sales_tax_perc,
        'discount': discount,
        'name': ordered_items_names,
        'quantity': ordered_items_quantity,
        'price': ordered_items_price,
        'current_date_and_time': current_date_and_time
    }

    # Generate and print the receipt
    generate_receipt(items)

if __name__ == "__main__":
    main()