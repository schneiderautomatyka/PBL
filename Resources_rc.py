# -*- coding: utf-8 -*-

# Resource object code
#
# Created by: The Resource Compiler for PyQt5 (Qt v5.15.2)
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore

qt_resource_data = b"\
\x00\x00\x00\x57\
\x3c\
\xb8\x64\x18\xca\xef\x9c\x95\xcd\x21\x1c\xbf\x60\xa1\xbd\xdd\x42\
\x00\x00\x00\x08\x00\x58\xb7\xb9\x00\x00\x00\x00\x69\x00\x00\x00\
\x2e\x03\x00\x00\x00\x0c\x00\x42\x00\x65\x00\x72\x00\x65\x00\x69\
\x00\x74\x08\x00\x00\x00\x00\x06\x00\x00\x00\x05\x52\x65\x61\x64\
\x79\x07\x00\x00\x00\x08\x40\x64\x65\x66\x61\x75\x6c\x74\x01\x88\
\x00\x00\x00\x02\x01\x01\
"

qt_resource_name = b"\
\x00\x08\
\x08\x4e\xb9\x95\
\x00\x6c\
\x00\x61\x00\x6e\x00\x67\x00\x75\x00\x61\x00\x67\x00\x65\
\x00\x09\
\x04\xeb\xd8\xc3\
\x00\x4c\
\x00\x61\x00\x6e\x00\x67\x00\x75\x00\x61\x00\x67\x00\x65\x00\x73\
\x00\x11\
\x04\xf6\x07\x5d\
\x00\x74\
\x00\x72\x00\x61\x00\x6e\x00\x73\x00\x6c\x00\x61\x00\x74\x00\x69\x00\x6f\x00\x6e\x00\x2e\x00\x64\x00\x65\x00\x2e\x00\x71\x00\x6d\
\
"

qt_resource_struct_v1 = b"\
\x00\x00\x00\x00\x00\x02\x00\x00\x00\x01\x00\x00\x00\x01\
\x00\x00\x00\x00\x00\x02\x00\x00\x00\x01\x00\x00\x00\x02\
\x00\x00\x00\x16\x00\x02\x00\x00\x00\x01\x00\x00\x00\x03\
\x00\x00\x00\x2e\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\
"

qt_resource_struct_v2 = b"\
\x00\x00\x00\x00\x00\x02\x00\x00\x00\x01\x00\x00\x00\x01\
\x00\x00\x00\x00\x00\x00\x00\x00\
\x00\x00\x00\x00\x00\x02\x00\x00\x00\x01\x00\x00\x00\x02\
\x00\x00\x00\x00\x00\x00\x00\x00\
\x00\x00\x00\x16\x00\x02\x00\x00\x00\x01\x00\x00\x00\x03\
\x00\x00\x00\x00\x00\x00\x00\x00\
\x00\x00\x00\x2e\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\
\x00\x00\x01\x86\xae\x7d\x5a\xd1\
"

qt_version = [int(v) for v in QtCore.qVersion().split('.')]
if qt_version < [5, 8, 0]:
    rcc_version = 1
    qt_resource_struct = qt_resource_struct_v1
else:
    rcc_version = 2
    qt_resource_struct = qt_resource_struct_v2

def qInitResources():
    QtCore.qRegisterResourceData(rcc_version, qt_resource_struct, qt_resource_name, qt_resource_data)

def qCleanupResources():
    QtCore.qUnregisterResourceData(rcc_version, qt_resource_struct, qt_resource_name, qt_resource_data)

qInitResources()
