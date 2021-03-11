_list = [2, [1], [1, [0], [1]]]
def tree(label, branches=[]):
    for branch in branches:
        assert is_tree(branch), 'ветви должны быть деревьями'
    return [label] + list(branches)

def label(tree):
    return tree[0]

def branches(tree):
    return tree[1:]

def is_tree(tree):
    if type(tree) != list or len(tree) < 1:
        return False
    for branch in branches(tree):
        if not is_tree(branch):
            return False
    return True

def is_leaf(tree):
    return not branches(tree)


def print_tree(t,indent=0):
    print(' ' * indent + str(label(t)))
    for b in branches(t):
        print_tree(b,indent + 1)

print_tree(_list)

indent=0
while len(_list)!=0:
    print(' ' * indent + str(label(_list)))
    _list.pop(0)
    indent += 1