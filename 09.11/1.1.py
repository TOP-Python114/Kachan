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
                 # ИСПРАВИТЬ: мне представляется сомнительной возможность существования экземпляра ноты со всеми атрибутами равными None — зачем добавили значения по умолчанию для pitch и octave?
                 #не разбираюсь в нотах, учту на будущее - тщательнее изучать объекты:)
                 pitch: Pitch,
                 octave: Octave,
                 accidental: Accidental = None,
                 duration: Duration = Duration.QUARTER):
        self.pitch = pitch
        self.octave = octave
        self.accidental = accidental
        self.duration = duration

    def clone(self, **kwargs):
        """Клонирует и обновляет атрибуты словаря"""
        clone_obj = deepcopy(self)
        # КОММЕНТАРИЙ: очень хорошо
        clone_obj.__dict__.update(**kwargs)
        return clone_obj

    def __str__(self):
        return (f'Высота: {self.pitch}\nОктава: {self.octave}'
                f'\nAccidental: {self.accidental}'
                f'\nПродолжительность: {self.duration}')


class ScoreNote(Note):
    """Отображает музыкальную ноту в партитуре."""

    def __init__(self,
                 *,
                 stem_up: bool,
                 beam: bool = False,
                 # ИСПРАВИТЬ: аналогично для pitch и octave — и не забудьте о порядке задания параметров, обладающих и не обладающих значениями по умолчанию
                 pitch: Pitch,
                 octave: Octave,
                 accidental: Accidental = None,
                 duration: Duration = Duration.QUARTER):
        super().__init__(pitch=pitch, octave=octave, accidental=accidental, duration=duration)
        self.stem_up = stem_up
        self.beam = beam

    def __str__(self):
        return super().__str__()


class MIDINote(Note):
    """Кодирует музыкальную ноту в MIDI протоколе."""

    def __init__(self,
                 *,
                 velocity: int,
                 # ИСПРАВИТЬ: аналогично для pitch и octave
                 pitch: Pitch,
                 octave: Octave,
                 accidental: Accidental = None,
                 duration: Duration = Duration.QUARTER):
        super().__init__(pitch=pitch, octave=octave, accidental=accidental, duration=duration)
        self.velocity = velocity

    def __str__(self):
        return super().__str__()+ f'\nVelocity: {self.velocity}'

note = Note(pitch=Pitch.C, octave=Octave.S_CONTRA, accidental=Accidental.NATURAL)

midi_c3 = MIDINote(pitch=Pitch.C, octave=Octave.LINE_1, velocity=80)
midi_d4 = midi_c3.clone(pitch=Pitch.D, octave=Octave.S_CONTRA)


print(f'Нота 1:')
print(note, '\n')

print(f'Нота 2:')
print(midi_c3, '\n')

print(f'Нота с измененными аттрибутами:')
print(midi_d4, '\n')

# ДОБАВИТЬ: под меткой tests закомментированные результаты выполнения скрипта с различными входными данными
# tests:
# Нота 1:
# Высота: 1
# Октава: -1
# Accidental: natural
# Продолжительность: Duration.QUARTER
#
# Нота 2:
# Высота: 1
# Октава: 3
# Accidental: None
# Продолжительность: Duration.QUARTER
# Velocity: 80
#
# Нота с измененными аттрибутами:
# Высота: 2
# Октава: -1
# Accidental: None
# Продолжительность: Duration.QUARTER
# Velocity: 80


# ИТОГ: очень хорошо — 5/6
