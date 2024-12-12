from pathlib import Path


def main(input: str):
    datafile = Path("day05") / input
    data = datafile.read_text()
    (rules, pages) = data.split("\n\n")
    rules = rules.splitlines()
    pages = pages.splitlines()

    output = 0

    for page in pages:
        if page == "":
            continue
        numbers = page.split(",")
        numbers = [int(x) for x in numbers]
        correct = True
        for rule in rules:
            (a, b) = rule.split("|")
            a = int(a)
            b = int(b)
            if a in numbers:
                ind_a = numbers.index(a)
            else:
                ind_a = 0
            if b in numbers:
                ind_b = numbers.index(b)
            else:
                ind_b = len(numbers)
            if ind_b < ind_a:
                correct = False
                break
        if correct:
            output += numbers[(len(numbers) // 2)]

    return output


def test():
    result = main("test.txt")
    expected = 143
    assert result == expected, f"test failed {result} != {expected}"


if __name__ == "__main__":
    test()
    result = main("input.txt")
    print(result)
