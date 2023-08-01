# Pre-processing Raga music - Process Midi codes after Audio to Midi Conversion 
import os
from music21 import converter, pitch, scale, interval, meter

# Define the scale
scale_pitches = ['C', 'D-', 'E', 'F', 'G', 'A-', 'B-', 'C']
custom_scale = scale.ConcreteScale(pitches=[pitch.Pitch(p) for p in scale_pitches])

def correct_notes(midi_file):
    for note in midi_file.recurse().notes:
        if note.pitch.name not in scale_pitches:
            note.pitch = custom_scale.next(note.pitch)
    return midi_file

def transpose_to_c(midi_file):
    key = midi_file.analyze('key')
    i = interval.Interval(key.tonic, pitch.Pitch('C'))
    return midi_file.transpose(i)

def reduce_density(midi_file, reduction_factor=0.5):
    notes = midi_file.recurse().notes
    for i, note in enumerate(notes):
        if i % int(1/reduction_factor) == 0:
            midi_file.remove(note)
    return midi_file

def remove_silences(midi_file):
    for rest in midi_file.recurse().getElementsByClass('Rest'):
        midi_file.remove(rest)
    return midi_file

def regularize_tempo(midi_file):
    midi_file.insert(0, meter.TimeSignature('4/4'))
    return midi_file

def process_midi_file(file_path):
    midi_file = converter.parse(file_path)
    midi_file = correct_notes(midi_file)
    midi_file = transpose_to_c(midi_file)
    midi_file = reduce_density(midi_file)
    midi_file = remove_silences(midi_file)
    midi_file = regularize_tempo(midi_file)
    new_file_path = file_path.replace('.mid', '_processed.mid')
    midi_file.write('midi', fp=new_file_path)

def process_all_midi_files(directory_path):
    midi_files = [f for f in os.listdir(directory_path) if f.endswith('.mid')]
    for midi_file in midi_files:
        file_path = os.path.join(directory_path, midi_file)
        process_midi_file(file_path)
