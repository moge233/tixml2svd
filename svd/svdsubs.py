#!/usr/bin/env python

#
# Generated Tue Mar 15 23:42:49 2022 by generateDS.py version 2.35.17.
# Python 3.9.5 (default, Nov 23 2021, 15:27:38)  [GCC 9.3.0]
#
# Command line options:
#   ('-o', 'svd.py')
#   ('-s', 'svdsubs.py')
#   ('--export', 'write literal etree validate')
#
# Command line arguments:
#   CMSIS-SVD.xsd
#
# Command line:
#   /home/matt/.virtualenvs/tixml2svd/bin/generateDS -o "svd.py" -s "svdsubs.py" --export="write literal etree validate" CMSIS-SVD.xsd
#
# Current working directory (os.getcwd()):
#   svd
#

import os
import sys
from lxml import etree as etree_

import ??? as supermod

def parsexml_(infile, parser=None, **kwargs):
    if parser is None:
        # Use the lxml ElementTree compatible parser so that, e.g.,
        #   we ignore comments.
        parser = etree_.ETCompatXMLParser()
    try:
        if isinstance(infile, os.PathLike):
            infile = os.path.join(infile)
    except AttributeError:
        pass
    doc = etree_.parse(infile, parser=parser, **kwargs)
    return doc

def parsexmlstring_(instring, parser=None, **kwargs):
    if parser is None:
        # Use the lxml ElementTree compatible parser so that, e.g.,
        #   we ignore comments.
        try:
            parser = etree_.ETCompatXMLParser()
        except AttributeError:
            # fallback to xml.etree
            parser = etree_.XMLParser()
    element = etree_.fromstring(instring, parser=parser, **kwargs)
    return element

#
# Globals
#

ExternalEncoding = ''
SaveElementTreeNode = True

#
# Data representation classes
#


class writeConstraintTypeSub(supermod.writeConstraintType):
    def __init__(self, writeAsRead=None, useEnumeratedValues=None, range=None, **kwargs_):
        super(writeConstraintTypeSub, self).__init__(writeAsRead, useEnumeratedValues, range,  **kwargs_)
supermod.writeConstraintType.subclass = writeConstraintTypeSub
# end class writeConstraintTypeSub


class addressBlockTypeSub(supermod.addressBlockType):
    def __init__(self, offset=None, size=None, usage=None, protection=None, **kwargs_):
        super(addressBlockTypeSub, self).__init__(offset, size, usage, protection,  **kwargs_)
supermod.addressBlockType.subclass = addressBlockTypeSub
# end class addressBlockTypeSub


class interruptTypeSub(supermod.interruptType):
    def __init__(self, name=None, description=None, value=None, **kwargs_):
        super(interruptTypeSub, self).__init__(name, description, value,  **kwargs_)
supermod.interruptType.subclass = interruptTypeSub
# end class interruptTypeSub


class cpuTypeSub(supermod.cpuType):
    def __init__(self, name=None, revision=None, endian=None, mpuPresent=None, fpuPresent=None, fpuDP=None, icachePresent=None, dcachePresent=None, itcmPresent=None, dtcmPresent=None, vtorPresent=None, nvicPrioBits=None, vendorSystickConfig=None, deviceNumInterrupts=None, sauNumRegions=None, sauRegionsConfig=None, **kwargs_):
        super(cpuTypeSub, self).__init__(name, revision, endian, mpuPresent, fpuPresent, fpuDP, icachePresent, dcachePresent, itcmPresent, dtcmPresent, vtorPresent, nvicPrioBits, vendorSystickConfig, deviceNumInterrupts, sauNumRegions, sauRegionsConfig,  **kwargs_)
supermod.cpuType.subclass = cpuTypeSub
# end class cpuTypeSub


class enumeratedValuesTypeSub(supermod.enumeratedValuesType):
    def __init__(self, derivedFrom=None, name=None, usage=None, enumeratedValue=None, **kwargs_):
        super(enumeratedValuesTypeSub, self).__init__(derivedFrom, name, usage, enumeratedValue,  **kwargs_)
supermod.enumeratedValuesType.subclass = enumeratedValuesTypeSub
# end class enumeratedValuesTypeSub


class fieldTypeSub(supermod.fieldType):
    def __init__(self, derivedFrom=None, name=None, description=None, lsb=None, msb=None, bitOffset=None, bitWidth=None, bitRange=None, access=None, modifiedWriteValues=None, writeConstraint=None, readAction=None, enumeratedValues=None, **kwargs_):
        super(fieldTypeSub, self).__init__(derivedFrom, name, description, lsb, msb, bitOffset, bitWidth, bitRange, access, modifiedWriteValues, writeConstraint, readAction, enumeratedValues,  **kwargs_)
supermod.fieldType.subclass = fieldTypeSub
# end class fieldTypeSub


