
"""
Day 1 - Python Basics
Clean, modular examples for lists, loops, dictionaries, and basic algorithms.
Save as: Day1_Python_Basics/problems.py
"""

def demo_prints():
    print("=== Basic prints ===")
    print(3)
    print("Hello, World!")


def list_examples():
    print("\n=== List examples ===")
    student = ['Jack', 32, 'Computer Science', [2, 4]]
    print("student:", student)

    empty_list = []
    print("empty_list:", empty_list)

    my_list = ['p', 'r', 'o', 'g', 'r', 'a', 'm']
    print("my_list =", my_list)
    print("my_list[2:5] =", my_list[2:5])
    print("my_list[2:-2] =", my_list[2:-2])
    print("my_list[0:3] =", my_list[0:3])

    my_list2 = [1, 2, 3, 4.5]
    print("my_list2:", my_list2, "length:", len(my_list2))

    # Example mutating list
    nums = [10, 20, 30, 40, 50]
    print("original nums:", nums)
    nums[1] = 200
    nums.append(600)
    nums.insert(2, 300)
    nums.remove(600)
    nums.pop(0)
    print("mutated nums:", nums)

    # sum and average
    total_sum = sum(nums)
    average = total_sum / len(nums)
    print("sum:", total_sum, "average:", average)

    # reverse in-place vs comprehension
    list1 = [100, 200, 300, 400, 500]
    list1.reverse()
    print("reversed list1:", list1)

    # squares with loop and comprehension
    numbers = list(range(1, 8))
    squares_loop = []
    for i in numbers:
        squares_loop.append(i ** 2)
    print("squares_loop:", squares_loop)

    squares_comp = [x * x for x in numbers]
    print("squares_comp:", squares_comp)


def find_min_max_no_builtin(data):
    """Return (min, max) from list without using min()/max()."""
    if not data:
        raise ValueError("Empty list provided")

    smallest = largest = data[0]
    for x in data:
        if x > largest:
            largest = x
        elif x < smallest:
            smallest = x
    return smallest, largest


def count_occurrences_no_builtin(seq, target):
    """Return count of target in seq without using .count()."""
    cnt = 0
    for item in seq:
        if item == target:
            cnt += 1
    return cnt


def while_loop_demo(limit=10):
    print("\n=== While loop demo ===")
    i = 1
    while i <= limit:
        print(i, end=' ')
        i += 1
    print()


def number_pattern(rows=5):
    print("\n=== Number pattern ===")
    for i in range(1, rows + 1):
        for j in range(1, i + 1):
            print(j, end=' ')
        print()


def sum_upto_n(n):
    """Return sum of numbers from 1 to n."""
    s = 0
    for i in range(1, n + 1):
        s += i
    return s


def multiplication_table_of_2():
    """Return multiplication table of 2 from 1 to 10 as a list."""
    table = []
    for i in range(1, 11):
        table.append(2 * i)
    return table


def conditional_loop_display(numbers):
    """Print numbers based on conditions (demonstrates break/continue)."""
    print("\n=== Conditional loop display ===")
    for num in numbers:
        if num >= 500:
            break
        elif num > 150:
            continue
        elif num % 5 == 0:
            print(num)


def dictionary_operations_demo():
    print("\n=== Dictionary operations ===")
    my_dict = {'name': 'Alice', 'age': 35, 'city': 'New York'}
    my_dict["Profession"] = "Doctor"
    print("after adding Profession:", my_dict)
    my_dict["age"] = 40
    print("after modifying age:", my_dict)
    print("city value:", my_dict["city"])

    # Removing a key
    my_dict.pop("Profession", None)
    print("after popping Profession:", my_dict)

    # Iterate key-value pairs
    print("key-value pairs:")
    for k, v in my_dict.items():
        print(k, v)


def main():
    demo_prints()
    list_examples()

    data = [8, 2, 15, 1, 9]
    smallest, largest = find_min_max_no_builtin(data)
    print("\nLargest number:", largest)
    print("Smallest number:", smallest)

    sports = ['Cricket', 'Football', 'Hockey', 'Football', 'Tennis', 'Football']
    football_count = count_occurrences_no_builtin(sports, "Football")
    print("\nFootball appears", football_count, "times")

    while_loop_demo(limit=10)
    number_pattern(rows=5)

    # sum up to n (safe input handling)
    try:
        raw = input("Enter a number to sum up to (press Enter for 10): ").strip()
        n = int(raw) if raw else 10
    except Exception:
        print("Invalid input — using default n=10")
        n = 10
    print("Sum is:", sum_upto_n(n))

    print("\nMultiplication table of 2:", multiplication_table_of_2())

    numbers = [12, 75, 150, 180, 145, 525, 50]
    conditional_loop_display(numbers)

    dictionary_operations_demo()


if __name__ == "__main__":
    main()
