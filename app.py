from flask import Flask

app = Flask(__name__)

def convert(decimal_num):
    roman = {1000:'M', 900:'CM', 500:'D', 400:'CD', 100:'C', 90:'XC', 50:'L', 40:'XL', 10:'X', 9:'IX', 5:'V', 4:'IV', 1:'I'}

    num_to_roman=''
    for i in roman.keys():
        num_to_roman += roman[i] * (decimal_num // i)
        decimal_num %= i

    return num_to_roman


print('3 -- ', convert(3))
print('9 -- ', convert(9))
print('58 -- ', convert(58))
print('1994 -- ', convert(1994))
print('3500 -- ', convert(3500))

