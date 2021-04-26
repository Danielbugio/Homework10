with open("Livro1.csv", 'r') as Livro1_file:
    livro1_lines = Livro1_file.read().splitlines()

    for row in livro1_lines:
        line_data = row.split(";")
        print(f"{line_data[0]} is {line_data[1]} years old and {line_data[2]}")

