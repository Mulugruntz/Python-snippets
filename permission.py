import contextlib
import os
import stat

@contextlib.contextmanager
def ensure_permission(path, perm):
    """
    Makes sure file at `path` has some given permissions.
    Restores the initial permissions afterwards.
    .. code-block::
       with ensure_permission('myfile.txt', stat.S_IROTH | stat.S_IWOTH):
           myfunc('myfile.txt')
    """
    root_perm = stat.S_IMODE(os.stat(path).st_mode)
    os.chmod(path, root_perm | perm)
    try:
        yield
    finally:
        os.chmod(path, root_perm) 
