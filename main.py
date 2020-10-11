# Return the string representation of a number padded on the left with zeroes.
def rightJustifyNumber(num: number, length: number):
    global answer
    answer = convert_to_text(num)
    while len(answer) < length:
        answer = "0" + answer
    return answer
# Update the display whenever the accelerometer reports an update

def on_microbit_id_accelerometer_evt_data_update():
    global accel
    LCD1IN8.dis_string(50, 20, accel, LCD1IN8.Get_Color(LCD_COLOR.WHITE))
    accel = rightJustifyNumber(input.acceleration(Dimension.STRENGTH), 4)
    LCD1IN8.dis_string(50, 20, accel, LCD1IN8.Get_Color(LCD_COLOR.RED))
    LCD1IN8.LCD_DisplayWindows(50, 20, 90, 30)
control.on_event(EventBusSource.MICROBIT_ID_ACCELEROMETER,
    EventBusValue.MICROBIT_ACCELEROMETER_EVT_DATA_UPDATE,
    on_microbit_id_accelerometer_evt_data_update)

answer = ""
accel = ""
input.calibrate_compass()
LCD1IN8.LCD_Init()
LCD1IN8.LCD_Clear()
LCD1IN8.LCD_SetBL(123)
accel = rightJustifyNumber(input.acceleration(Dimension.STRENGTH), 4)
heading = rightJustifyNumber(input.compass_heading(), 3)
lumens = rightJustifyNumber(input.light_level(), 3)
magneticForce = rightJustifyNumber(input.magnetic_force(Dimension.STRENGTH), 8)
magneticForce = rightJustifyNumber(input.magnetic_force(Dimension.STRENGTH), 3)
pitch = rightJustifyNumber(input.rotation(Rotation.PITCH), 4)
roll = rightJustifyNumber(input.rotation(Rotation.ROLL), 4)
temp = rightJustifyNumber(input.temperature(), 3)
LCD1IN8.dis_string(0, 0, "light: ", LCD1IN8.Get_Color(LCD_COLOR.BLACK))
LCD1IN8.dis_string(50, 0, lumens, LCD1IN8.Get_Color(LCD_COLOR.RED))
LCD1IN8.dis_string(0, 10, "temp: ", LCD1IN8.Get_Color(LCD_COLOR.BLACK))
LCD1IN8.dis_string(50, 10, temp, LCD1IN8.Get_Color(LCD_COLOR.RED))
LCD1IN8.dis_string(0, 20, "accel:", LCD1IN8.Get_Color(LCD_COLOR.BLACK))
LCD1IN8.dis_string(50, 20, accel, LCD1IN8.Get_Color(LCD_COLOR.RED))
LCD1IN8.dis_string(0, 30, "head: ", LCD1IN8.Get_Color(LCD_COLOR.BLACK))
LCD1IN8.dis_string(50, 30, heading, LCD1IN8.Get_Color(LCD_COLOR.RED))
LCD1IN8.dis_string(0, 40, "magnet:", LCD1IN8.Get_Color(LCD_COLOR.BLACK))
LCD1IN8.dis_string(50, 40, magneticForce, LCD1IN8.Get_Color(LCD_COLOR.RED))
LCD1IN8.dis_string(0, 50, "pitch:", LCD1IN8.Get_Color(LCD_COLOR.BLACK))
LCD1IN8.dis_string(50, 50, pitch, LCD1IN8.Get_Color(LCD_COLOR.RED))
LCD1IN8.dis_string(0, 60, "roll: ", LCD1IN8.Get_Color(LCD_COLOR.BLACK))
LCD1IN8.dis_string(50, 60, roll, LCD1IN8.Get_Color(LCD_COLOR.RED))
LCD1IN8.LCD_Display()
# Poll the temperature sensor every 100ms and update the display

def on_in_background():
    global temp
    while True:
        LCD1IN8.dis_string(50, 10, temp, LCD1IN8.Get_Color(LCD_COLOR.WHITE))
        temp = rightJustifyNumber(input.temperature(), 3)
        LCD1IN8.dis_string(50, 10, temp, LCD1IN8.Get_Color(LCD_COLOR.RED))
        LCD1IN8.LCD_DisplayWindows(50, 10, 90, 20)
        basic.pause(100)
control.in_background(on_in_background)

# Poll the magnetometer every 100ms and update the display.

def on_in_background2():
    global magneticForce
    while True:
        LCD1IN8.dis_string(50, 40, magneticForce, LCD1IN8.Get_Color(LCD_COLOR.WHITE))
        magneticForce = rightJustifyNumber(input.magnetic_force(Dimension.STRENGTH), 8)
        LCD1IN8.dis_string(50, 40, magneticForce, LCD1IN8.Get_Color(LCD_COLOR.RED))
        LCD1IN8.LCD_DisplayWindows(50, 40, 160, 50)
        basic.pause(100)
control.in_background(on_in_background2)

# Poll the pitch sensor
# every 100ms and update the display.

def on_in_background3():
    global pitch
    while True:
        LCD1IN8.dis_string(50, 50, pitch, LCD1IN8.Get_Color(LCD_COLOR.WHITE))
        pitch = rightJustifyNumber(input.rotation(Rotation.PITCH), 4)
        LCD1IN8.dis_string(50, 50, pitch, LCD1IN8.Get_Color(LCD_COLOR.RED))
        LCD1IN8.LCD_DisplayWindows(50, 50, 90, 50)
        basic.pause(100)
control.in_background(on_in_background3)

# Poll the roll sensor every 100ms and update the display.

def on_in_background4():
    global roll
    while True:
        LCD1IN8.dis_string(50, 60, roll, LCD1IN8.Get_Color(LCD_COLOR.WHITE))
        roll = rightJustifyNumber(input.rotation(Rotation.ROLL), 4)
        LCD1IN8.dis_string(50, 60, roll, LCD1IN8.Get_Color(LCD_COLOR.RED))
        LCD1IN8.LCD_DisplayWindows(50, 60, 90, 60)
        basic.pause(100)
control.in_background(on_in_background4)

# Poll the compass every 100ms and update the display.

def on_in_background5():
    global heading
    while True:
        LCD1IN8.dis_string(50, 30, heading, LCD1IN8.Get_Color(LCD_COLOR.WHITE))
        heading = rightJustifyNumber(input.compass_heading(), 3)
        LCD1IN8.dis_string(50, 30, heading, LCD1IN8.Get_Color(LCD_COLOR.RED))
        LCD1IN8.LCD_DisplayWindows(50, 30, 90, 40)
        basic.pause(100)
control.in_background(on_in_background5)

# Poll the light sensor every 100ms and update the display.

def on_in_background6():
    global lumens
    while True:
        LCD1IN8.dis_string(50, 0, lumens, LCD1IN8.Get_Color(LCD_COLOR.WHITE))
        lumens = rightJustifyNumber(input.light_level(), 3)
        LCD1IN8.dis_string(50, 0, lumens, LCD1IN8.Get_Color(LCD_COLOR.RED))
        LCD1IN8.LCD_DisplayWindows(50, 0, 90, 10)
        basic.pause(100)
control.in_background(on_in_background6)
