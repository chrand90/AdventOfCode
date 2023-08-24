def parse_input(file_name):
    cur_folder = None
    with open(file_name) as f:
        for line in f.readlines():
            line_splits = line.strip().split(" ")
            if line_splits[0] == "$" and line_splits[1] == "cd":
                if line_splits[2] == "..":
                    cur_folder = cur_folder.parent
                elif line_splits[2] == '/':
                    cur_folder = Folder("root", None)
                else:
                    cur_folder = next(x for x in cur_folder.folders if x.folder_name == line_splits[2])
            elif line_splits[1] == "ls":
                continue
            elif line_splits[0] == "dir":
                cur_folder.add_folder(Folder(line_splits[1], cur_folder))
            else:
                cur_folder.add_file(AoC_File(int(line_splits[0]), line_splits[1]))
    while cur_folder.parent is not None:
        cur_folder = cur_folder.parent

    return cur_folder


def find_directories_with_size_less(folder_sizes, limit=100000):
    total_size = 0
    for _, value in folder_sizes.items():
        if value <= limit:
            total_size += value
    return total_size


def find_largest_with_size_less(folder_sizes, limit=30000000):
    total_size = folder_sizes["root"]
    unused_space = 70000000 - total_size
    cur = total_size
    for _, value in folder_sizes.items():
        if value >= limit-unused_space and value < cur:
            cur = value
    return cur


class Folder:

    def __init__(self, folder_name, parent):
        self.folder_name = folder_name
        self.parent = parent
        self.files = []
        self.folders = []

    def add_folder(self, folder):
        self.folders.append(folder)

    def get_full_path(self, path=""):
        if path == "":
            path = self.folder_name
        if self.parent is None:
            return path
        else:
            return self.parent.get_full_path(self.parent.folder_name + "/" + path)

    def add_file(self, file):
        self.files.append(file)

    def determine_size(self, folder_sizes):
        for folder in self.folders:
            folder.determine_size(folder_sizes)

        folder_sizes[self.get_full_path()] = sum([x.size for x in self.files]) + sum(
            [folder_sizes[x.get_full_path()] for x in self.folders])

    def __str__(self):
        return self.folder_name

    def print_folder_structure(self, indent=0):
        print(" " * indent + "- " + self.folder_name + " (dir)")

        for file in self.files:
            print(" " * (indent + 1) + "- " + file.file_name + " (file, size=" + str(file.size) + ")")

        for folder in self.folders:
            folder.print_folder_structure(indent + 1)


class AoC_File:
    def __init__(self, size, file_name):
        self.size = size
        self.file_name = file_name

    def __str__(self):
        return self.file_name


if __name__ == '__main__':
    folders = parse_input("input.txt")
    folders.print_folder_structure()
    sizes = {}
    folders.determine_size(sizes)
    print(sizes)
    print(find_directories_with_size_less(sizes))
    print(find_largest_with_size_less(sizes))
