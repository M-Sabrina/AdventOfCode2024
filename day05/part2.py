from pathlib import Path


def check_all_rules(numbers: list[int], rules: list[str]):
    for rule in rules:
        (a_, b_) = rule.split("|")
        a = int(a_)
        b = int(b_)
        if (a not in numbers) or (b not in numbers):
            continue
        ind_a = numbers.index(a)
        ind_b = numbers.index(b)
        if ind_b < ind_a:
            return False
    return True


def main(input: str):
    datafile = Path("day05") / input
    data = datafile.read_text()
    (rules_, pages_) = data.split("\n\n")
    rules = rules_.splitlines()
    pages = pages_.splitlines()

    output = 0

    for page in pages:
        if page == "":
            continue
        numbers_ = page.split(",")
        numbers = [int(x) for x in numbers_]
        correct = check_all_rules(numbers, rules)
        if correct:
            continue
        while not correct:
            correct = check_all_rules(numbers, rules)
            if correct:
                output += numbers[(len(numbers) // 2)]
                break
            else:
                for rule in rules:
                    (a_, b_) = rule.split("|")
                    a = int(a_)
                    b = int(b_)
                    if (a not in numbers) or (b not in numbers):
                        continue
                    ind_a = numbers.index(a)
                    ind_b = numbers.index(b)
                    if ind_b < ind_a:
                        numbers[ind_a], numbers[ind_b] = numbers[ind_b], numbers[ind_a]

    return output


def test():
    result = main("test.txt")
    expected = 123
    assert result == expected, f"test failed {result} != {expected}"


if __name__ == "__main__":
    test()
    result = main("input.txt")
    print(result)
