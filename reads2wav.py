# coding=utf-8
import wave
import sys

seq = ""
with open(sys.argv[1], 'r') as readFile:
    for line in readFile:
        if(not line[0] == '>'):
            seq += line.rstrip("\n")

length = len(seq)
out = wave.open("read.wav", "wb")

out.setframerate(44100)
out.setnchannels(1)
out.setsampwidth(2)


def nc2level(nucleotide, byte_value):
    convert = {'A':-10, 'C': -5, 'G': 5, 'T': 10}
    incremnt = 0
    if nucleotide in convert:
        increment = convert[nucleotide]

    value = (int.from_bytes(byte_value, byteorder='big') + increment) %256
    return(value.to_bytes(1, byteorder='big'))


time = 10
maxFrame = time * 44100
level = (127).to_bytes(1, byteorder='big')
frames = 0
for nc in seq:
    waveData = nc2level(nc,level)
#    print(int.from_bytes(waveData, byteorder = 'big'))
    out.writeframes(waveData)
    out.writeframes(waveData)
    frames += 1
    if(frames >= maxFrame):
    	break
out.close()
