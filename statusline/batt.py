#!/usr/bin/env python
###############################################################################
### Josh McGee <j dot s dot mcgee115 at gmail dot com>              ###########
### 2012-03-20                                                      ###########
###############################################################################
### "retrive battery charge for tmux statusline"


from decimal import *


def get_battery():
    """retrieve battery status and mutate it into human readable logic"""
    acpi_max = open("/sys/class/power_supply/BAT0/charge_full").read()
    if not int(acpi_max) > 0:
        print('error obtaining maximum capacity:\nkernel too old or battery missing?')
    else:
        acpi_current = open("/sys/class/power_supply/BAT0/charge_now").read()
        charge_dec = (Decimal(acpi_current) / Decimal(acpi_max)) * 100
        charge = charge_dec.quantize(Decimal('.01'), rounding=ROUND_DOWN)
        print(charge, end='%')


if __name__ == '__main__':
    get_battery()
