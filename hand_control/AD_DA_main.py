#!/usr/bin/python
# -*- coding:utf-8 -*-

import time
import ADS1256
import DAC8532
import RPi.GPIO as GPIO

"""
try:
    ADC = ADS1256.ADS1256()
    DAC = DAC8532.DAC8532()
    ADC.ADS1256_init()

    DAC.DAC8532_Out_Voltage(0x30, 3)
    DAC.DAC8532_Out_Voltage(0x34, 3)
    while True:
        ADC_Value = ADC.ADS1256_GetAll()
        print ("0 ADC = %lf"%(ADC_Value[0]*5.0/0x7fffff))
        print ("1 ADC = %lf"%(ADC_Value[1]*5.0/0x7fffff))
        print ("2 ADC = %lf"%(ADC_Value[2]*5.0/0x7fffff))
        print ("3 ADC = %lf"%(ADC_Value[3]*5.0/0x7fffff))
        print ("4 ADC = %lf"%(ADC_Value[4]*5.0/0x7fffff))
        print ("5 ADC = %lf"%(ADC_Value[5]*5.0/0x7fffff))
        print ("6 ADC = %lf"%(ADC_Value[6]*5.0/0x7fffff))
        print ("7 ADC = %lf"%(ADC_Value[7]*5.0/0x7fffff))

        temp = (ADC_Value[0]>>7)*5.0/0xffff
        print ("DAC :", temp)
        print ("\33[10A")
        DAC.DAC8532_Out_Voltage(DAC8532.channel_A, temp)
        DAC.DAC8532_Out_Voltage(DAC8532.channel_B, 3.3 - temp)

except :
    GPIO.cleanup()
    print ("\r\nProgram end     ")
    exit()
"""

class AD_DA_Transfer:
    def __init__(self):
        self.ADC = ADS1256.ADS1256()
        self.DAC = DAC8532.DAC8532()
        self.ADC.ADS1256_init()
        self.DAC.DAC8532_Out_Voltage(0x30, 0.04)
        self.DAC.DAC8532_Out_Voltage(0x34, 0.04)

    def get_value(self):
        ADC_Value = self.ADC.ADS1256_GetAll()
        AD0 = ADC_Value[0] * 5.0 / 0x7fffff
        AD1 = ADC_Value[1] * 5.0 / 0x7fffff
        AD2 = ADC_Value[2] * 5.0 / 0x7fffff
        AD3 = ADC_Value[3] * 5.0 / 0x7fffff
        AD4 = ADC_Value[4] * 5.0 / 0x7fffff
        AD5 = ADC_Value[5] * 5.0 / 0x7fffff
        AD6 = ADC_Value[6] * 5.0 / 0x7fffff
        AD7 = ADC_Value[7] * 5.0 / 0x7fffff
        AD_dict = {
            'AD0': AD0, 'AD1': AD1, 'AD2': AD2, 'AD3': AD3, 'AD4': AD4, 'AD5': AD5, 'AD6': AD6, 'AD7': AD7,
        }
        return AD_dict

    def da_value(self, da0=0.1, da1=0.1):
        self.DAC.DAC8532_Out_Voltage(DAC8532.channel_A, da0)
        self.DAC.DAC8532_Out_Voltage(DAC8532.channel_B, da1)

    def clearned(self):
        GPIO.cleanup()
