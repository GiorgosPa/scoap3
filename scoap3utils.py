# -*- coding: utf-8 -*-
##
## This file is part of Invenio.
## Copyright (C) 2013 CERN.
##
## Invenio is free software; you can redistribute it and/or
## modify it under the terms of the GNU General Public License as
## published by the Free Software Foundation; either version 2 of the
## License, or (at your option) any later version.
##
## Invenio is distributed in the hope that it will be useful, but
## WITHOUT ANY WARRANTY; without even the implied warranty of
## MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
## General Public License for more details.
##
## You should have received a copy of the GNU General Public License
## along with Invenio; if not, write to the Free Software Foundation, Inc.,
## 59 Temple Place, Suite 330, Boston, MA 02111-1307, USA.

"""
Set of utilities for the SCOAP3 project.
"""

import logging


def xml_to_text(xml):
    if xml.nodeType == xml.TEXT_NODE:
        return xml.wholeText.encode('utf-8')
    elif xml.hasChildNodes():
        return ''.join(xml_to_text(child) for child in xml.childNodes)
    return ''


def get_value_in_tag(xml, tag):
    tag_elements = xml.getElementsByTagName(tag)
    if tag_elements:
        return xml_to_text(tag_elements[0])
    else:
        return ""


# Creates a logger object
def create_logger(name):
    logger = logging.getLogger('contrast_out_connector')
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    fh = logging.FileHandler(filename=name)
    fh.setFormatter(formatter)
    logger.addHandler(fh)
    logger.setLevel(logging.DEBUG)
    return logger


class MD5Error(Exception):
    def __init__(self, value):
        self.value = value
