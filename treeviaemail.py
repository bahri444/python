tanya = "Y"
while(tanya == "Y"):
    class Node(object):
        def __init__(self, value):
            self.value = value
            self.left = []
            self.right = []

    class BinaryTree(object):
        def __init__(self, root):
            self.root = Node(root)

        def print_tree(self, traversal_type):
            if traversal_type == "preorder":
                return self.preorder_print(tree.root, "[")
            else:
                print("traversal type " +
                      str(traversal_type), +"is not supported.")
                return False

        def preorder_print(self, start, traversal):
            # root=>left=>right
            if start:
                traversal += (str(start.value)+"] [")
                traversal = self.preorder_print(start.left, traversal)
                traversal = self.preorder_print(start.right, traversal)
            return traversal

    cuaca = input(str("input cuaca [hujan,angin,lembab,cerah] :"))
    root = input(str("input akar :"))
    simpul_kiri = input(str("input simpul_kiri :"))
    simpul_kanana = input(str("input simpul_kanana :"))
    ranting_kiri_kiri = input(str("input ranting_kiri_kiri :"))
    ranting_kiri_kanan = input(str("input ranting_kiri_kanan :"))

    tree = BinaryTree(root)
    tree.root.left = Node(simpul_kiri)
    tree.root.right = Node(simpul_kanana)
    tree.root.left.left = Node(ranting_kiri_kiri)
    tree.root.left.right = Node(ranting_kiri_kanan)
    print()
    print(tree.print_tree("preorder"))
    print()
    if (cuaca == "hujan") or (cuaca == "angin"):
        print("tidak bisa main cuaca sedang ", cuaca)
    elif (cuaca == "lembab") or (cuaca == "cerah"):
        print("bisa main karena cuaca sedang ", cuaca)
    else:
        print("cuaca salah ", cuaca)
    tanya = input(str("apakah anda ingin mengulangnya ?  [Y/N] : "))
    print()

    # def inorder_print(self, start, traversal):
    # left=>root =>right
    # if start:
    #traversal = self.inorder_print(start.left, traversal)
    #traversal += (str(start.value)+"] [")
    #traversal = self.inorder_print(start.right, traversal)
    # return traversal

    # def postorder_print(self, start, traversal):
    # left=>right=>root
    # if start:
    #traversal = self.postorder_print(start.left, traversal)

    #traversal = self.postorder_print(start.right, traversal)
    #traversal += (str(start.value)+"] [")
    # return traversal

    # elif traversal_type == "inorder":
    # return self.inorder_print(tree.root, "")

    # elif traversal_type == "postorder":
    # return self.postorder_print(tree.root, "")

    # print(tree.print_tree("inorder"))
    # print(tree.print_tree("postorder"))
