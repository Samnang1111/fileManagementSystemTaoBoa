# Task 1
class Node:
    def __init__(self, name, is_file=False):
        """
        Initialize a node representing a file or directory
        
        Args:
        - name (str): Name of the file or directory
        - is_file (bool): Indicates if the node is a file (True) or directory (False)
        """
        self.name = name
        self.is_file = is_file
        self.children = []  # List of child nodes

class FileSystemTree:
    def __init__(self, root_name="Root"):
        """
        Initialize the file system tree with a root node
        
        Args:
        - root_name (str): Name of the root directory
        """
        self.root = Node(root_name)

    def print_tree(self, node=None, level=0):
        """
        Print the hierarchical structure of the tree
        
        Args:
        - node (Node): Starting node for printing (default is root)
        - level (int): Current depth level for indentation
        """
        if node is None:
            node = self.root

        # Print current node with indentation
        indent = "  " * level
        file_type = "[F]" if node.is_file else "[D]"
        print(f"{indent}{file_type} {node.name}")

        # Recursively print children
        for child in node.children:
            self.print_tree(child, level + 1)

    def find_node(self, name, current_node=None):
        """
        Find a node by name in the tree
        
        Args:
        - name (str): Name of the node to find
        - current_node (Node): Current node in the search (default is root)
        
        Returns:
        - Node or None: Found node or None if not found
        """
        if current_node is None:
            current_node = self.root

        # Check current node
        if current_node.name == name:
            return current_node

        # Search in children
        for child in current_node.children:
            found = self.find_node(name, child)
            if found:
                return found

        return None

    def add_node(self, parent_name, new_name, is_file=False):
        """
        Add a new node under a specified parent node
        
        Args:
        - parent_name (str): Name of the parent node
        - new_name (str): Name of the new node
        - is_file (bool): Indicates if the new node is a file
        
        Returns:
        - bool: True if node added successfully, False otherwise
        """
        # Check if node already exists
        if self.find_node(new_name):
            print(f"Node '{new_name}' already exists.")
            return False

        # Find parent node
        parent = self.find_node(parent_name)
        if not parent:
            print(f"Parent '{parent_name}' not found.")
            return False

        # Create and add new node
        new_node = Node(new_name, is_file)
        parent.children.append(new_node)
        return True

def main():
    # Create file system tree
    fs_tree = FileSystemTree()

    while True:
        print("\n--- File System Management ---")
        print("1. Add Directory")
        print("2. Add File")
        print("3. Print Tree")
        print("4. Search")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            parent = input("Enter parent directory name: ")
            dir_name = input("Enter directory name: ")
            fs_tree.add_node(parent, dir_name)

        elif choice == '2':
            parent = input("Enter parent directory name: ")
            file_name = input("Enter file name: ")
            fs_tree.add_node(parent, file_name, is_file=True)

        elif choice == '3':
            fs_tree.print_tree()

        elif choice == '4':
            search_name = input("Enter name to search: ")
            result = fs_tree.find_node(search_name)
            if result:
                print(f"Found: {result.name} ({'File' if result.is_file else 'Directory'})")
            else:
                print("Not found.")

        elif choice == '5':
            break

        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()