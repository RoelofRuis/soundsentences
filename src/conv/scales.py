# Part of the Soundsentences program
# By Roelof Ruis <roelof.ruis@gmail.com>

# Going the full monty by defining all knowledge about scales and notes ourselves!

# Using a factory object makes sure that there will be no mistakes when creating
# scales we would like to use.
# If you want another scale, just add it to the factory.
class ScaleFactory():
    def majorScale(self):
        pass

# Represents a musical scale. Create one of these via the ScaleFactory
class Scale():
    def __init__(self, notes):
        self.notes = notes

# Representation of the different octaves.
class Octave():
    def __init__(self, octave):
        if isinstance(octave, int) and octave in range(-2, 9):
            self.octave = octave
        else:
            raise AttributeError('An octave should be instantiated with an integer between -2 and 8')

    def __str__(self):
        return 'octave ' + str(self.octave)

# Let the note factory build the notes.
class NoteFactory():
    C_FLAT  = Note('Cb', 11)
    C       = Note('C',  0)
    C_SHARP = Note('C#', 1)
    D_FLAT  = Note('Db', 1)
    D       = Note('D',  2)
    D_SHARP = Note('D#', 3)
    E_FLAT  = Note('Eb', 3)
    E       = Note('E',  4)
    E_SHARP = Note('E#', 5)
    F_FLAT  = Note('Fb', 4)
    F       = Note('F',  5)
    F_SHARP = Note('F#', 6)
    G_FLAT  = Note('Gb', 6)
    G       = Note('G',  7)
    G_SHARP = Note('G#', 8)
    A_FLAT  = Note('Ab', 8)
    A       = Note('A',  9)
    A_SHARP = Note('A#', 10)
    B_FLAT  = Note('Bb', 10)
    B       = Note('B',  11)
    B_SHARP = Note('B#', 0)

# Defining the note object.
class Note():
    def __init__(self, name, interval):
        if isinstance(name, basestring):
            self.name = name
        else:
            raise AttributeError('The note name should be a string.')

        if isinstance(interval, int) and interval in range(0, 12):
            self.interval = interval
        else:
            raise AttributeError('The note interval should be an integer between 0 and 11')

    def __str__(self):
        return 'note ' + str(self.name)

# Representation of the different pitches.
class Pitch():
    def __init__(self, note, octave):
        self.note   = note
        self.octave = octave

    def __str__(self):
        return 'pitch ' + self.pitch
