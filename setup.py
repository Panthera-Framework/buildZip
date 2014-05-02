#!/usr/bin/env python
#-*- encoding: utf-8 -*-

"""
    Setup for Panthera buildZip application
"""
 
from distutils.core import setup 

setup(
    name='Panthera zip/targz builder from git',
    author='Damian Kęska',
    author_email='damian@darbs.pl',
    scripts=['panthera-buildZip']
)
