class Block(tuple):
    def __repr__(self):
        orig = super().__repr__()
        orig = f"{self.__class__.__name__}{orig}"
        return orig
