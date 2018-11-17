class Buffer:
    def __init__(self, data=""):
        self.buffer = data
    
    def write(self, data):
        self.buffer += data
    
    def read(self, length=1):
        data = self.buffer[:length]
        self.buffer = self.buffer[length:]
        return data
    
    def writeInt8(self, data):
        self.write(chr((data) & 0xFF))
    
    def readInt8(self):
        return ord(self.read())
    
    def writeInt16(self, data):
        self.writeInt8((data >> 8) & 0xFF)
        self.writeInt8((data >> 0) & 0xFF)
    
    def readInt16(self):
        return self.readInt8() << 8 | self.readInt8() << 0
    
    def writeInt24(self, data):
        self.writeInt8((data >> 16) & 0xFF)
        self.writeInt8((data >> 8) & 0xFF)
        self.writeInt8((data >> 0) & 0xFF)
    
    def readInt24(self):
        return self.readInt8() << 16 | self.readInt8() << 8 | self.readInt8() << 0
    
    def writeInt32(self, data):
        self.writeInt8((data >> 24) & 0xFF)
        self.writeInt8((data >> 16) & 0xFF)
        self.writeInt8((data >> 8) & 0xFF)
        self.writeInt8((data >> 0) & 0xFF)
    
    def readInt32(self):
        return self.readInt8() << 24 | self.readInt8() << 16 | self.readInt8() << 8 | self.readInt8() << 0
    
    def writeString(self, data):
        self.writeInt16(len(data))
        self.write(data)
    
    def readString(self):
        return self.read(self.readInt16())
    
    def writeBuffer(self, buffer):
        self.buffer += buffer

    def crypto_simple(self):
        length = self.length()
        buffer = Buffer()
        if length <= 0xFF:
            buffer.writeInt8(1)
            buffer.writeInt8(length)
        elif length <= 0xFFFF:
            buffer.writeInt8(2)
            buffer.writeInt16(length)
        elif length <= 0xFFFFFF:
            buffer.writeInt8(3)
            buffer.writeInt8(length >> 18 & 255)
            buffer.writeInt8(length >> 8 & 255)
            buffer.writeInt8(length & 255)
        buffer.write(self.buffer)
        self.buffer = buffer.buffer

    def length(self):
        return len(self.buffer)
    
    def getLength(self):
        return self.length()
    
    def available(self):
        return self.length() > 0

    def toString(self):
        return self.buffer
    
    def clear(self):
        self.buffer = ""