import time
from datetime import datetime, timedelta

class Student:
    def __init__(self, name, id_no, stream):
        self.name = name
        self.id_no = id_no
        self.stream = stream
        self.book1 = None
        self.book2 = None
        self.book_no = 0
        self.issuedbook = 0

class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

class LibraryManagement:
    def __init__(self):
        self.root = None

    def insert(self, key):
        self.root = self._insert_rec(self.root, key)

    def _insert_rec(self, root, key):
        if not root:
            return Node(key)

        if key < root.key:
            root.left = self._insert_rec(root.left, key)
        elif key > root.key:
            root.right = self._insert_rec(root.right, key)
        else:
            print("error.")

        return root

    def delete_key(self, key):
        self.root = self._delete_rec(self.root, key)

    def _delete_rec(self, root, key):
        if not root:
            return root

        if key < root.key:
            root.left = self._delete_rec(root.left, key)
        elif key > root.key:
            root.right = self._delete_rec(root.right, key)
        else:
            if not root.left:
                return root.right
            elif not root.right:
                return root.left

            root.key = self.min_value(root.right)

            root.right = self._delete_rec(root.right, root.key)

        return root

    def min_value(self, root):
        minv = root.key
        while root.left:
            minv = root.left.key
            root = root.left
        return minv

    def contains_node(self, value):
        return self._contains_node_recursive(self.root, value)

    def _contains_node_recursive(self, current, key):
        if not current:
            return False

        if key == current.key:
            return True

        return self._contains_node_recursive(current.left, key) if key < current.key else self._contains_node_recursive(current.right, key)

    def print_tree(self):
        self.root = self._print_tree_rec(self.root, 0)

    def _print_tree_rec(self, t, space):
        if not t:
            return self.root

        space += 5
        self._print_tree_rec(t.right, space)

        print()
        for i in range(5, space):
            print(" ", end="")
        print("[{}]".format(t.key), end="")

        return self._print_tree_rec(t.left, space)

    def print_inorder(self):
        self._print_inorder(self.root)

    def _print_inorder(self, node):
        if not node:
            return
        self._print_inorder(node.left)
        print(node.key)
        self._print_inorder(node.right)

