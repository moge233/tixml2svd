#!/bin/env python3
import argparse

from lxml import etree


if __name__ == '__main__':

    arg_parser = argparse.ArgumentParser(description="validate an XML against an XSD Schema file")

    arg_parser.add_argument('schema_file', metavar='sf',
                            type=argparse.FileType('r'),
                            help='XSD Schema file')
    arg_parser.add_argument('xml_file', metavar='xf',
                            type=argparse.FileType('r'),
                            help='XML file to validate')

    args = arg_parser.parse_args()
    schema_file = args.schema_file
    xml_file = args.xml_file

    schema = etree.XMLSchema(file=schema_file.name)
    xml = etree.parse(xml_file.name)
    print(schema.validate(xml))