class fieldsTypeSub(supermod.fieldsType):
    def __init__(self, field=None, **kwargs_):
        super(fieldsTypeSub, self).__init__(field,  **kwargs_)
supermod.fieldsType.subclass = fieldsTypeSub
# end class fieldsTypeSub


class registerTypeSub(supermod.registerType):
    def __init__(self, derivedFrom=None, dim=None, dimIncrement=None, dimIndex=None, name=None, displayName=None, description=None, alternateGroup=None, alternateRegister=None, addressOffset=None, size=None, access=None, protection=None, resetValue=None, resetMask=None, dataType=None, modifiedWriteValues=None, writeConstraint=None, readAction=None, fields=None, **kwargs_):
        super(registerTypeSub, self).__init__(derivedFrom, dim, dimIncrement, dimIndex, name, displayName, description, alternateGroup, alternateRegister, addressOffset, size, access, protection, resetValue, resetMask, dataType, modifiedWriteValues, writeConstraint, readAction, fields,  **kwargs_)
supermod.registerType.subclass = registerTypeSub
# end class registerTypeSub


class clusterTypeSub(supermod.clusterType):
    def __init__(self, derivedFrom=None, dim=None, dimIncrement=None, dimIndex=None, name=None, description=None, alternateCluster=None, headerStructName=None, addressOffset=None, size=None, access=None, protection=None, resetValue=None, resetMask=None, register=None, cluster=None, **kwargs_):
        super(clusterTypeSub, self).__init__(derivedFrom, dim, dimIncrement, dimIndex, name, description, alternateCluster, headerStructName, addressOffset, size, access, protection, resetValue, resetMask, register, cluster,  **kwargs_)
supermod.clusterType.subclass = clusterTypeSub
# end class clusterTypeSub


class registersTypeSub(supermod.registersType):
    def __init__(self, cluster=None, register=None, **kwargs_):
        super(registersTypeSub, self).__init__(cluster, register,  **kwargs_)
supermod.registersType.subclass = registersTypeSub
# end class registersTypeSub


class peripheralTypeSub(supermod.peripheralType):
    def __init__(self, derivedFrom=None, dim=None, dimIncrement=None, dimIndex=None, name=None, version=None, description=None, alternatePeripheral=None, groupName=None, prependToName=None, appendToName=None, headerStructName=None, disableCondition=None, baseAddress=None, size=None, access=None, protection=None, resetValue=None, resetMask=None, addressBlock=None, interrupt=None, registers=None, **kwargs_):
        super(peripheralTypeSub, self).__init__(derivedFrom, dim, dimIncrement, dimIndex, name, version, description, alternatePeripheral, groupName, prependToName, appendToName, headerStructName, disableCondition, baseAddress, size, access, protection, resetValue, resetMask, addressBlock, interrupt, registers,  **kwargs_)
supermod.peripheralType.subclass = peripheralTypeSub
# end class peripheralTypeSub


class deviceSub(supermod.device):
    def __init__(self, schemaVersion=None, vendor=None, vendorID=None, name=None, series=None, version=None, description=None, licenseText=None, cpu=None, headerSystemFilename=None, headerDefinitionsPrefix=None, addressUnitBits=None, width=None, size=None, access=None, protection=None, resetValue=None, resetMask=None, peripherals=None, vendorExtensions=None, **kwargs_):
        super(deviceSub, self).__init__(schemaVersion, vendor, vendorID, name, series, version, description, licenseText, cpu, headerSystemFilename, headerDefinitionsPrefix, addressUnitBits, width, size, access, protection, resetValue, resetMask, peripherals, vendorExtensions,  **kwargs_)
supermod.device.subclass = deviceSub
# end class deviceSub


class rangeTypeSub(supermod.rangeType):
    def __init__(self, minimum=None, maximum=None, **kwargs_):
        super(rangeTypeSub, self).__init__(minimum, maximum,  **kwargs_)
supermod.rangeType.subclass = rangeTypeSub
# end class rangeTypeSub


class sauRegionsConfigTypeSub(supermod.sauRegionsConfigType):
    def __init__(self, enabled=True, protectionWhenDisabled='s', region=None, **kwargs_):
        super(sauRegionsConfigTypeSub, self).__init__(enabled, protectionWhenDisabled, region,  **kwargs_)
supermod.sauRegionsConfigType.subclass = sauRegionsConfigTypeSub
# end class sauRegionsConfigTypeSub


class regionTypeSub(supermod.regionType):
    def __init__(self, enabled=True, name=None, base=None, limit=None, access=None, **kwargs_):
        super(regionTypeSub, self).__init__(enabled, name, base, limit, access,  **kwargs_)
supermod.regionType.subclass = regionTypeSub
# end class regionTypeSub


class enumeratedValueTypeSub(supermod.enumeratedValueType):
    def __init__(self, name=None, description=None, value=None, isDefault=None, **kwargs_):
        super(enumeratedValueTypeSub, self).__init__(name, description, value, isDefault,  **kwargs_)
