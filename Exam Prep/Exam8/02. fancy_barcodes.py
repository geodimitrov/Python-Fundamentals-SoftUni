import re

EXPRESSION = "^@#+[a-zA-Z0-9]+@#+"
SPLIT_EX = "[@#+@#+]"

def is_valid(barcode):


def process_barcodes(barcodes):
    for barcode in barcodes:
        if not is_valid(barcode):
            print("Invalid barcode")

barcodes = [
    "@#FreshFisH@#",
    "@###Brea0D@###",
    "@##Che4s6E@##"
]

n = 3
process_barcodes(barcodes)