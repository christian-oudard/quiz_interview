class MinStack:

    def __init__(self):
        self.value_stack = []
        self.min_index_stack = []

    def __repr__(self):
        return '{} {}'.format(
            str(self.value_stack),
            str(self.min_value),
        )

    def push(self, value):
        self.value_stack.append(value)
        if len(self.min_index_stack) == 0:
            self.min_index_stack = [len(self.value_stack) - 1]
        else:
            if value < self.min_value:
                self.min_index_stack.append(len(self.value_stack) - 1)

    def pop(self):
        value = self.value_stack.pop()
        if len(self.value_stack) <= self.min_index_stack[-1]:
            self.min_index_stack.pop()
        return value

    @property
    def min_value(self):
        try:
            return self.value_stack[self.min_index_stack[-1]]
        except IndexError:
            return None

