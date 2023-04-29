from binarytree import Node,build

# Construct a binary tree from a list of integers
values = [2,4,6,7,8,10, 120]
root = build(values)

# Print the binary tree
print(root)

# Ask the user for their choice
choice = int(input("Enter your choice (1: Add element, 2: Delete element): "))

if choice == 1:
    # Ask the user for the value to be added
    value = int(input("Enter the value to be added: "))
    
    # Add the value to the binary tree
    node = Node(value)
    root.insert(node)
    
    # Print the updated binary tree
    print(root)
    
elif choice == 2:
    # Ask the user for the value to be deleted
    value = int(input("Enter the value to be deleted: "))
    
    # Delete the value from the binary tree
    node = root.search(value)
    root.delete(node)
    
    # Print the updated binary tree
    print(root)
    
else:
    print("Invalid choice")