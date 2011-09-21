# -*- coding: utf-8 -*-
from setuptools import setup, find_packages
import os

version = open(os.path.join("Products", "PloneSlideShow", "version.txt")).read().strip()

setup(name='Products.PloneSlideShow',
      version=version,
      description="PloneSlideShow is a tool for presentation of random images and news in Plone sites.",
      long_description=open(os.path.join("Products", "PloneSlideShow", "README.txt")).read() + "\n" +
                       open(os.path.join("docs", "HISTORY.txt")).read(),
      # Get more strings from http://www.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
        "Framework :: Plone",
        "Framework :: Zope2",
        "Framework :: Zope3",
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",
        ],
      keywords='web zope plone random slider',
      author='Cleber J Santos',
      author_email='cleber@cleberjsantos.com.br',
      url='http://www.cleberjsantos.com.br/',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['Products', 'Products.PloneSlideShow'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          'Products.CMFPublicator',
      ],
      entry_points="""
      # -*- Entry points: -*-

      [z3c.autoinclude.plugin]
      target = plone
      """,
      )
