# Part of the Soundsentences program
# By Roelof Ruis <roelof.ruis@gmail.com>

# Going the full monty by defining all knowledge about scales and notes ourselves!

# Using a factory object makes sure that there will be no mistakes when creating
# scales we would like to use.
# If you want another scale, just add it to the factory.
class ScaleFactory():
    def majorScale(self, pitch='C', octave=3):
        pitchInstance  = Pitch(pitch)
        octaveInstance = Octave(octave)
        print pitchInstance
        print octaveInstance


# Represents a musical scale. Create one of these via the ScaleFactory
class Scale():
    def __init__(self, notes):
        self.notes = notes

# Representation of the different octaves.
class Octave():
    def __init__(self, octave):
        self.octave = octave
        
    def __str__(self):
        return 'octave ' + str(self.octave)

# Representation of the different pitches.
class Pitch():
    PITCH_DICT = {
        'C' : 0,
        'D' : 2,
        'E' : 4,
        'F' : 5,
        'G' : 7,
        'A' : 9,
        'B' : 11
    }
    
    def __init__(self, pitch):
        if pitch in self.PITCH_DICT:
            self.pitch = pitch
        else:
            raise AttributeError('Undefined pitch')
    
    def __str__(self):
        return 'pitch ' + self.pitch
        
    
    