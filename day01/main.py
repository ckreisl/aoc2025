from pathlib import Path


def read_file(filepath: Path) -> str:
    with open(filepath, encoding="utf-8") as f:
        return f.read()


def main() -> int:
    filename = "sample.txt"
    filepath = Path(__file__).parent / filename
    content = read_file(filepath)

    counter: int = 0
    dial: int = 50
    for line in content.splitlines():
        value = int(line[1:])
        if line.startswith("R"):
            counter += (dial + value - 1) // 100
            dial = (dial + value) % 100
        else:
            counter += (dial - 1) // 100 - (dial - value) // 100
            dial = (dial - value) % 100

        if dial == 0:
            counter += 1

    print(f'Result: {counter}')

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
