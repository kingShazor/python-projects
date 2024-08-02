with open("data.txt", 'r') as input:
    content = input.read()

with open("out.txt", 'w') as out:
    out.write(content)
