#!/usr/bin/env python
###############################################################################
### Josh McGee <j dot s dot mcgee115 at gmail dot com>              ###########
### 2012-03-20                                                      ###########
###############################################################################
### "retrieve stats for tmux statusline"


from time import strftime
import os


def get_battery():
    """retrieve battery status and mutate it into human readable logic"""
    acpi_max = int(open("/sys/class/power_supply/BAT0/charge_full").read())
    if not acpi_max > 0:
        print('error obtaining maximum capacity:\
                \nkernel too old or battery missing?')
    else:
        acpi_current = int(open("/sys/class/power_supply/BAT0/charge_now").read())
        charge = "{:.2%}".format(acpi_current / acpi_max)
        return charge


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
