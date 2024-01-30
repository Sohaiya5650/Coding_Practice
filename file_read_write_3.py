import sys
import re

# file_path = "650CC_STATEMENTS_033123.txt"


def find_acct_no(line):
    pattern = r"~02(\d+)~"
    match = re.search(pattern, line)

    if match:
        value = match.group(1)
        return value
    else:
        return None


def print_acct_no(file_path):
    line_count = 0

    with open(file_path, "r") as file:
        lines = file.readlines()
        for line in lines:
            if line.startswith("200~"):
                acct_value = find_acct_no(line)
                if acct_value is not None:
                    line_count = line_count + 1
                    print("Line {} : {}".format(line_count, acct_value.strip()))



def main():
    if len(sys.argv)!=2:
        print("Invalid no of arguments")
        sys.exit(1)

    file_path = sys.argv[1]

    print_acct_no(file_path)


if __name__ == "__main__":
    main()


