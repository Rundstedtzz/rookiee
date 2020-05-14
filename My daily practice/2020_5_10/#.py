


'''
func1 = input("Enter file name: ")
fh = open(func1)
count = 0.0
for line in fh:
    if line.startswith("#") :
        continue
    else:
        line.join('#')
    print(count)
fh.close



func1 = input("Enter file name: ")
with open(func1) as fh:
    for line in fh:
        fh.write('#', 'EDF ')
fh.close
'''
def add_str2(f_name, str_to_add):
    with open(f_name, "r") as f:
        lines = f.readlines()
        for index, line in enumerate(lines):
            if not line.startswith("#"):
                lines[index] = str_to_add + line.strip() + "\n"
            elif line.startswith("#"):
                continue

    with open(f_name, "w") as f:
        for line in lines:
            f.write(line)

'''
def add_str3(f_name, string_to_remove):
    with open(f_name, "r") as f:
        lines = f.readlines()
        for index, line in enumerate(lines):
            if not line.startswith("#"):
                continue
            elif line.startswith("#"):
                line[index]= line.replace("string_to_remove","")

    with open(f_name, "w") as f:
        for line in lines:
            f.write(line)
'''
