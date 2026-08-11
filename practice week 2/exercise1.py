def main():

    with open("notes.txt", "r") as file:
        text = file.read()
        print(text)

    with open("notes.txt", "a") as file:
        file.write("Omer studies\n")
        file.write("omer plays\n")

    with open("notes.txt", "r") as file:
        reader = file.readlines()
        for line in reader:
            print(line.strip())


if __name__ == "__main__":
    main()