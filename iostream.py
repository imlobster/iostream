import sys

__all__ = [
    'cout', 'cerr',
    'endl', 'flush'
]

class _int_flush_impl: pass
flush = _int_flush_impl()

class _int_endl_impl: pass
endl = _int_endl_impl()

class _int_cxxostream:
    def __init__(self, istream):
        self.stream = istream

    def __lshift__(self, iv):
        if iv is endl:
            print('', end='\n', file=self.stream, flush=True)
        elif iv is flush:
            self.stream.flush()
        else:
            print(str(iv), end='', file=self.stream, flush=False)
        return self


cout = _int_cxxostream(sys.stdout)
cerr = _int_cxxostream(sys.stderr)
