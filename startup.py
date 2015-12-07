
_exit = exit

class _Exit(object):
    def __repr__(self):
        _exit()
    def __call__(self, code=None):
        _exit(code)

q = exit = _Exit()
