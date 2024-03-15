from time import sleep
from keypad import Keypad
from gpiozero.pins.mock import MockConnectedPin, MockPin

inputpins = [12,16,18,22]
outputpins = [11,13,15,19]

class MockPressedButton(MockPin):
    """
    This derivative of :class:`MockPin` emulates a pin connected to another
    mock pin e.g. by pressing a button.
    """
    def __init__(self, factory, info, connected_pin):
        super().__init__(factory, info)
        self.connected_pin = connected_pin
    
    def _change_state(self, value):
        self.connected_pin.state = value
        return super()._change_state(value)

def test_Keypad(mock_factory):
    keys = [
        ["1","2","3","A"],
        ["4","5","6","B"],
        ["7","8","9","C"],
        ["*","0","#","D"]
    ]
    pad = Keypad(inputpins=inputpins, outputpins=outputpins)
    assert pad.inputpinnumbers == inputpins
    assert pad.outputpinnumbers == outputpins
    assert pad.keys == keys

def test_otherkeys(mock_factory):
    keys = [
        ["1","2","3"],
        ["4","5","6"],
        ["7","8","9"],
        ["*","0","#"]
    ]
    pad = Keypad(inputpins=inputpins, outputpins=outputpins, keys = keys)
    assert pad.inputpinnumbers == inputpins
    assert pad.outputpinnumbers == outputpins
    assert pad.keys == keys

def test_5pressed(mock_factory):
    pin13 = mock_factory.pin(13)
    pin16 = mock_factory.pin(16, pin_class=MockPressedButton, connected_pin=pin13)
    pin13.function = "output"
    pin16.function = "input"
    assert pin16.state is False
    assert pin13.state is False
    pin16.drive_high()
    sleep(1)
    assert pin16.state is True
    assert pin13.state is True
    pad = Keypad(inputpins=inputpins, outputpins=outputpins)
    assert pad.value == "5"

def test_9pressed(mock_factory):
    pin18 = mock_factory.pin(18)
    pin15 = mock_factory.pin(15, pin_class=MockPressedButton, connected_pin=pin18)
    pin18.function = "output"
    pin15.function = "input"
    assert pin15.state is False
    assert pin18.state is False
    pin15.drive_high()
    sleep(1)
    assert pin15.state is True
    assert pin18.state is True
    pad = Keypad(inputpins=inputpins, outputpins=outputpins)
    assert pad.value == "9"