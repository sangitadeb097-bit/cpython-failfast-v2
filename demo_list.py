# demo_list.py
# Demonstration of modifying a list while iterating over it.

def main():
    numbers = [1, 2, 3, 4, 5, 6]
    print(f"Starting list: {numbers}")

    for item in numbers:
        print(f"Current item: {item}")
        if item == 2:
            numbers.remove(item)
            print(f"Removed {item}, list is now: {numbers}")

    print(f"Finished iteration. Final list: {numbers}")

if __name__ == "__main__":
    main()
