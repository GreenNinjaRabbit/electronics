from gpiozero import Device

class Keypad(Device):
    KEYS = [
        ["1","2","3","A"],
        ["4","5","6","B"],
        ["7","8","9","C"],
        ["*","0","#","D"]
    ]
    def __init__(self, inputpins, outputpins, keys=KEYS, **kwargs) -> None:
        self.inputpinnumbers = inputpins
        self.outputpinnumbers = outputpins
        self.keys = keys
        super().__init__(**kwargs)
        self.inputpins = [Device.pin_factory.pin(pinnumber) for pinnumber in inputpins]
        self.outputpins = [Device.pin_factory.pin(pinnumber) for pinnumber in outputpins]
        
    @property
    def value(self):
        for row, inputpin in enumerate(self.inputpins):
            if inputpin.state:
                for col, outputpin in enumerate(self.outputpins):
                    if outputpin.state:
                        return self.keys[row][col]