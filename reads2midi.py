# coding=utf-8
from mido import Message, MidiFile, MidiTrack
import sys

seq = ""
with open(sys.argv[1], 'r') as readFile:
    for line in readFile:
        if(not line[0] == '>'):
            seq += line.rstrip("\n")

length = len(seq)
k = 7

mid = MidiFile()
track = MidiTrack()
mid.tracks.append(track)


def km2level(kmer, notes):
    convert = {'A': '00', 'C': '01', 'G': '10', 'T': '11'}
    binVal = ''
    for n in kmer:
        binVal += convert[n]
    nt = int(binVal[0:7], 2)
    vl = int(binVal[7:], 2)
    op = ''
    if(notes[nt]):
        notes[nt] = 0
        op = 'note_off'
    else:
        notes[nt]= 1
        op = 'note_on'
    message = Message(op, note=nt, velocity=vl, time=16)
    return(message)


track.append(Message('program_change', program=0, time=0))

notes = [0] * 128
for i in range(length // k):
    msg = km2level(seq[i * k:i * k + k], notes)
    track.append(msg)

mid.save('reads.mid')
