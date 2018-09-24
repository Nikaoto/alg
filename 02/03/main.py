# - signed magnitude - MSB denotes sign (1 is negative, 0 positive)
# - two's complement - flip bits and add 1 to get negative
# - one's complement - flip bits
# - excess-bias representation - numbers are shifted by bias B

'''
    ნიკა ოთიაშვილი, დავალება 2.3.
    გადაჰყავს ნიშნიანი ათობითი რიცხვი ორობითში და პირიქით 
'''
debug_mode = True
def log(msg, *m):
    if debug_mode:
        print("LOG:", msg, *m)

def flip_bits(num):
    # ატრიალებს ორობითი რიცხვის ბიტებს
    assert type(num) is str
    ans = ""
    for c in num:
        if c == "0":
            ans = "{}{}".format(ans, "1")
        else:
            ans = "{}{}".format(ans, "0")
    return ans

def to_bin(num):
    # გადაიყვანს ათობითიდან ორობითში უნიშნოდ (0-ებს მიუწერს ბაიტებად დაყოფისთვის)
    assert type(num) is int
    ans = ""
    quotent = num
    while True:
        remainder = quotent % 2
        ans = "{}{}".format(remainder, ans)
        if quotent == remainder:
            break
        quotent = int((quotent - remainder) / 2)
    # ბაიტებად დაყოფისთვის 0-ების მიწერა
    if len(ans) % 4 > 0:
        ans = "{}{}".format("0"*(4 - (len(ans) % 4)), ans)
    return ans

def to_dec(num, sign="+"):
    # გადაიყვანს ორობითიდან ათობითში
    assert type(num) is str
    ans = 0
    for i, c in enumerate(num):
        pos = len(num) - i - 1
        digit = int(c) * (2**pos)
        ans += digit
    # მივუწეროთ ნიშანი პასუხს
    if sign == "+":
        return ans
    elif sign == "-":
        return "{}{}".format("-", ans)

def get_dec_sign(dec_num):
    # აბრუნებს ათობითი რიცხვის ნიშანს ("-" ან "+")
    if dec_num[0] == "-":
        return "-"
    else:
        return "+"

def signed_magnitude_dec_to_bin(dec_num):
    # გადაიყვანს ნიშნიან ათობით რიცხვს ორობით ნიშნიან გამოსახულებაში
    assert type(dec_num) is str
    sign = get_dec_sign(dec_num)
    raw_num = dec_num
    if dec_num[0] == "-" or dec_num[0] == "+":
        raw_num = dec_num[1:]
    bin_num = to_bin(int(raw_num))
    if sign == "-":
        return "{}{}".format("1", bin_num)
    elif sign == "+":
        return "{}{}".format("0", bin_num)

def signed_magnitude_bin_to_dec(bin_num):
    # აბრუნებს ნიშნიანი გამოსახულებით ჩაწერილი ორობითი რიცხვის ათობით მნიშვნელობას
    assert type(bin_num) is str
    # დავითრიოთ ნიშანი
    sign = "+"
    if bin_num[0] == "1":
        sign = "-"
    raw_bin_num = bin_num[1:]
    raw_dec_num = to_dec(raw_bin_num)
    return "{}{}".format(sign, raw_dec_num)

def twos_complement_dec_to_bin(dec_num):
    # გადაიყვანს ნიშნიან ათობით რიცხვს ორობით ფუძის დამატებით გამოსახულებაში
    assert type(dec_num) is str
    # თუ დადებითია, პირდაპირ გადავიყვანოთ
    if get_dec_sign(dec_num) == "+":
        return to_bin(int(dec_num))
    # წავაჭრათ ნიშანი
    raw_dec_num = dec_num
    if dec_num[0] == "-" or dec_num[0] == "+":
        raw_dec_num = dec_num[1:]
    log("raw_dec_num:", raw_dec_num)
    # გადავიყვანოთ ორობითში
    raw_bin_num = to_bin(int(raw_dec_num))
    log("raw_bin_num:", raw_bin_num)
    # დავატრიალოთ ბიტები
    flipped_bin_num = flip_bits(raw_bin_num)
    log("flipped_bin_num:", flipped_bin_num)
    # გადავიყვანოთ ათობითში, დავუმატოთ 1 და გადმოვიყვანოთ ორობითში
    bin_num = to_bin(to_dec(flipped_bin_num) + 1)
    # მივუწეროთ ნულები მარცხნივ თუ დამოკლდა
    if len(bin_num) < len(raw_bin_num):
        bin_num = "{}{}".format("0"*(len(raw_bin_num) - len(bin_num)), bin_num)
    elif len(bin_num) > len(raw_bin_num): # მოვაჭრათ მარცხნიდან თუ ზედმეტია
        bin_num = bin_num[len(bin_num) - len(raw_bin_num):]
    # გამოვიტანოთ პასუხი
    return bin_num
    
def twos_complement_bin_to_dec(bin_num):
    # აბრუნებს ფუძის დამატებითი გამოსახულებით ჩაწერილი ორობითი რიცხვის ათობით მნიშვნელობას
    pass

def main():
    # შევიყვანოთ ინფორმაცია
    number = input("Number: ")    
    choice = int(input('''Choose the base of your number: 
        1) Base 10
        2) Base 2\n'''))
    # method = int(input('''Choose method: 
    #     1)signed magnitude
    #     2)two's complement
    #     3)one's complement
    #     4)excess-bias\n'''))
    if choice == 1:
        base = 10
        print("Signed magnitude:", signed_magnitude_dec_to_bin(number))
        print("Two's complement:", twos_complement_dec_to_bin(number))
    elif choice == 2:
        base = 2
        print("Signed magnitude:", signed_magnitude_bin_to_dec(number))
        print("Two's complement:", twos_complement_bin_to_dec(number))
