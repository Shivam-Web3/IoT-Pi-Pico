from machine import Pin,ADC   # GPIO pins
import utime                  # time related functions

trigger = Pin(1, Pin.OUT)                    # send pulse
echo = Pin(0, Pin.IN)                        # recieve pulse
led_pin = machine.Pin(25, machine.Pin.OUT)   # led 

def ultra():
    
    led_pin.value(0)      # ensure led off
    utime.sleep(0.5)
    
    trigger.low()         # ensure sensor inactive
    utime.sleep_us(2)     
    
    trigger.high()        # short burst (10 microsecs)
    utime.sleep_us(10)    
    trigger.low()
    
    while echo.value() == 0:
        signaloff = utime.ticks_us()      # no signal timestamp >
    
    while echo.value() == 1:
        signalon = utime.ticks_us()       # signal timestamp <
    
    timepassed = signalon - signaloff     # total time <>
    
    sensor_temp = ADC(4)                  # getting temprature (dry air) 
    conversion_factor = 3.3/65535
    reading = sensor_temp.read_u16() * conversion_factor
    temp = 27 - (reading - 0.706)/0.001721 
    speed  = (331.4+(0.6*temp))/1e4       # cm/microseconds 
        
    distance = (timepassed * speed) / 2
    
    warning = ""                          # distance warnings
     
    if distance <= 4:             
        warning = "Too close"
        led_pin.value(1)
        utime.sleep(0.5)
        
    if distance >= 400:
        warning = "Too far"
        led_pin.value(1)
        utime.sleep(0.5)
    
    print("Distance:",distance,"cm","| Temprature:",temp, "degree Celcius | Speed of sound:", speed*1e4, "m/s |", warning)
                
while True:               # runs the loop each second
    ultra()
    utime.sleep(1)
    
    



    
        
        