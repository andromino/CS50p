def main():
    phone = "123-456-7890"
    print(f"Phone Number: {phone}")

    print(f"Area Code: {phone[:3]}")
    print(f"middle 3 Digits: {phone[4:7]}")
    print(f"Last 4 Digits: {phone[8:]}")
    print(f"Last 4 Digits: {phone[-4:]}")



main()