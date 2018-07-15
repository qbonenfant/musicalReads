# coding=utf-8
import wave
import sys

seq = ""
with open(sys.argv[1], 'r') as readFile:
    for line in readFile:
        if(not line[0] == '>'):
            seq += line.rstrip("\n")


length = len(seq)
k = 4
out = wave.open("read.wav", "wb")

out.setframerate(44100)
out.setnchannels(1)
out.setsampwidth(2)


def km2level(kmer):
    convert = {'A': 0, 'C': 1, 'G': 2, 'T': 3, 'N': 0}
    value = 0
    for i, n in enumerate(kmer):
        value += convert[n]**i
    level = bytes([value])
#    print(level)
    return(level)


for i in range(length//k):
    waveData = km2level(seq[i*k:i*k + k])
    out.writeframes(waveData)
out.close()
