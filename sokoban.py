def main():
    history = []

    while True:
        action = input("Action: ").lower()
        
        if action == "undo":
            undone = history.pop()
            print(f"Undone: {undone}")
            continue
        elif action == "quit":
            print("Bye!")
            break
        elif action == "restart":
            history.clear()
            print("Restarted!")
            continue
        else:
            history.append(action)

        print(history)
     


main()