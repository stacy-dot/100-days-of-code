while True:
    number = int(input("Enter a number between 1 and 10: "))

    print(f"\nMultiples of {number} (skipping multiples of 4):")

    for i in range(1, 11):
        result = number * i
        if result % 4 == 0:
            continue
        print(result)

    play_again = input("\nDo you want to play again? (yes/no): ").lower()
    if play_again != "yes":
        print("Goodbye!")
        break
