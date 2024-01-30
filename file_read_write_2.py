file_path = "650CC_STATEMENTS_033123.txt"

line_count = 0

with open(file_path, "r") as file:
    lines = file.readlines()

    for line in lines:
        line_count = line_count + 1
        if line.startswith('200~'):
            print("Line {} : {}".format(line_count, line.strip()))

