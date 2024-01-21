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
        self.lastpressed = None
        super().__init__(**kwargs)
        self.inputpins = [Device.pin_factory.pin(pinnumber) for pinnumber in inputpins]
        self.outputpins = [Device.pin_factory.pin(pinnumber) for pinnumber in outputpins]
        for pin in self.inputpins+self.outputpins:
            pin.function = "input"
        self.setpinstate("up")
        for outputpin in self.outputpins:
            outputpin.edges = "rising"
            outputpin.when_changed = self.setlastpressed

    def setpinstate(self, state):
        for inputpin in self.inputpins:
            inputpin.pull=state
    
    def setlastpressed(self, *_):
        self.lastpressed = self.value

    @property
    def value(self):
        for outputpin in self.outputpins:
            outputpin.edges = "none"
        self.setpinstate("down")
        for row, inputpin in enumerate(self.inputpins):
            inputpin.pull = "up"
            for col, outputpin in enumerate(self.outputpins):
                if outputpin.state:
                    self.setpinstate("up")
                    for outputpin in self.outputpins:
                        outputpin.edges = "rising"
                    return self.keys[row][col]
                
    @property
    def is_active(self):
        return any(outputpin.state for outputpin in self.outputpins)