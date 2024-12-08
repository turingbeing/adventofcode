from functools import cmp_to_key

def read_input_file(file_path):
    with open(file_path, "r") as file:
        content = file.read().strip().split("\n\n")

    rules = [tuple(map(int, rule.split("|"))) for rule in content[0].split("\n")]
    updates = [list(map(int, update.split(","))) for update in content[1].split("\n")]

    print("Rules:", rules)  # Debug print
    print("Updates:", updates)  # Debug print

    return rules, updates


def is_update_valid(update, rules):
    for first, second in rules:
        if first in update and second in update:
            if update.index(first) > update.index(second):
                return False
    return True

def get_middle_page(update):
    return update[len(update) // 2]

def compare_pages(a, b, rules):
    for first, second in rules:
        if a == first and b == second:
            return -1
        if a == second and b == first:
            return 1
    return 0

def order_update(update, rules):
    return sorted(update, key=cmp_to_key(lambda x, y: compare_pages(x, y, rules)))

def sum_middle_pages(file_path):
    rules, updates = read_input_file(file_path)
    total = 0
    for i, update in enumerate(updates):
        valid = is_update_valid(update, rules)
        middle_page = get_middle_page(update)
        print(f"Update {i+1}: {update}")
        print(f"  Valid: {valid}")
        print(f"  Middle page: {middle_page}")
        if valid:
            total += middle_page
            print(f"  Added to total. New total: {total}")
        print()
    return total

def sum_middle_pages_of_incorrect_updates(file_path):
    rules, updates = read_input_file(file_path)
    total = 0
    for update in updates:
        if not is_update_valid(update, rules):
            ordered_update = order_update(update, rules)
            middle_page = get_middle_page(ordered_update)
            total += middle_page
            print(f"Incorrect update: {update}")
            print(f"Ordered update: {ordered_update}")
            print(f"Middle page: {middle_page}")
            print(f"Running total: {total}")
            print()
    return total

def main():
    file_path = "files/input.txt"
    valid_updates = sum_middle_pages(file_path)
    invalid_updates = sum_middle_pages_of_incorrect_updates(file_path)
    print(f"Number of valid updates: {valid_updates}")
    print(f"Total of middle pages of incorrect updates: {invalid_updates}")


if __name__ == "__main__":
    main()
