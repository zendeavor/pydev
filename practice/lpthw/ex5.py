#!/usr/bin/env python
###############################################################################
### Josh McGee <j dot s dot mcgee115 at gmail dot com>              ###########
### 2012-05-28                                                      ###########
###############################################################################
### "lpthw exercise 5: more vars and printing"

me = "josh"
age = 24
height = 72
weight = 130
eyes = "blue"
teeth = "white"
hair = "brown"
conv_kg = 2.2
conv_km = 39.3700787
weight_kg = weight * conv_kg
height_km = height * conv_km

print("let's talk about {}.".format(me))
print("he's {} inches tall.".format(age))
print("he's {} lbs heavy.".format(weight))
print("actually that's not too heavy.")
print("he's got {} eyes and {} hair.".format(eyes, hair))

print("if i add {}, {:,.2f}, and {:.2f} i get {:,.2f}".format(age, height_km, 
    weight_kg, age + height_km + weight_kg))

