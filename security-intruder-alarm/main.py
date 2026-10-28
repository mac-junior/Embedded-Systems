from machine import Pin, PWM
import time

# Clean, safe Pin Assignments
PIR_SENSOR = Pin(13, Pin.IN)       # Input from Motion Sensor
ALERT_LED = Pin(15, Pin.OUT)       # Red Warning LED (Moved off crashing pin D12)

# Hardware PWM driver setup on Pin D4
buzzer_pwm = PWM(Pin(4))
buzzer_pwm.freq(440)               # Standard stable A4 audio frequency
buzzer_pwm.duty(0)                  # Start 100% silent

print("System Initializing... Calibrating PIR Sensor.")
time.sleep(2)  
print("System Armed. Monitoring perimeter...")

while True:
    motion_detected = PIR_SENSOR.value()
    
    if motion_detected == 1:
        print("🚨 ALERT! Intrusion Detected!")
        
        # Run a continuous flashing alert sequence
        for _ in range(5):
            ALERT_LED.on()
            buzzer_pwm.freq(550)    # Alter pitch to sound like a real siren
            buzzer_pwm.duty(512)    # 50% duty cycle turns sound ON
            time.sleep(0.3)
            
            ALERT_LED.off()
            buzzer_pwm.freq(440)    # Alter pitch down
            buzzer_pwm.duty(512)
            time.sleep(0.3)
            
        # Clear states when alarm cycle ends
        buzzer_pwm.duty(0)
        print("Alarm burst complete. Polling sensor...")
        time.sleep(1) 
            
    else:
        # Enforce secure state
        ALERT_LED.off()
        buzzer_pwm.duty(0)
        
    time.sleep(0.1)
