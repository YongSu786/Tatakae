# Expression Tree from Prefix Expression (using dictionaries)

def construct_expression_tree(prefix):
    """Construct expression tree from prefix expression"""
    stack = []
    operators = ['+', '-', '*', '/', '^']

    # Reverse the prefix expression to process from right to left
    prefix = prefix[::-1]

    for char in prefix:
        if char not in operators:
            # Operand -> create node as dictionary
            stack.append({'data': char, 'left': None, 'right': None})
        else:
            # Operator -> pop two nodes and make them children
            left = stack.pop()
            right = stack.pop()
            stack.append({'data': char, 'left': left, 'right': right})

    # Only one node remains -> root
    return stack[0]

def postorder_traversal(root):
    """Non-recursive postorder traversal"""
    if root is None:
        return []

    stack1 = [root]
    stack2 = []
    result = []

    while stack1:
        node = stack1.pop()
        stack2.append(node)
        if node['left']:
            stack1.append(node['left'])
        if node['right']:
            stack1.append(node['right'])

    while stack2:
        node = stack2.pop()
        result.append(node['data'])

    return result

def delete_tree(root):
    """Delete entire tree (remove references)"""
    stack = [root]
    while stack:
        node = stack.pop()
        if node['left']:
            stack.append(node['left'])
        if node['right']:
            stack.append(node['right'])
        node.clear()  # remove keys
    root = None
    return root

# --- Main Program ---
prefix = input("Enter prefix expression: ")
root = construct_expression_tree(prefix)

print("Post-order Traversal:", *postorder_traversal(root))

root = delete_tree(root)
print("Expression tree deleted.")

