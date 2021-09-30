class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinaryTree(object):
    def __init__(self, root):
        self.root = Node(root)

    def print_tree(self, traversal_type):
        if traversal_type == "inorder":
            return self.preorder_print(tree.root, "[")
        else:
            print("traversal type " +
                  str(traversal_type), +"is not supported.")
            return False

    def inorder_print(self, start, traversal):
        # left=>root =>right
        if start:
            traversal = self.inorder_print(start.left, traversal)
            traversal += (str(start.value)+"] [")
            traversal = self.inorder_print(start.right, traversal)
        return traversal


root = input(str("input akar :"))
simpul_kiri = input(str("input simpul_kiri :"))
simpul_kanana = input(str("input simpul_kanana :"))
ranting_kiri_kiri = input(str("input ranting_kiri_kiri :"))
ranting_kiri_kanan = input(str("input ranting_kiri_kanan :"))
ranting_kanan_kiri = input(str("input ranting_kanan_kiri :"))
ranting_kanan_kanan = input(str("input ranting_kanan_kanan :"))

tree = BinaryTree(root)
tree.root.left = Node(simpul_kiri)
tree.root.right = Node(simpul_kanana)
tree.root.left.left = Node(ranting_kiri_kiri)
tree.root.left.right = Node(ranting_kiri_kanan)
tree.root.right.left = Node(ranting_kanan_kiri)
tree.root.right.right = Node(ranting_kanan_kanan)
print(tree.print_tree("inorder"))
