from keypad import Keypad

inputpins = [12,16,18,22]
outputpins = [11,13,15,19]

def test_Keypad():
    keys = [
        ["1","2","3","A"],
        ["4","5","6","B"],
        ["7","8","9","C"],
        ["*","0","#","D"]
    ]
    pad = Keypad(inputpins=inputpins, outputpins=outputpins)
    assert pad.inputpins == inputpins
    assert pad.outputpins == outputpins
    assert pad.keys == keys

def test_otherkeys():
    keys = [
        ["1","2","3"],
        ["4","5","6"],
        ["7","8","9"],
        ["*","0","#"]
    ]
    pad = Keypad(inputpins=inputpins, outputpins=outputpins, keys = keys)
    assert pad.inputpins == inputpins
    assert pad.outputpins == outputpins
    assert pad.keys == keys