from gpiozero import Device

class Keypad:
    KEYS = [
        ["1","2","3","A"],
        ["4","5","6","B"],
        ["7","8","9","C"],
        ["*","0","#","D"]
    ]
    def __init__(self, inputpins, outputpins, keys=KEYS) -> None:
        self.inputpinnumbers = inputpins
        self.inputpins = [Device.pin_factory.pin(pinnumber) for pinnumber in inputpins]
        self.outputpinnumbers = outputpins
        self.outputpins = [Device.pin_factory.pin(pinnumber) for pinnumber in outputpins]
        self.keys = keys
        
    @property
    def value(self):
        for row, inputpin in enumerate(self.inputpins):
            if inputpin.state:
                for col, outputpin in enumerate(self.outputpins):
                    if outputpin.state:
                        return self.keys[row][col]