def main():
    tree = LibraryManagement()
    hash_mapping = {}
    students = [
        Student("Rupa", 6117, "B.Tech-AIML"),
        Student("Haritha", 6110, "B.Tech-AIML"),
        Student("Jyothi", 6101, "B.Tech-AIML")
    ]

    fr = open("append.txt", "a+")
    br = open("append.txt", "a+")
    fr1 = open("append.txt", "a+")
    br1 = open("append.txt", "a+")
    fr2 = open("append.txt", "a+")
    br2 = open("append.txt", "a+")
    fr3 = open("append.txt", "a+")
    br3 = open("append.txt", "a+")
    file = open('x.txt',"r")
    reader = file.readlines()
    file2 = open('y.txt', "r")
    reader2 = file2.readlines()
    file3 = open('z.txt', "r")
    reader3 = file3.readlines()

    formatter = "%d/%m/%Y %H:%M:%S"
    cal = datetime.now()

    i = 0
    for line in reader:
        tree.insert(line.strip())
        hash_mapping[line.strip()] = i
        i += 1

    arr = [[0 for _ in range(2)] for _ in range(100)]

    o = 0
    for number in reader2:
        result = int(number.strip())
        if i != o:
            arr[o][0] = result
        o += 1

    pq = 0
    for number in reader3:
        result = int(number.strip())
        if i != pq:
            arr[pq][1] = result
        pq += 1

    e1 = False
    while not e1:
        print("\n.....................................")
        print("1. Librarian Login.")
        print("2. User Login.")
        print("3. Exit.")
        print("\n.....................................")

        ch1 = int(input("\nEnter Your choice:"))

        if ch1 == 1:
            pwd1 = "abc123"
            id1 = "dsa@12"

            id2 = input("\nEnter UserId:")
            pwd2 = input("\nEnter Password:")

            if id1 != id2:
                print("Invalid Userid.")
            elif pwd1 != pwd2:
                print("Invalid Password.")
            else:
                print("Login succesfully.")
                e2 = False
                while not e2:
                    print("\n.....................................")
                    print("1. Add book.")
                    print("2. Delete book.")
                    print("3. Update book.")
                    print("4. Print Books Details.")
                    print("5. Print Books in-order.")
                    print("6. Print tree")
                    print("7. Exit")
                    print("\n.....................................")

                    ch2 = int(input("\nEnter Your choice:"))

                    if ch2 == 1:
                        for line in reader:
                            tree.insert(line.strip())
                            hash_mapping[line.strip()] = i
                            i += 1
                        j = i

                        o = 0
                        for number in reader2:
                            result = int(number.strip())
                            if j != o:
                                arr[o][0] = result
                            o += 1

                        pq = 0
                        for number in reader3:
                            result = int(number.strip())
                            if j != pq:
                                arr[pq][1] = result
                            pq += 1

                        name = input("\nEnter name of book:")
                        z1 = tree.contains_node(name)

                        if z1:
                            print("\nIt is already exists:")
                        else:
                            quantity = int(input("\nEnter quantity of book:"))
                            br1.write(name)
                            br2.write(str(quantity))
                            br3.write(str(quantity))

                            tree.insert(name)
                            hash_mapping[name] = i
                            arr[i][0] += quantity
                            arr[i][1] += quantity
                            i += 1
                    elif ch2 == 2:
                        b1 = input("\nEnter name of book:")
                        x = tree.contains_node(b1)
                        if x:
                            tree.delete_key(b1)
                            hash_mapping.pop(b1)
                    elif ch2 == 3:
                        b2 = input("\nEnter name of book:")
                        z = tree.contains_node(b2)
                        if z:
                            a = hash_mapping.get(b2)
                            q = int(input("\nEnter quantity of book to add more:"))
                            arr[a][0] += q
                    elif ch2 == 4:
                        for key, value in hash_mapping.items():
                            print("Name of book is:", key)
                            print("Total Quantity of book is:", arr[value][0])
                            print("Available Quantity of book is:", arr[value][1])
                            print()
                    elif ch2 == 5:
                        tree.print_inorder()
                    elif ch2 == 6:
                        tree.print_tree()
                    elif ch2 == 7:
                        e2 = True
        elif ch1 == 2:
            e3 = False
            while not e3:
                print("\n.....................................")
                print("1. Issue book.")
                print("2. Return book.")
                print("3. Exit")
                print("\n.....................................")

                ch3 = int(input("\nEnter Your choice:"))

                if ch3 == 1:
                    index = -1
                    id = int(input("\nEnter your id:"))

                    for k in range(len(students)):
                        if students[k].id_no == id:
                            index = k
                            break

                    if index != -1:
                        if students[index].book_no == 2:
                            print("\nYou can't issue more than two books.")
                        else:
                            book = input("\nEnter name of book:")
                            x = tree.contains_node(book)
                            if x:
                                a = hash_mapping.get(book)
                                if arr[a][1] > 0:
                                    if not students[index].book1:
                                        students[index].book1 = book
                                    else:
                                        students[index].book2 = book
                                    print("Book issued successfully.")
                                    arr[a][1] -= 1
                                    Cday = cal
                                    print("Currunt Date Time :", cal.strftime(formatter))
                                    cal += timedelta(seconds=5)
                                    Rday1 = cal
                                    print("Due Date Time:", Rday1.strftime(formatter))
                                    students[index].book_no += 1

                                    br.write("\nStudent name:   " + students[index].name)
                                    br.write("\nStudent ID  :   " + str(students[index].id_no))
                                    br.write("\nIssued Book :   " + book)
                                    br.write("\nIssued date :   " + Cday.strftime(formatter))
                                    br.write("\nReturn date :   " + Rday1.strftime(formatter))
                                else:
                                    print("You can not issue book now.\nTry again after some days")
                            else:
                                print("Book is not available.")
                    else:
                        print("Invalid ID")
                elif ch3 == 2:
                    try:
                        ind = -1
                        s_id = int(input("\nEnter your id:"))
                        Rbook = input("\nEnter name of book:")
                        for k in range(len(students)):
                            if students[k].id_no == s_id and (students[k].book1 == Rbook or students[k].book2 == Rbook):
                                ind = k
                                break

                        if ind != -1:
                            y = tree.contains_node(Rbook)
                            if y:
                                if students[ind].book1 == Rbook:
                                    students[ind].book1 = None
                                else:
                                    students[ind].book2 = None

                                cal = datetime.now()
                                Rday2 = cal
                                if Rday2 > Rday1:
                                    print("Book is overdue.")
                                    diff = Rday2 - Rday1
                                    noofdays = int(diff.total_seconds() / 2000)
                                    print("Due Date Time:", Rday2.strftime(formatter))
                                    print("book is delayed by", noofdays, "seconds.", diff)
                                    charge = noofdays * 5
                                    print("Your charge is:", charge, "Rs.")
                                else:
                                    print("Book is returned successfully.")

                                a = hash_mapping.get(Rbook)
                                arr[a][1] += 1
                                students[ind].book_no -= 1
                        else:
                            print("Invalid ID")
                    except Exception as e:
                        print("Something is going to be wrong.")
                elif ch3 == 3:
                    e3 = True
        elif ch1 == 3:
            e1 = True

    fr.close()
    br.close()
    fr1.close()
    br1.close()
    fr2.close()
    br2.close()
    fr3.close()
    br3.close()
    file.close()
    file2.close()
    file3.close()

if __name__ == "__main__":
    main()
