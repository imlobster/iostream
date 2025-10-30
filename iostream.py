import sys

class _int_cxxostream:
    def __init__(self, istream):
        self.stream = istream

    def __lshift__(self, iv):
        if iv is endl:
            self.stream.write('\n')
            self.stream.flush()
        elif iv is flush:
            self.stream.flush()
        else:
            self.stream.write(str(iv))
        return self

flush = object()
endl = object()

cout = _int_cxxostream(sys.stdout)
cerr = _int_cxxostream(sys.stderr)

__all__ = [
    'cout', 'cerr',
    'endl', 'flush'
]