supermod.enumeratedValueType.subclass = enumeratedValueTypeSub
# end class enumeratedValueTypeSub


class peripheralsTypeSub(supermod.peripheralsType):
    def __init__(self, peripheral=None, **kwargs_):
        super(peripheralsTypeSub, self).__init__(peripheral,  **kwargs_)
supermod.peripheralsType.subclass = peripheralsTypeSub
# end class peripheralsTypeSub


class vendorExtensionsTypeSub(supermod.vendorExtensionsType):
    def __init__(self, anytypeobjs_=None, **kwargs_):
        super(vendorExtensionsTypeSub, self).__init__(anytypeobjs_,  **kwargs_)
supermod.vendorExtensionsType.subclass = vendorExtensionsTypeSub
# end class vendorExtensionsTypeSub


def get_root_tag(node):
    tag = supermod.Tag_pattern_.match(node.tag).groups()[-1]
    rootClass = None
    rootClass = supermod.GDSClassesMapping.get(tag)
    if rootClass is None and hasattr(supermod, tag):
        rootClass = getattr(supermod, tag)
    return tag, rootClass


def parse(inFilename, silence=False):
    parser = None
    doc = parsexml_(inFilename, parser)
    rootNode = doc.getroot()
    rootTag, rootClass = get_root_tag(rootNode)
    if rootClass is None:
        rootTag = 'writeConstraintType'
        rootClass = supermod.writeConstraintType
    rootObj = rootClass.factory()
    rootObj.build(rootNode)
    # Enable Python to collect the space used by the DOM.
    if not SaveElementTreeNode:
        doc = None
        rootNode = None
    if not silence:
        sys.stdout.write('<?xml version="1.0" ?>\n')
        rootObj.export(
            sys.stdout, 0, name_=rootTag,
            namespacedef_='',
            pretty_print=True)
    return rootObj


def parseEtree(inFilename, silence=False):
    parser = None
    doc = parsexml_(inFilename, parser)
    rootNode = doc.getroot()
    rootTag, rootClass = get_root_tag(rootNode)
    if rootClass is None:
        rootTag = 'writeConstraintType'
        rootClass = supermod.writeConstraintType
    rootObj = rootClass.factory()
    rootObj.build(rootNode)
    mapping = {}
    rootElement = rootObj.to_etree(None, name_=rootTag, mapping_=mapping)
    reverse_mapping = rootObj.gds_reverse_node_mapping(mapping)
    # Enable Python to collect the space used by the DOM.
    if not SaveElementTreeNode:
        doc = None
        rootNode = None
    if not silence:
        content = etree_.tostring(
            rootElement, pretty_print=True,
            xml_declaration=True, encoding="utf-8")
        sys.stdout.write(content)
        sys.stdout.write('\n')
    return rootObj, rootElement, mapping, reverse_mapping


def parseString(inString, silence=False):
    if sys.version_info.major == 2:
        from StringIO import StringIO
    else:
        from io import BytesIO as StringIO
    parser = None
    rootNode= parsexmlstring_(inString, parser)
    rootTag, rootClass = get_root_tag(rootNode)
    if rootClass is None:
        rootTag = 'writeConstraintType'
        rootClass = supermod.writeConstraintType
    rootObj = rootClass.factory()
    rootObj.build(rootNode)
    # Enable Python to collect the space used by the DOM.
    if not SaveElementTreeNode:
        rootNode = None
    if not silence:
        sys.stdout.write('<?xml version="1.0" ?>\n')
        rootObj.export(
            sys.stdout, 0, name_=rootTag,
            namespacedef_='')
    return rootObj


def parseLiteral(inFilename, silence=False):
    parser = None
    doc = parsexml_(inFilename, parser)
    rootNode = doc.getroot()
    rootTag, rootClass = get_root_tag(rootNode)
    if rootClass is None:
        rootTag = 'writeConstraintType'
        rootClass = supermod.writeConstraintType
    rootObj = rootClass.factory()
    rootObj.build(rootNode)
    # Enable Python to collect the space used by the DOM.
    if not SaveElementTreeNode:
        doc = None
        rootNode = None
    if not silence:
        sys.stdout.write('#from ??? import *\n\n')
        sys.stdout.write('import ??? as model_\n\n')
        sys.stdout.write('rootObj = model_.rootClass(\n')
        rootObj.exportLiteral(sys.stdout, 0, name_=rootTag)
        sys.stdout.write(')\n')
    return rootObj


USAGE_TEXT = """
Usage: python ???.py <infilename>
"""


def usage():
    print(USAGE_TEXT)
    sys.exit(1)


def main():
    args = sys.argv[1:]
    if len(args) != 1:
        usage()
    infilename = args[0]
    parse(infilename)


if __name__ == '__main__':
    #import pdb; pdb.set_trace()
    main()
