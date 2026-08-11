def main():

    with open(notes.txt, "r") as file:
        text = file.read()
        print(text)

if __name__ == "__main__":
    main()