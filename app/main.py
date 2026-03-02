
import argparse
from app.algorithms import insertion_sort, linear_search
from app.crud import create_user, read_users


def demo_algorithms():
    numbers = [5, 3, 2, 8, 1]
    sorted_numbers = insertion_sort(numbers)
    idx_8 = linear_search(sorted_numbers, 8)
    print("Sorted:", sorted_numbers)
    print("Index of 8:", idx_8)


def demo_database():
    print("Creating user 'Alice' (29)...")
    create_user("Alice", 29)
    print("All users:")
    for row in read_users():
        print(row)


def main():
    parser = argparse.ArgumentParser(description='Azure SQL CRUD + Algorithms demo')
    parser.add_argument('--algorithms', action='store_true', help='Run algorithms demo')
    parser.add_argument('--database', action='store_true', help='Run database CRUD demo')
    args = parser.parse_args()

    if not args.algorithms and not args.database:
        # Default to algorithms demo to avoid DB dependency
        demo_algorithms()
    else:
        if args.algorithms:
            demo_algorithms()
        if args.database:
            demo_database()


if __name__ == '__main__':
    main()
