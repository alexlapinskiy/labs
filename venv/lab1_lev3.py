number=input("Input last 3 digits of the scoring book: ")
def convert_base(num, to_base=10, from_base=10):
    # first convert to decimal number
    if isinstance(num, str):
        n = int(num, from_base)
    else:
        n = int(num)
    # now convert decimal to 'to_base' base
    alphabet = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    if n < to_base:
        return alphabet[n]
    else:
        return convert_base(n // to_base, to_base) + alphabet[n % to_base]
print(number," in decimal -> ",convert_base(number, from_base=8, to_base=10))
print(number,"in binary -> ",convert_base(number, from_base=8, to_base=2))
print(number,"in hex -> ",convert_base(number, from_base=8, to_base=16))


