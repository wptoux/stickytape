import tempfile as __stickytape_tempfile
import contextlib as __stickytape_contextlib
import shutil as __stickytape_shutil

@__stickytape_contextlib.contextmanager
def __stickytape_temporary_dir():
    dir_path = __stickytape_tempfile.mkdtemp()
    try:
        yield dir_path
    finally:
        __stickytape_shutil.rmtree(dir_path)

with __stickytape_temporary_dir() as __stickytape_working_dir:
    def __stickytape_write_module(path, contents):
        import os, os.path, errno

        def make_package(path):
            # TODO: should use path.split
            parts = path.split("/")
            partial_path = __stickytape_working_dir
            for part in parts:
                partial_path = os.path.join(partial_path, part)
                if not os.path.exists(partial_path):
                    os.mkdir(partial_path)
                    open(os.path.join(partial_path, "__init__.py"), "w").write("\n")
                    
        make_package(os.path.dirname(path))
        
        full_path = os.path.join(__stickytape_working_dir, path)
        with open(full_path, "w") as module_file:
            module_file.write(contents)

    import sys as __stickytape_sys
    __stickytape_sys.path.insert(0, __stickytape_working_dir)
