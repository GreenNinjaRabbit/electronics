from keypad import Keypad

def test_Keypad():
    inputpins = [12,16,18,22]
    outputpins = [11,13,15,19]
    pad = Keypad(inputpins=inputpins, outputpins=outputpins)
    assert pad.inputpins == inputpins
    assert pad.outputpins == outputpins