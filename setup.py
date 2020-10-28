#!/usr/bin/env python

# -----------------------------------------------------------------------------
# Copyright (c) 2013, The Qiita Development Team.
#
# Distributed under the terms of the BSD 3-clause License.
#
# The full license is in the file LICENSE, distributed with this software.
# -----------------------------------------------------------------------------

from setuptools import setup


__version__ = "2020.11"


classes = """
    Development Status :: 3 - Alpha
    License :: OSI Approved :: BSD License
    Topic :: Scientific/Engineering :: Bio-Informatics
    Topic :: Software Development :: Libraries :: Application Frameworks
    Topic :: Software Development :: Libraries :: Python Modules
    Programming Language :: Python
    Programming Language :: Python :: 3.6
    Programming Language :: Python :: Implementation :: CPython
    Operating System :: POSIX :: Linux
    Operating System :: MacOS :: MacOS X
"""


with open('README.rst') as f:
    long_description = f.read()

classifiers = [s.strip() for s in classes.split('\n') if s]

setup(name='qp-woltka',
      version=__version__,
      long_description=long_description,
      license="BSD",
      description='Qiita Plugin: woltka',
      author="Qiita development team",
      author_email="qiita.help@gmail.com",
      url='https://github.com/biocore/qiita',
      test_suite='nose.collector',
      packages=['qp_woltka', 'qp_woltka/trim',
                'qp_woltka/filter', 'qp_woltka/woltka',
                'qp_woltka/sortmerna'],
      package_data={
        'qp_woltka': [
            'support_files/config_file.cfg',
            'woltka/databases/*'],
        'sortmerna': ['qp_woltka/sortmerna/databases/*']},
      scripts=['scripts/configure_woltka', 'scripts/start_woltka'],
      extras_require={'test': ["nose >= 0.10.1", "pep8"]},
      install_requires=['click >= 3.3', 'future', 'pandas >= 0.15',
                        'h5py >= 2.3.1', 'biom-format',
                        'woltka @ https://github.com/'
                        'qiyunzhu/woltka/archive/master.zip'],
      classifiers=classifiers
      )
