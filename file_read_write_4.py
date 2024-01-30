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


def print_acct_no(file_path, acct_no):
    # line_count = 0
    block_200 = False

    with open(file_path, "r") as file:
        lines = file.readlines()
        for line in lines:
            extracted_acct_value = find_acct_no(line)
            if block_200:
                if line.startswith("200~"):
                    break
                print(line.strip())
            
            if line.startswith("200~") and extracted_acct_value == acct_no:
                block_200 = True
                print(line.strip())


def main():
    if len(sys.argv)!=3:
        print("Invalid no of arguments")
        sys.exit(1)

    file_path = sys.argv[1]
    acct_no = sys.argv[2]

    print_acct_no(file_path, acct_no)


if __name__ == "__main__":
    main()


