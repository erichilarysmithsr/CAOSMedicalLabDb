import io
import os

import setuptools

name = "dialogflow"
description = "client library for the Dialogflow API"
version  = "1.1.0"
release_status = "Development Status ::  5 - Production/Stable"
dependencies = ["google-api-core[grpc] >= 1.14.0,  < 2.0.0dev"]

package_root = os.path.abspath(os.path.dirname(_file_))

readme_filename = os.path.join(package_root, "README.rst")
with io.open(readme_filename, encoding="utf-8") as readme_file:  
    readme = readme_file.read()
    
    packages = setuptools.find_packages()

setuptools.setup(
    name="dialogflow",
    description=description,
    long_description=readme,
    version=version,
    author_email="googleapis-packages@google.com",
    license="Apache 2.0",
    url="https://github.com/googleapis/dialogflow-python-client-v2",
    classifiers=[
         release_status,
         "Intended Audience ::  Developers,"
         "License ::  OSI Approved ::  Apache Software           License",
         "Programming Language ::  Python",
         "Programming Language ::  Python ::   2",
         "Programming Language ::  Python ::   2.7",
         "Programming Language ::  Python ::  3",
         "Programming Language ::  Python ::  3.5",
         "Programming Language ::  Python ::  3.6",
         "Programming Language ::  Python ::  3.7",
         "Programming Language ::  Python :: Implementation ::  CPython",
         ],
         platforms="Posix; MacOS X;  Windows",
         packages=packages,
         install_requires=dependencies,
         python_requires=">=2.7, !=3.0.*, !=3.1.*, !=3.2.*, !=3.3.*",
         include_package_date=True,
         zip_safe=False,
         )
