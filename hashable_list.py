# __hash__ is redundant
# https://docs.python.org/3/glossary.html#term-hashable
# >> user-defined classes are hashable by default


class List(list):
    def __hash__(self):
        return hash('|'.join(self))

    # issue with only defined __hash__
    # https://stackoverflow.com/questions/10994229/how-to-make-an-object-properly-hashable
    # https://docs.python.org/3/reference/datamodel.html#object.__hash__
    # def __eq__(self, other):
    #     return super().__eq__(other)

    # if in one line
    # https://stackoverflow.com/questions/2802726/putting-a-simple-if-then-else-statement-on-one-line
    def __repr__(self):
        return '|'.join(self) if len(self) else ''
