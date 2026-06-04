def mask_account(s: str) -> str:
    if len(s) <= 4:
        return s
    return '*' * (len(str(s)[:-4])) + str(s[-4:])
#    return '*' * (len(s) - 4) + s[-4:]

for i in ["1234567890", "9876", "12345"]:
    print(mask_account(i))