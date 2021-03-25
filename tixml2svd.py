#! /usr/bin/env python


import argparse
import sys
import xml.etree.ElementTree as Et

from lxml import etree
import xmlschema

# SVD schema generated from generateDS
from svd import svd


class Device:

    def __init__(self, description=None, id=None, HW_revision=None,
                 desc=None):
        self.description = description
        self.id=id
        self.HW_revision=HW_revision
        self.desc=desc


    def __repr__(self):
        r = 'Device(description={}, id={}, HW_revision={}, desc={})'
        return r.format(self.description, self.id,
                        self.HW_revision, self.desc)


class Cpu:

    def __init__(self, HW_revision=None, XML_version=None, desc=None,
                 description=None, deviceSim=None, id=None, isa=None):
        self.HW_revision = HW_revision
        self.XML_version = XML_version
        self.desc = desc
        self.description = description
        self.deviceSim = deviceSim
        self.id = id
        self.isa = isa

    def __repr__(self):
        r = 'Cpu(HW_revision={}, XML_version={}, desc={}, description={},\
                deviceSim={}, id={}, isa={})'
        return r.format(self.HW_revision, self.XML_version, self.desc,
                        self.description, self.deviceSim, self.id,
                        self.isa)


class Property:

    def __init__(self, Type=None, Value=None, id=None):
        self.Type = Type
        self.Value = Value
        self.id = id

    def __repr__(self):
        r = 'Property(Type={}, Value={}, id={})'
        return r.format(self.Type, self.Value, self.id)


class ModuleRegister:

    def __init__(self, id=None, width=None, offset=None, description=None,
                bitfields=None, acronym=None):
        self.id = id
        self.width = width
        self.offset = offset
        self.description = description
        self.acronym = acronym

        if not bitfields:
            self.bitfields = list()
        else:
            self.bitfields = bitfields

    def __repr__(self):
        r = 'ModuleRegister(id={}, width={}, offset={}, description={},\
 bitfields={}, acronym={})'
        return r.format(self.id, self.width, self.offset, self.description,
                        self.bitfields, self.acronym)


class ModuleBitfield:

    def __init__(self, id=None, description=None, begin=None, end=None,
                 width=None, rwaccess=None):
        self.id = id
        self.description = description
        self.begin = begin
        self.end = end
        self.width = width
        self.rwaccess = rwaccess

    def __repr__(self):
        r = 'ModuleBitfield(id={}, description={}, begin={}, end={},\
 width={}, rwaccess={}'
        return r.format(self.id, self.description, self.begin, self.end,
                        self.width, self.rwaccess)


class Instance:

    def __init__(self, HW_revision=None, accessnumbytes=None, baseaddr=None,
                 description=None, href=None, id=None, xml=None,
                 permissions=None, xmlpath=None, registers=None):
        self.HW_revision = HW_revision
        self.accessnumbytes = accessnumbytes
        self.baseaddr = baseaddr
        self.description = description
        self.href = href
        self.id = id
        self.xml = xml
        self.permissions = permissions
        self.xmlpath = xmlpath

        if not registers:
            self.registers = list()
        else:
            self.registers = registers

    def __repr__(self):
        r = 'Instance(HW_revision={}, accessnumbytes={}, baseaddr={},\
 description={}, href={}, id={}, xml={}, permissions={},\
 xmlpath={}, registers={})'
        return r.format(self.HW_revision, self.accessnumbytes,
                        self.baseaddr, self.description, self.href,
                        self.id, self.xml, self.permissions,
                        self.xmlpath, self.registers)


class Router:

    def __init__(self, HW_revision=None, XML_version=None, description=None,
                 id=None, isa=None):
        self.HW_revision = HW_revision
        self.XML_version = XML_version
        self.description = description
        self.id = id
        self.isa = isa

    def __repr__(self):
        r = 'Router(HW_revision={}, XML_version={}, description={}, id={}, isa={})'
        return r.format(self.HW_revision, self.XML_version,
                        self.description, self.id, self.isa)


class Interrupt:

    def __init__(self, name=None, description=None, value=None):
        self.name = name
        self.description = description
        self.value = value

    def __repr__(self):
        r = 'Interrupt(name={}, description={}, value={})'
        return r.format(self.name, self.description, self.value)


def parse_device_file(device_file):
    device_tree = Et.parse(device_file)
    db = TiXmlParser()

    for item in device_tree.iter():
        if item.tag == 'device':
            for (k, v) in item.items():
                setattr(db.device, k, v)
        elif item.tag == 'property':
            p = Property()
            for (k, v) in item.items():
                setattr(p, k, v)
            db.properties.append(p)
        elif item.tag == 'instance':
            i = Instance()
            for (k, v) in item.items():
                setattr(i, k, v)
            db.instances.append(i)
        elif item.tag == 'router':
            r = Router()
            for (k, v) in item.items():
                setattr(r, k, v)
            db.routers.append(r)
        elif item.tag == 'cpu':
            for (k, v) in item.items():
                setattr(db.cpu, k, v)
        else:
            pass # ignore subpaths

    return db


def parse_module_file(path):
    '''
    Parse the module file provided in the href field.
    '''
    if path[:2] == '..':
        path = path[3:]
    path = './targetdb/' + path

    module_registers = list()

    module_tree = Et.parse(path)
    module_root = module_tree.getroot()

    for item in module_root:
        r = ModuleRegister()
        for (k, v) in item.items():
            setattr(r, k, v)

        # Registers cannot have blank descriptions
        if r.description == '':
            r.description = r.id

        for child in item:
            b = ModuleBitfield()
            for (K, V) in child.items():
                setattr(b, K, V)
            if b.description == '':
                b.description = b.id
            r.bitfields.append(b)
        module_registers.append(r)

    return module_registers


