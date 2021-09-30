root = str(input("masukkkan root :"))
brench_left = str(input("masukkkan simpul kiri :"))
brench_right = str(input("masukkkan simpul kanan :"))
left_child = str(input("masukkkan ranting kiri :"))
right_child = str(input("masukkkan ranting kanan :"))


def get_binary(root):
    return[root, [], []]


def get_brench_left(root, brench_new):
    brench_left = root.pop(1)
    if len(brench_left) > 1:
        root.insert(1, [brench_new, brench_left])
    else:
        root.insert(1, [brench_new, [], []])
        return root


def get_brench_right(root, brench_new):
    brench_left = root.pop(2)
    if len(brench_right) > 1:
        root.insert(2, [brench_new, brench_right])
    else:
        root.insert(2, [brench_new, [], []])
        return root


def get_root_val(root):
    return root[0]


def set_root_val(root):
    root[0] = root


def get_left_child(root):
    return root[1]


def get_right_child(root):
    return root[2]


root = get_binary(root)
brench_left(root, brench_left)
right_child(root, right_child)
brench_right(root, brench_right)
left_child(root, left_child)
l = get_left_child(root)
print(l)
set_root_val(l, brench_left)
print(root)
get_brench_left(l, brench_right)
print(root)
