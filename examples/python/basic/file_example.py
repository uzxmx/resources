#!/usr/bin/env python

import os
import tempfile
import shutil

def delete_file(name):
    if os.path.isdir(name):
        shutil.rmtree(name)
    else:
        os.unlink(name)

tmpdir = tempfile.mkdtemp(prefix='foo_')
print(tmpdir)
delete_file(tmpdir)

tmpfile = tempfile.NamedTemporaryFile(delete=False)
print(tmpfile.name)
delete_file(tmpfile.name)
