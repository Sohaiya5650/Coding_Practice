file_path = "owcf_latenotice_11222023.csv"

line_count = 0

with open(file_path, "r") as file:
    lines = file.readlines()

    for line in lines:
        line_count = line_count + 1
        print("Line {} : {}".format(line_count, line.strip()))
