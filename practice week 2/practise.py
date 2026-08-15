def get_average_score(scores: dict, student: str) -> None:
    try:
        total = scores[student.strip().capitalize()]
        num_tests = 5
        average = total / num_tests
        print(f"{student}'s average: {average}")
    except KeyError:
        print(f"No record found for {student}")
    except ZeroDivisionError:
        print(f"Can't calculate average for {student}, num_tests is zero")
    except ValueError:
        print("Invalid value encountered")


def main():
    scores = {"Ali": 450, "Sara": 0}

    get_average_score(scores, "Omer")
    get_average_score(scores, "Sara")
    get_average_score(scores, "Ali")
    get_average_score(scores, "ali")


if __name__ == "__main__":
    main()