def main():
    my_dict = {"key": 0}
    lister = []

    try:
        user_input = int(input("How much did you risk?"))
    except ValueError:
        print("Value error!")
    finally:
        print("what are you doing?")

    try:
        print(my_dict["1"])
    except KeyError:
        print("Key Error!")

    try:
        print(lister[1])
    except IndexError:
        print("Index error!")

    try:
        with open("trex", "r") as file:
            print(file.read())
    except FileNotFoundError:
        print("file not found!")

    try:
        result = 10/len(lister)
    except ZeroDivisionError:
        print("zero division error!")

    def calculate_average(my_dict: dict, key: str) -> None:
        try:
            divisor = my_dict[key.strip().lower()]          # can raise KeyError
            result = 10 / divisor        # can raise ZeroDivisionError
            print(f"Result: {result}")
        except KeyError:
            print(f"'{key}' not found in data")
        except ZeroDivisionError:
            print("Can't divide by zero")


if __name__ == "__main__":
    main()