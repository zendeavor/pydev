#!/usr/bin/env python
###############################################################################
### Josh McGee <j dot s dot mcgee115 at gmail dot com>              ###########
### 2012-03-20                                                      ###########
###############################################################################
### "retrieve stats for tmux statusline"


from time import strftime
import decimal as dec
import os


def get_battery():
    """retrieve battery status and mutate it into human readable logic"""
    acpi_max = open("/sys/class/power_supply/BAT0/charge_full").read()
    if not int(acpi_max) > 0:
        print('error obtaining maximum capacity:\nkernel too old or battery missing?')
    else:
        acpi_current = open("/sys/class/power_supply/BAT0/charge_now").read()
        acpi_current = dec.Decimal(acpi_current)
        acpi_max = dec.Decimal(acpi_max)
        charge_dec = (acpi_current / acpi_max) * 100
        dp = dec.Decimal('.01')
        charge = charge_dec.quantize(dp, dec.ROUND_05UP)
        charge = str(charge)
        return charge + '%'


def get_loadavg():
    """poll loadavg and output"""
    load = os.getloadavg()
    return load


def get_datetime():
    """grab date and time"""
    dtime = strftime("%Y-%m-%d %H:%M:%S")
    return dtime


def main():
    """run the script"""
    batt = get_battery()
    load = get_loadavg()
    dtime = get_datetime()
    print(batt, '|', load, '|', dtime)

if __name__ == '__main__':
    main()
