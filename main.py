def on_forever():
    basic.pause(500)
    music.play(music.tone_playable(392, music.beat(BeatFraction.WHOLE)),
        music.PlaybackMode.UNTIL_DONE)
    music.play(music.tone_playable(440, music.beat(BeatFraction.WHOLE)),
        music.PlaybackMode.UNTIL_DONE)
    music.play(music.tone_playable(294, music.beat(BeatFraction.HALF)),
        music.PlaybackMode.UNTIL_DONE)
    music.play(music.tone_playable(440, music.beat(BeatFraction.WHOLE)),
        music.PlaybackMode.UNTIL_DONE)
    music.play(music.tone_playable(494, music.beat(BeatFraction.WHOLE)),
        music.PlaybackMode.UNTIL_DONE)
    music.play(music.tone_playable(587, music.beat(BeatFraction.QUARTER)),
        music.PlaybackMode.UNTIL_DONE)
    music.play(music.tone_playable(523, music.beat(BeatFraction.QUARTER)),
        music.PlaybackMode.UNTIL_DONE)
    music.play(music.tone_playable(494, music.beat(BeatFraction.QUARTER)),
        music.PlaybackMode.UNTIL_DONE)
    music.play(music.tone_playable(440, music.beat(BeatFraction.QUARTER)),
        music.PlaybackMode.UNTIL_DONE)
    music.play(music.tone_playable(392, music.beat(BeatFraction.WHOLE)),
        music.PlaybackMode.UNTIL_DONE)
    music.play(music.tone_playable(440, music.beat(BeatFraction.WHOLE)),
        music.PlaybackMode.UNTIL_DONE)
    basic.pause(500)
basic.forever(on_forever)

def on_forever2():
    basic.show_string("Never Gonna Give You Up")
basic.forever(on_forever2)