def parse_interrupts(device):
    path = './targetdb/interrupts/{}_interrupts.xml'.format(device)
    interrupts = list()

    interrupts_tree = Et.parse(path)
    interrupts_root = interrupts_tree.getroot()

    for item in interrupts_root:
        i = Interrupt()
        for (k, v) in item.items():
            setattr(i, k, v)
        interrupts.append(i)

    return interrupts


class TiXmlParser:

    def __init__(self):
        self.device = Device()
        self.cpu = Cpu()
        self.properties = []
        self.instances = []
        self.routers = []

    @staticmethod
    def export(svd_device, outfile):
        svd_device.export(outfile, 1)

    def device_to_svd_device(self):
        '''
        Convert the TI device to an SVD device generated from the SVD
        scheme using generateDS
        '''
        d = svd.device()
        d.vendor = 'Texas Instruments'
        d.vendorID = 'TI'
        d.name = self.device.id
        d.description = self.device.description
        d.version = self.device.HW_revision

        filter_string = self.properties[0].Value
        d.series = filter_string

        d.addressUnitBits = 8
        d.width = 32
        d.resetValue = '0x00000000'
        d.resetMask = '0xFFFFFFFF'

        return d

    def module_to_svd_peripheral(self, inst):
        p = svd.peripheralType()

        p.protection = inst.permissions
        if inst.description == '':
            p.description = inst.id
        else:
            p.description = inst.description
        p.baseAddress = inst.baseaddr
        p.name = inst.id
        p.version = inst.HW_revision

        address_block = svd.addressBlockType('0', inst.accessnumbytes,
                                             'registers')
        address_block.protection = inst.permissions
        p.add_addressBlock(address_block)

        # Create registers
        p.registers = svd.registersType()
        access_map = {
            'R'     : 'read-only',
            'RO'    : 'read-only',
            'RW'    : 'read-write',
            'R/W'   : 'read-write',
            'W'     : 'write-only',
            'WO'    : 'write-only',
            'N'     : 'read-write',
        }
        for reg in inst.registers:
            svd_reg = svd.registerType()
            svd_reg.name = reg.id
            svd_reg.description = reg.description
            svd_reg.addressOffset = reg.offset
            svd_reg.size = 32
            svd_reg.access = 'read-write'

            if reg.acronym:
                svd_reg.displayName = reg.acronym
            else:
                svd_reg.displayName = inst.id + '_' + reg.id

            if reg.bitfields:
                svd_reg.fields = svd.fieldsType()
            for b in reg.bitfields:
                svd_bitfield = svd.fieldType()
                svd_bitfield.name = b.id
                svd_bitfield.description = b.description
                # svd_bitfield.bitWidth = b.width
                svd_bitfield.lsb = b.end
                svd_bitfield.msb = b.begin

                svd_bitfield.access = access_map[b.rwaccess]

                svd_reg.fields.add_field(svd_bitfield)

            p.registers.add_register(svd_reg)

        return p

    def cpu_to_svd_cpu(self):
        c = svd.cpuType()
        c.name = 'CM4'
        c.revision = 'r' + self.cpu.HW_revision[0] + 'p' + \
                     self.cpu.HW_revision[-1]
        c.endian = 'little'
        c.mpuPresent = 0
        c.fpuPresent = 0
        c.icachePresent = 0
        c.dtcmPresent = 0
        c.vtorPresent = 0
        c.nvicPrioBits = 8
        c.vendorSystickConfig = 0
        return c


def run(device_file, output_file):
    tdb = parse_device_file(device_file)
    svd_device = tdb.device_to_svd_device()

    svd_device.set_schemaVersion('1.3')
    svd_device.cpu = tdb.cpu_to_svd_cpu()
    svd_device.peripherals = svd.peripheralsType()

    # TODO: parse interrupts for more devices?
    interrupts = parse_interrupts('cc3220sf')
    interrupt_peripheral = svd.peripheralType()
    interrupt_peripheral.name = '_INTERRUPTS'
    interrupt_peripheral.baseAddress = '0'
    # Add a peripheral for interrupts, essentially acting as a container
    for interrupt in interrupts:
        i = svd.interruptType()
        i.name = 'INTERRUPT_' + interrupt.name
        i.description = interrupt.description
        i.value = int(interrupt.value)
        interrupt_peripheral.add_interrupt(i)
        svd_device.peripherals.add_peripheral(interrupt_peripheral)

    for inst in tdb.instances:
        if inst.href[:2] == '..':
            inst.registers = parse_module_file(inst.href)

            peripheral = tdb.module_to_svd_peripheral(inst)
            svd_device.peripherals.add_peripheral(peripheral)

    tdb.export(svd_device, output_file)


if __name__ == '__main__':

    description = '''
    tixml2svd
    Convert a TI targetdb device XML file to an SVD file
    '''

    arg_parser = argparse.ArgumentParser(description=description)
    arg_parser.add_argument('device_file', metavar='df',
                            type=argparse.FileType('r'),
                            help='TI targetdb XML device file')
    arg_parser.add_argument('output_file', metavar='of',
                            type=argparse.FileType('w+'),
                            default=sys.stdout,
                            help='output SVD file')

    args = arg_parser.parse_args()
    device_file = args.device_file
    output_file = args.output_file
    validate = args.validate

    run(device_file, output_file)
