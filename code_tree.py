def binary_tree(x):
    return [x, [], []]


def insert_left(root, new_brench):
    t = root.pop(1)
    if len(t) > 1:
        root.insert(1, [new_brench, t, []])
    else:
        root.insert(1, [new_brench, [], []])
        return root


def insert_right(root, new_brench):
    t = root.pop(2)
    if len(t) > 1:
        root.insert(2, [new_brench, [], t])
    else:
        root.insert(2, [new_brench, [], []])
        return root


def get_root_val(root):
    return root[0]


def set_root_val(root, new_val):
    root[0] = new_val


def get_left_child(root):
    return root[1]


def get_right_child(root):
    return root[2]


x = binary_tree('A')
insert_left(x, 'B')
insert_left(x, 'C')
insert_right(x, 'D')
insert_right(x, 'E')
l = get_left_child(x)
r = get_right_child(x)
print("ini adalah l :", l)
print("ini adalah r :", r)
set_root_val(l, 'F')
print("ini adalah x", x)
insert_left(l, 'G')
print("aku tidak tahu ", x)
