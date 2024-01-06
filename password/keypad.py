class Keypad:
    KEYS = [
        ["1","2","3","A"],
        ["4","5","6","B"],
        ["7","8","9","C"],
        ["*","0","#","D"]
    ]
    def __init__(self, inputpins, outputpins, keys=KEYS) -> None:
        self.inputpins = inputpins
        self.outputpins = outputpins
        self.keys = keys
        self.value = "5"