# coding=utf-8
from mido import MidiFile
import sys


def mid2seq(note, velocity):
    convert = {'00': 'A', '01': 'C', '10': 'G', '11': 'T'}
    dna = ""
    bi = bin(note)[2:].zfill(7) + bin(velocity)[2:].zfill(7)
    for i in range(len(bi) // 2):
        dna += convert[bi[i * 2:i * 2 + 2]]
    return(dna)


out = open("outsequence.fasta", 'w')

for msg in MidiFile(sys.argv[1]):
    if not msg.is_meta:
        m = msg.bytes()[0]
        # If not off or note on
        if(m == 128 or m == 144):
            m, nt, vl = msg.bytes()
            out.write(mid2seq(nt, vl))
out.close()
