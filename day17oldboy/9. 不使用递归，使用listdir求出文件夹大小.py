import os


def file_size(path):
    list1 = [path]
    size = 0
    while list1:
        pathrmv = list1.pop()
        name_list = os.listdir(pathrmv)
        for name in name_list:
            full_path = os.path.join(pathrmv,name)
            if os.path.isdir(full_path):
                list1.append(full_path)
            elif os.path.isfile(full_path):
                size += os.path.getsize(full_path)
    return size


size = file_size(r'C:\Users\prominent\Desktop\老男孩python')
print(size)