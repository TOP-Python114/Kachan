# Вам даны классы Note, ScoreNote и MIDINote. В файле constants.py прописаны используемые в перечислителях константы.
# Допишите конструкторы классов ScoreNote и MIDINote исходя из требований о наличии дополнительных атрибутов у соответствующих классов. Требования подписаны в виде комментариев под сигнатурами классов.
# Допишите метод clone() в родительском классе. В методе необходимо учесть наследование. То есть, метод должен клонировать не только экземпляр класса Note, но и экземпляры дочерних классов, создавая новые экземпляры тех же классов.
# Также, необходимо добавить возможность переопределять значения некоторых атрибутов при клонировании.

from copy import deepcopy
from constants import *


class Note:
    """Музыкальная нота с возможностью копирования."""

    def __init__(self,
                 *,
                 pitch: Pitch = None,
                 octave: Octave = None,
                 accidental: Accidental = None,
                 duration: Duration = Duration.QUARTER):
        self.pitch = pitch
        self.octave = octave
        self.accidental = accidental
        self.duration = duration

    def clone(self, **kwargs):
        """Клонирование и обновление словаря атрибутов."""
        clone_obj = deepcopy(self)
        clone_obj.__dict__.update(**kwargs)
        return clone_obj


class ScoreNote(Note):
    """Изображение музыкальной ноты в партитуре."""

    def __init__(self,
                 *,
                 stem_up: bool,
                 beam: bool = False,
                 pitch: Pitch = None,
                 octave: Octave = None,
                 accidental: Accidental = None,
                 duration: Duration = Duration.QUARTER):
        super().__init__(pitch=pitch, octave=octave, accidental=accidental, duration=duration)
        self.stem_up = stem_up
        self.beam = beam


class MIDINote(Note):
    """Кодирование музыкальной ноты в MIDI протоколе."""

    def __init__(self,
                 *,
                 velocity: int,
                 pitch: Pitch = None,
                 octave: Octave = None,
                 accidental: Accidental = None,
                 duration: Duration = Duration.QUARTER):
        super().__init__(pitch=pitch, octave=octave, accidental=accidental, duration=duration)
        self.velocity = velocity


pot = Note(pitch=Pitch.C, octave=Octave.S_CONTRA, accidental=Accidental.NATURAL)

midi_c3 = MIDINote(pitch=Pitch.C, octave=Octave.LINE_1, velocity=80)
midi_d3 = midi_c3.clone(pitch=Pitch.D, octave=Octave.S_CONTRA)

print(midi_d3.clone().octave)


# ДОБАВИТЬ: под меткой tests закомментированные результаты выполнения скрипта с различными входными данными
# tests:
