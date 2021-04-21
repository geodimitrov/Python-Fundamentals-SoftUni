import re

EXPRESSION = r"@#+([A-Z][a-zA-Z0-9]{4,}[A-Z])@#+$"
def read_input(n):
    result = []

    for _ in range(n):
        result.append(input())

    return result

def validate_barcodes(barcodes_data):
    barcodes = []

    for el in barcodes_data:
        match = re.search(EXPRESSION, el)

        if match:
            barcode = match.group()
        else:
            barcode = None

        barcodes.append(barcode)

    return barcodes

def get_product_group(barcode):
    group = ""

    for char in barcode:
        if char.isdigit():
            group += char

    if not group:
        group = "00"

    return group

def print_result(barcodes):
    for barcode in barcodes:
        if not barcode:
            print("Invalid barcode")
        else:
            product_group = get_product_group(barcode)
            print(f"Product group: {product_group}")

n = int(input())
barcodes_data = read_input(n)
barcodes = validate_barcodes(barcodes_data)
print_result(barcodes)