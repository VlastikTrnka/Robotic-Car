uartdata = ""
connected = False
bluetooth.set_transmit_power(7)
bluetooth.start_uart_service()
pin_L = DigitalPin.P12
pin_R = DigitalPin.P15

def on_forever():
    pins.set_pull(DigitalPin.P12, PinPullMode.PULL_NONE)
    read_L = pins.digital_read_pin(DigitalPin.P12)
    print(read_L)
    if read_L == 0:
        PCAmotor.motor_run(PCAmotor.Motors.M2, 100)
        PCAmotor.motor_run(PCAmotor.Motors.M1, 100)  
        basic.show_icon(IconNames.HEART)
    basic.pause(20)
    if read_L == 1:
        PCAmotor.motor_run(PCAmotor.Motors.M2, 80)
        PCAmotor.motor_run(PCAmotor.Motors.M1, 50)
        PCAmotor.motor_stop_all()
        basic.show_icon(IconNames.SAD)
    basic.pause(20)
basic.forever(on_forever)

def manual():
    if uartdata == '0':
        PCAmotor.motor_stop_all()
    if uartdata == 'A':
        PCAmotor.motor_run(PCAmotor.Motors.M2, 255)
        PCAmotor.motor_run(PCAmotor.Motors.M1, 255)
    if uartdata == "B":
        PCAmotor.motor_run(PCAmotor.Motors.M2, -255)
        PCAmotor.motor_run(PCAmotor.Motors.M1, -255)
    if uartdata == "D":
        PCAmotor.motor_run(PCAmotor.Motors.M2, 255)
        PCAmotor.motor_run(PCAmotor.Motors.M1, 50)
    if uartdata == "C":
        PCAmotor.motor_run(PCAmotor.Motors.M2, 50)
        PCAmotor.motor_run(PCAmotor.Motors.M1, 255)

def on_bluetooth_connected():
    global connected, uartdata
    connected = True
    while connected:
        uartdata = bluetooth.uart_read_until(serial.delimiters(Delimiters.HASH))
        manual()
bluetooth.on_bluetooth_connected(on_bluetooth_connected)

def on_bluetooth_disconnected():
    global connected
    connected = False
bluetooth.on_bluetooth_disconnected(on_bluetooth_disconnected)

