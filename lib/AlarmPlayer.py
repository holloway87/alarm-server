from simpleaudio import PlayObject, WaveObject
from typing import TypeVar

PlayObjectNone = TypeVar('PlayObjectNone', PlayObject, type(None))


class AlarmPlayer:
    """
    Logic to play the alarm sound.
    """
    alarm_sound: WaveObject
    alarm_playing: PlayObjectNone

    def __init__(self, sound_file: str):
        """
        Creates all needed instances.

        :param sound_file: absolute path for the alarm sound file
        """
        self.alarm_sound = WaveObject.from_wave_file(sound_file)
        self.alarm_playing = None

    def play(self) -> None:
        """
        Plays the alarm sound, if not already playing.

        :return:
        """
        if self.alarm_playing and not self.alarm_playing.is_playing():
            self.alarm_playing = None

        if not self.alarm_playing:
            self.alarm_playing = self.alarm_sound.play()

    def stop(self) -> None:
        """
        Stops the alarm sound, if playing.

        :return:
        """
        if self.alarm_playing:
            if self.alarm_playing.is_playing():
                self.alarm_playing.stop()
            self.alarm_playing = None
