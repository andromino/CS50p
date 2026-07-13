def main():
    names = ["John", "Smith", "Jane"]
    for name in names:
        print(write_letter(name, "Peach"))

def write_letter(recever, sender):
    return F"""
    +~~~~~~~~~~~~~~~~~~~~~~~~~~~~+
    Dear {recever},

    Thank you for comming to my wedding.
    
    Sincerely,
    {sender}
    +~~~~~~~~~~~~~~~~~~~~~~~~~~~~+
    """

main()