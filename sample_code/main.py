from asterisk_doorphone.usb_keyboard import UsbKeyboard

import apartments
import config


def main():
    keyboard = UsbKeyboard(apartments, config)
    keyboard.start()


if __name__ == "__main__":
    import sys
    sys.exit(main())
