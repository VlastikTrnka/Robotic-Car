uartdata = ""
connected = 1
bluetooth.set_transmit_power(7)
bluetooth.start_uart_service()
pin_L = DigitalPin.P12
pin_R = DigitalPin.P15

rightmotor = PCAmotor.Motors.M1
leftmotor = PCAmotor.Motors.M2
pomalej=85
rychlej=pomalej+14
turn = 0

# def automat():
#     global rychlej, pomalej
#     pins.set_pull(pin_R, PinPullMode.PULL_NONE)
#     read_R = pins.digital_read_pin(pin_R)
#     pins.set_pull(pin_L, PinPullMode.PULL_NONE)
#     read_L = pins.digital_read_pin(pin_L)

#     if read_R==1 and read_L==1:
#         pins.set_pull(pin_R, PinPullMode.PULL_NONE)
#         read_R = pins.digital_read_pin(pin_R)
#         pins.set_pull(pin_L, PinPullMode.PULL_NONE)
#         read_L = pins.digital_read_pin(pin_L)
#         PCAmotor.motor_run(leftmotor, pomalej)
#         PCAmotor.motor_run(rightmotor, rychlej)
              
#     if read_L==1 and read_R==0: #doleva
#         pins.set_pull(pin_R, PinPullMode.PULL_NONE)
#         read_R = pins.digital_read_pin(pin_R)
#         pins.set_pull(pin_L, PinPullMode.PULL_NONE)
#         read_L = pins.digital_read_pin(pin_L)
#         PCAmotor.motor_run(leftmotor,10)
#         PCAmotor.motor_run(rightmotor,75)

#     if read_L==0 and read_R==1: #doprava
#         pins.set_pull(pin_R, PinPullMode.PULL_NONE)
#         read_R = pins.digital_read_pin(pin_R)
#         pins.set_pull(pin_L, PinPullMode.PULL_NONE)
#         read_L = pins.digital_read_pin(pin_L)
#         PCAmotor.motor_run(leftmotor,75)
#         PCAmotor.motor_run(rightmotor,12)
# basic.forever(automat)

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
    global connected, uartdata, turn
    connected = 1
    while connected and turn == 0:
        global rychlej, pomalej
        if input.button_is_pressed(Button.A):
            turn = 1
            basic.show_number(turn)
        while turn == 1:
            manual()
            if input.button_is_pressed(Button.A):
                turn = 0
            basic.show_number(turn)
        pins.set_pull(pin_R, PinPullMode.PULL_NONE)
        read_R = pins.digital_read_pin(pin_R)
        pins.set_pull(pin_L, PinPullMode.PULL_NONE)
        read_L = pins.digital_read_pin(pin_L)

        if read_R==1 and read_L==1:
            pins.set_pull(pin_R, PinPullMode.PULL_NONE)
            read_R = pins.digital_read_pin(pin_R)
            pins.set_pull(pin_L, PinPullMode.PULL_NONE)
            read_L = pins.digital_read_pin(pin_L)
            PCAmotor.motor_run(leftmotor, pomalej)
            PCAmotor.motor_run(rightmotor, rychlej)
            if input.button_is_pressed(Button.A):
                turn = 1
                basic.show_number(turn)
        if read_R==0 and read_L==0:
            pins.set_pull(pin_R, PinPullMode.PULL_NONE)
            read_R = pins.digital_read_pin(pin_R)
            pins.set_pull(pin_L, PinPullMode.PULL_NONE)
            read_L = pins.digital_read_pin(pin_L)
            PCAmotor.motor_run(leftmotor, pomalej)
            PCAmotor.motor_run(rightmotor, rychlej)       
        if read_L==1 and read_R==0: #doleva
            pins.set_pull(pin_R, PinPullMode.PULL_NONE)
            read_R = pins.digital_read_pin(pin_R)
            pins.set_pull(pin_L, PinPullMode.PULL_NONE)
            read_L = pins.digital_read_pin(pin_L)
            PCAmotor.motor_run(leftmotor,10)
            PCAmotor.motor_run(rightmotor,75)
        if read_L==0 and read_R==1: #doprava
            pins.set_pull(pin_R, PinPullMode.PULL_NONE)
            read_R = pins.digital_read_pin(pin_R)
            pins.set_pull(pin_L, PinPullMode.PULL_NONE)
            read_L = pins.digital_read_pin(pin_L)
            PCAmotor.motor_run(leftmotor,75)
            PCAmotor.motor_run(rightmotor,12)
        # if uartdata_2 == 'A':
        #     turn = 1
        #     basic.show_number(turn)
bluetooth.on_bluetooth_connected(on_bluetooth_connected)

def on_bluetooth_disconnected():
    global connected
    connected = 0
bluetooth.on_bluetooth_disconnected(on_bluetooth_disconnected)