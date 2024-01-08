import sys
i = 0
rows = 3
result = ""
filename = sys.argv[1]
with open(filename, 'r') as f:
    lines = f.readlines()
    for line in lines:
      if not line.isspace():
        if (i + 1) % rows == 0:
            result += line
        i += 1
print(result)
