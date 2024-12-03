def is_safe_report(levels):
    diff = levels[1] - levels[0]
    increasing = diff > 0

    for i in range(1, len(levels)):
        current_diff = levels[i] - levels[i - 1]

        if (increasing and current_diff <= 0) or (not increasing and current_diff >= 0):
            return False
        if abs(current_diff) < 1 or abs(current_diff) > 3:
            return False

    return True


def can_be_made_safe(levels):
    if is_safe_report(levels):
        return True
    for i in range(len(levels)):
        modified_levels = levels[:i] + levels[i + 1 :]
        if is_safe_report(modified_levels):
            return True

    return False


def count_safe_reports(file_path):
    safe_count = 0
    with open(file_path, "r") as file:
        for line in file:
            levels = list(map(int, line.strip().split()))
            if can_be_made_safe(levels):
                safe_count += 1
    return safe_count


def main():
    file_path = "files/input.txt"
    safe_reports = count_safe_reports(file_path)
    print(f"Number of safe reports: {safe_reports}")


if __name__ == "__main__":
    main()
