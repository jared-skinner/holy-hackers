import RPi.GPIO as GPIO
import time

HOUR_PINS = [19, 13, 6, 5]
MINUTE_PINS =9 [22, 27, 17, 4, 21, 20]
SECOND_PINS = [16, 12, 25, 24, 23, 18]

def test() -> None:
    """
    verify that the breadboard is wired correctly
    """

    print("testing!")

    # zero everything out
    for pins in [HOUR_PINS, MINUTE_PINS, SECOND_PINS]:
        for pin in pins:
            GPIO.output(pin, GPIO.LOW)

    # test each pin individually
    for pins in [HOUR_PINS, MINUTE_PINS, SECOND_PINS]:
        for pin in pins:
            GIPO.output(pin, GPIO.HIGH)
            time.sleep(.3)
            GPIO.output(pin, GPIO.LOW)

def set_pins(type: str, binary_value: str) -> None:
    """
    set the pins for hours, minutes, or seconds
    this is a helper function for the clock method
    """
    if type == "hour":
        pins = HOUR_PINS
    elif type == "minute":
        pins = MINUTE_PINS
    elif type == "seconds":
        pins = SECOND_PINS

    for val, pin in zip(binary_value, pins):
        if val == "0":
            GPIO.output(pin, GPIO.LOW)
        else:
            GPIO.output(pin, GPIO.HIGH)

def dec_to_binary(value: int) -> int:
    """
    convert a decimal value to binary
    """
    if value == 0:
        return value

    binary_value = 0
    while value > 0:
        place = 0
        while 2 ** place <= value:
            place += 1

        place -= 1

        value = value - 2 ** place
        binary_value += 10 ** place

    return binary_value

def clock() -> None:
    """
    run the binary clock
    """

    print("starting clock!")
    print("")

    while True:
        # get the time 
        now = time.time()
        now = time.localtime(now)

        # convert the time to binary
        if now.tm_hour > 12:
            hour = now.tm_hour - 12
        else:
            hour = now.tm_hour

        binary_hour = str(dec_to_binary(hour))
        binary_min = str(dec_to_binary(now.tm_min))
        binary_sec = str(dec_to_binary(now.tm_sec))

        while len(binary_hour) < 4:
            binary_hour = "0" + binary_hour

        while len(binary_min) < 6:
            binary_min = "0" + binary_min

        while len(binary_sec) < 6:
            binary_sec = "0" + binary_sec

        print(f"hour:   {binary_hour}")
        print(f"minute: {binary_min}")
        print(f"second: {binary_sec}")
        print("")

        # set the pins

        time.sleep(1)

def main():
    print("chose a mode:")
    print("1 - test")
    print("2 - clock")

    x = 0
    while x not in ("1", "2"):
        x = input(":")

    if x == "1":
        test()
    if x == "2":
        clock()


if __name__ == "__main__":
    main()
