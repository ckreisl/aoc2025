from pathlib import Path


def read_file(filepath: Path) -> str:
    with open(filepath, encoding="utf-8") as f:
        return f.read()


def part_01(content: str) -> int:
    numbers: list[str] = content.split(",")

    sum: int = 0
    for value in numbers:
        x, y = value.split('-')
        start = int(x)
        end = int(y)
        for i in range(start, end + 1):
            s = str(i)
            s_len = len(s)
            first_part = s[:s_len//2]
            second_part = s[s_len//2:]
            if first_part == second_part:
                sum += i

    return sum


def part_02(content: str) -> int:
    def is_repeated_sequence(s: str) -> bool:
        n = len(s)
        for size in range(1, n // 2 + 1):
            if n % size == 0:
                repeats = n // size
                if repeats >= 2 and s == s[:size] * repeats:
                    return True
        return False

    total = 0
    for value in content.split(","):
        start, end = map(int, value.split("-"))
        for i in range(start, end + 1):
            if is_repeated_sequence(str(i)):
                total += i
    return total


def main() -> int:
    filename = "input.txt"
    filepath = Path(__file__).parent / filename
    content = read_file(filepath)

    res1 = part_01(content)
    res2 = part_02(content)

    print(f"Result1: {res1}")
    print(f"Result2: {res2}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
