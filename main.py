import utils
from data.students import students


def main():
    highest_score = utils.max_score(students)
    print(f"The highest score is {highest_score}")

    minimum_score = utils.min_score(students)
    print(f"The minimum score is {minimum_score}")

    avg = utils.avg_score(students)
    print(f"The avg score is {avg}")


if __name__ == '__main__':
    main()
