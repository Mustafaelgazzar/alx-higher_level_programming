#!/usr/bin/python3
"""Defining read_file function"""

def read_file(filename=""):
    """read filename with utf-8"""
    with open(filename, endcoding=' utf-8') as f:
        print(f.read(), end"")
