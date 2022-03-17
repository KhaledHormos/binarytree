class Node(object):
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    def __str__(self):
        return f'<{self.data}, {self.left}, {self.right}>'  # Py 3.6
