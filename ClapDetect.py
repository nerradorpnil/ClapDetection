import pyaudio
import struct
import math


class ClapListener(object):
    CLAP_VOL_THRESHOLD = 0.05               # clap sensitivity
    FORMAT             = pyaudio.paInt16    # audio format type
    BLOCK_VOL_PERCENT  = 1.0/32768.0        # converts value of int to percentage
    CHANNELS           = 2                  # audio channel number/type
    BAUD_RATE          = 44100
    POLL_TIME          = 0.08               # percentage of a second
    VOL_POLLS_PER_BLK  = int(BAUD_RATE * POLL_TIME)
    DUR_NOT_CLAP       = 0.15/POLL_TIME
    
    def __init__(self):
        self.pa                 = pyaudio.PyAudio()
        self.stream             = self.openMicStream()
        self.clapVolThreshold   = self.CLAP_VOL_THRESHOLD
        self.noisyCount         = self.DUR_NOT_CLAP + 1
        self.quietCount         = 0
        self.errorCount         = 0
        self.clapCount          = 0

    def stop(self):
        self.stream.close()

    def getAvgVol(self, block):
        count = len(block)/2
        format = "%dh"%(count)
        shorts = struct.unpack(format, block)

        squareValSum = 0.0

        for i in shorts:
            p = i * self.BLOCK_VOL_PERCENT
            squareValSum = squareValSum + (p * p)

        avgVal = math.sqrt(squareValSum / count)
        return avgVal

    def findInputDevice(self):
        deviceIndex = None
        for i in range(self.pa.get_device_count()):
            deviceInfo = self.pa.get_device_info_by_index(i)
            print("Device %d: %s" %(i,deviceInfo["name"]))

            for j in ["mic","input"]:
                if j in deviceInfo["name"].lower():
                    print("Found an input device: %d - %s" %(i,deviceInfo["name"]))
                    deviceIndex = i
                    return deviceIndex

        if deviceIndex == None:
            print("no preferred input found; using default input device.")

        return deviceIndex

    def openMicStream(self):
        deviceIndex = self.findInputDevice()

        stream = self.pa.open(format = self.FORMAT, channels = self.CHANNELS, rate = self.BAUD_RATE, input = True,
                              input_device_index = deviceIndex, frames_per_buffer = self.VOL_POLLS_PER_BLK)

        return stream

    def clapDetected(self):
        print("Get Clapped, Fool")
        
    
    def listen(self):
        try:
            block = self.stream.read(self.VOL_POLLS_PER_BLK)
        except IOError as e:
            self.errorcount = self.errorcount + 1
            self.noisycount = 1
            print("Error Recording")
            return False

        detected = False
        volume = self.getAvgVol(block)
        if volume > self.clapVolThreshold:
            #loud, Clap
            self.noisyCount = self.noisyCount + 1
            self.quietCount = 0
            
        else:
            #soft, no clap
            if 1 <= self.noisyCount <= self.DUR_NOT_CLAP:
                self.clapDetected()
                detected = True
            self.noisyCount = 0
            self.quietCount = self.quietCount +1
        return detected

    def getClapCount():
        return self.clapCount

    def clearClapCount():
        self.clapCount = 0;













