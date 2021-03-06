#
# This class is automatically generated by mig. DO NOT EDIT THIS FILE.
# This class implements a Python interface to the 'OscilloscopeMsg'
# message type.
#

import tinyos.message.Message

# The default size of this message type in bytes.
DEFAULT_MESSAGE_SIZE = 10

# The Active Message type associated with this message.
AM_TYPE = 147

class OscilloscopeMsg(tinyos.message.Message.Message):
    # Create a new OscilloscopeMsg of size 10.
    def __init__(self, data="", addr=None, gid=None, base_offset=0, data_length=10):
        tinyos.message.Message.Message.__init__(self, data, addr, gid, base_offset, data_length)
        self.amTypeSet(AM_TYPE)
    
    # Get AM_TYPE
    def get_amType(cls):
        return AM_TYPE
    
    get_amType = classmethod(get_amType)
    
    #
    # Return a String representation of this message. Includes the
    # message type name and the non-indexed field values.
    #
    def __str__(self):
        s = "Message <OscilloscopeMsg> \n"
        try:
            s += "  [version=0x%x]\n" % (self.get_version())
        except:
            pass
        try:
            s += "  [interval=0x%x]\n" % (self.get_interval())
        except:
            pass
        try:
            s += "  [id=0x%x]\n" % (self.get_id())
        except:
            pass
        try:
            s += "  [count=0x%x]\n" % (self.get_count())
        except:
            pass
        try:
            s += "  [readings=";
            for i in range(0, 1):
                s += "0x%x " % (self.getElement_readings(i) & 0xffff)
            s += "]\n";
        except:
            pass
        return s

    # Message-type-specific access methods appear below.

    #
    # Accessor methods for field: version
    #   Field type: int
    #   Offset (bits): 0
    #   Size (bits): 16
    #

    #
    # Return whether the field 'version' is signed (False).
    #
    def isSigned_version(self):
        return False
    
    #
    # Return whether the field 'version' is an array (False).
    #
    def isArray_version(self):
        return False
    
    #
    # Return the offset (in bytes) of the field 'version'
    #
    def offset_version(self):
        return (0 / 8)
    
    #
    # Return the offset (in bits) of the field 'version'
    #
    def offsetBits_version(self):
        return 0
    
    #
    # Return the value (as a int) of the field 'version'
    #
    def get_version(self):
        return self.getUIntElement(self.offsetBits_version(), 16, 1)
    
    #
    # Set the value of the field 'version'
    #
    def set_version(self, value):
        self.setUIntElement(self.offsetBits_version(), 16, value, 1)
    
    #
    # Return the size, in bytes, of the field 'version'
    #
    def size_version(self):
        return (16 / 8)
    
    #
    # Return the size, in bits, of the field 'version'
    #
    def sizeBits_version(self):
        return 16
    
    #
    # Accessor methods for field: interval
    #   Field type: int
    #   Offset (bits): 16
    #   Size (bits): 16
    #

    #
    # Return whether the field 'interval' is signed (False).
    #
    def isSigned_interval(self):
        return False
    
    #
    # Return whether the field 'interval' is an array (False).
    #
    def isArray_interval(self):
        return False
    
    #
    # Return the offset (in bytes) of the field 'interval'
    #
    def offset_interval(self):
        return (16 / 8)
    
    #
    # Return the offset (in bits) of the field 'interval'
    #
    def offsetBits_interval(self):
        return 16
    
    #
    # Return the value (as a int) of the field 'interval'
    #
    def get_interval(self):
        return self.getUIntElement(self.offsetBits_interval(), 16, 1)
    
    #
    # Set the value of the field 'interval'
    #
    def set_interval(self, value):
        self.setUIntElement(self.offsetBits_interval(), 16, value, 1)
    
    #
    # Return the size, in bytes, of the field 'interval'
    #
    def size_interval(self):
        return (16 / 8)
    
    #
    # Return the size, in bits, of the field 'interval'
    #
    def sizeBits_interval(self):
        return 16
    
    #
    # Accessor methods for field: id
    #   Field type: int
    #   Offset (bits): 32
    #   Size (bits): 16
    #

    #
    # Return whether the field 'id' is signed (False).
    #
    def isSigned_id(self):
        return False
    
    #
    # Return whether the field 'id' is an array (False).
    #
    def isArray_id(self):
        return False
    
    #
    # Return the offset (in bytes) of the field 'id'
    #
    def offset_id(self):
        return (32 / 8)
    
    #
    # Return the offset (in bits) of the field 'id'
    #
    def offsetBits_id(self):
        return 32
    
    #
    # Return the value (as a int) of the field 'id'
    #
    def get_id(self):
        return self.getUIntElement(self.offsetBits_id(), 16, 1)
    
    #
    # Set the value of the field 'id'
    #
    def set_id(self, value):
        self.setUIntElement(self.offsetBits_id(), 16, value, 1)
    
    #
    # Return the size, in bytes, of the field 'id'
    #
    def size_id(self):
        return (16 / 8)
    
    #
    # Return the size, in bits, of the field 'id'
    #
    def sizeBits_id(self):
        return 16
    
    #
    # Accessor methods for field: count
    #   Field type: int
    #   Offset (bits): 48
    #   Size (bits): 16
    #

    #
    # Return whether the field 'count' is signed (False).
    #
    def isSigned_count(self):
        return False
    
    #
    # Return whether the field 'count' is an array (False).
    #
    def isArray_count(self):
        return False
    
    #
    # Return the offset (in bytes) of the field 'count'
    #
    def offset_count(self):
        return (48 / 8)
    
    #
    # Return the offset (in bits) of the field 'count'
    #
    def offsetBits_count(self):
        return 48
    
    #
    # Return the value (as a int) of the field 'count'
    #
    def get_count(self):
        return self.getUIntElement(self.offsetBits_count(), 16, 1)
    
    #
    # Set the value of the field 'count'
    #
    def set_count(self, value):
        self.setUIntElement(self.offsetBits_count(), 16, value, 1)
    
    #
    # Return the size, in bytes, of the field 'count'
    #
    def size_count(self):
        return (16 / 8)
    
    #
    # Return the size, in bits, of the field 'count'
    #
    def sizeBits_count(self):
        return 16
    
    #
    # Accessor methods for field: readings
    #   Field type: int[]
    #   Offset (bits): 64
    #   Size of each element (bits): 16
    #

    #
    # Return whether the field 'readings' is signed (False).
    #
    def isSigned_readings(self):
        return False
    
    #
    # Return whether the field 'readings' is an array (True).
    #
    def isArray_readings(self):
        return True
    
    #
    # Return the offset (in bytes) of the field 'readings'
    #
    def offset_readings(self, index1):
        offset = 64
        if index1 < 0 or index1 >= 1:
            raise IndexError
        offset += 0 + index1 * 16
        return (offset / 8)
    
    #
    # Return the offset (in bits) of the field 'readings'
    #
    def offsetBits_readings(self, index1):
        offset = 64
        if index1 < 0 or index1 >= 1:
            raise IndexError
        offset += 0 + index1 * 16
        return offset
    
    #
    # Return the entire array 'readings' as a int[]
    #
    def get_readings(self):
        tmp = [None]*1
        for index0 in range (0, self.numElements_readings(0)):
                tmp[index0] = self.getElement_readings(index0)
        return tmp
    
    #
    # Set the contents of the array 'readings' from the given int[]
    #
    def set_readings(self, value):
        for index0 in range(0, len(value)):
            self.setElement_readings(index0, value[index0])

    #
    # Return an element (as a int) of the array 'readings'
    #
    def getElement_readings(self, index1):
        return self.getUIntElement(self.offsetBits_readings(index1), 16, 1)
    
    #
    # Set an element of the array 'readings'
    #
    def setElement_readings(self, index1, value):
        self.setUIntElement(self.offsetBits_readings(index1), 16, value, 1)
    
    #
    # Return the total size, in bytes, of the array 'readings'
    #
    def totalSize_readings(self):
        return (16 / 8)
    
    #
    # Return the total size, in bits, of the array 'readings'
    #
    def totalSizeBits_readings(self):
        return 16
    
    #
    # Return the size, in bytes, of each element of the array 'readings'
    #
    def elementSize_readings(self):
        return (16 / 8)
    
    #
    # Return the size, in bits, of each element of the array 'readings'
    #
    def elementSizeBits_readings(self):
        return 16
    
    #
    # Return the number of dimensions in the array 'readings'
    #
    def numDimensions_readings(self):
        return 1
    
    #
    # Return the number of elements in the array 'readings'
    #
    def numElements_readings():
        return 1
    
    #
    # Return the number of elements in the array 'readings'
    # for the given dimension.
    #
    def numElements_readings(self, dimension):
        array_dims = [ 1,  ]
        if dimension < 0 or dimension >= 1:
            raise IndexException
        if array_dims[dimension] == 0:
            raise IndexError
        return array_dims[dimension]
    
