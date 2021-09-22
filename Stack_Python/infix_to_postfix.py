from queue import LifoQueue


def infix_to_postfix(string):
    st = LifoQueue(maxsize=0)
    postfix = ''
    for i in string:
        if i != '+' or i != '-' or i != '*' or i != '/' or i != '(' or i != ')':
            postfix = postfix + str(i)
        else:
            return