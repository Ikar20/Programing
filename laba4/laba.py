def read_file(file):
    with open(file) as file:
        paths = []
        counter = 0
        line = int(file.readline().strip("\n"))
        lines = int(file.readline().replace(" ", "").strip("\n"))
        paths.append(int(lines))
        experience = lines
        for l in range(0, line):
            lines = file.readline().replace(" ", "").strip("\n")
            line_length = len(lines)
            for i in range(0, len(lines)):
                counter += 1
                if 0 < i < line_length - 1:
                    if paths[counter - line_length + 1] > paths[counter - line_length]:
                        paths.append(paths[counter - line_length + 1] + int(lines[i]))
                    else:
                        paths.append(paths[counter - line_length] + int(lines[i]))
                elif i == 0:
                    paths.append(paths[counter - line_length + 1] + int(lines[i]))
                else:
                    paths.append(paths[counter - line_length] + int(lines[i]))
                if paths[-1] > experience:
                    experience = paths[-1]

        return experience
def main():
    a = read_file("file1.txt")
    print(a)
main()
