from keypad import Keypad

def test_Keypad():
    inputpins = [12,16,18,22]
    outputpins = [11,13,15,19]
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