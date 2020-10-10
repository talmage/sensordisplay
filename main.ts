//  Return the string representation of a number padded on the left with zeroes.
function rightJustifyNumber(num: number, length: number): string {
    
    answer = convertToText(num)
    while (answer.length < length) {
        answer = "0" + answer
    }
    return answer
}

//  Update the display whenever the accelerometer reports an update
control.onEvent(EventBusSource.MICROBIT_ID_ACCELEROMETER, EventBusValue.MICROBIT_ACCELEROMETER_EVT_DATA_UPDATE, function on_microbit_id_accelerometer_evt_data_update() {
    
    LCD1IN8.DisString(50, 20, accel, LCD1IN8.Get_Color(LCD_COLOR.WHITE))
    accel = rightJustifyNumber(input.acceleration(Dimension.Strength), 4)
    LCD1IN8.DisString(50, 20, accel, LCD1IN8.Get_Color(LCD_COLOR.RED))
    LCD1IN8.LCD_DisplayWindows(50, 20, 90, 30)
})
let answer = ""
let accel = ""
input.calibrateCompass()
LCD1IN8.LCD_Init()
LCD1IN8.LCD_Clear()
LCD1IN8.LCD_SetBL(123)
accel = rightJustifyNumber(input.acceleration(Dimension.Strength), 4)
let heading = rightJustifyNumber(input.compassHeading(), 3)
let lumens = rightJustifyNumber(input.lightLevel(), 3)
let magneticForce = rightJustifyNumber(input.magneticForce(Dimension.Strength), 8)
magneticForce = rightJustifyNumber(input.magneticForce(Dimension.Strength), 3)
let pitch = rightJustifyNumber(input.rotation(Rotation.Pitch), 4)
let roll = rightJustifyNumber(input.rotation(Rotation.Roll), 4)
let temp = rightJustifyNumber(input.temperature(), 3)
LCD1IN8.DisString(0, 0, "light: ", LCD1IN8.Get_Color(LCD_COLOR.BLACK))
LCD1IN8.DisString(50, 0, lumens, LCD1IN8.Get_Color(LCD_COLOR.RED))
LCD1IN8.DisString(0, 10, "temp: ", LCD1IN8.Get_Color(LCD_COLOR.BLACK))
LCD1IN8.DisString(50, 10, temp, LCD1IN8.Get_Color(LCD_COLOR.RED))
LCD1IN8.DisString(0, 20, "accel:", LCD1IN8.Get_Color(LCD_COLOR.BLACK))
LCD1IN8.DisString(50, 20, accel, LCD1IN8.Get_Color(LCD_COLOR.RED))
LCD1IN8.DisString(0, 30, "head: ", LCD1IN8.Get_Color(LCD_COLOR.BLACK))
LCD1IN8.DisString(50, 30, heading, LCD1IN8.Get_Color(LCD_COLOR.RED))
LCD1IN8.DisString(0, 40, "magnet:", LCD1IN8.Get_Color(LCD_COLOR.BLACK))
LCD1IN8.DisString(50, 40, magneticForce, LCD1IN8.Get_Color(LCD_COLOR.RED))
LCD1IN8.DisString(0, 50, "pitch:", LCD1IN8.Get_Color(LCD_COLOR.BLACK))
LCD1IN8.DisString(50, 50, pitch, LCD1IN8.Get_Color(LCD_COLOR.RED))
LCD1IN8.DisString(0, 60, "roll: ", LCD1IN8.Get_Color(LCD_COLOR.BLACK))
LCD1IN8.DisString(50, 60, roll, LCD1IN8.Get_Color(LCD_COLOR.RED))
LCD1IN8.LCD_Display()
//  Poll the light sensor every 100ms and update the display.
control.inBackground(function on_in_background() {
    
    while (true) {
        LCD1IN8.DisString(50, 0, lumens, LCD1IN8.Get_Color(LCD_COLOR.WHITE))
        lumens = rightJustifyNumber(input.lightLevel(), 3)
        LCD1IN8.DisString(50, 0, lumens, LCD1IN8.Get_Color(LCD_COLOR.RED))
        LCD1IN8.LCD_DisplayWindows(50, 0, 90, 10)
        basic.pause(100)
    }
})
//  Poll the temperature sensor every 100ms and update the display
control.inBackground(function on_in_background2() {
    
    while (true) {
        LCD1IN8.DisString(50, 10, temp, LCD1IN8.Get_Color(LCD_COLOR.WHITE))
        temp = rightJustifyNumber(input.temperature(), 3)
        LCD1IN8.DisString(50, 10, temp, LCD1IN8.Get_Color(LCD_COLOR.RED))
        LCD1IN8.LCD_DisplayWindows(50, 10, 90, 20)
        basic.pause(100)
    }
})
//  Poll the magnetometer every 100ms and update the display.
control.inBackground(function on_in_background3() {
    
    while (true) {
        LCD1IN8.DisString(50, 40, magneticForce, LCD1IN8.Get_Color(LCD_COLOR.WHITE))
        magneticForce = rightJustifyNumber(input.magneticForce(Dimension.Strength), 8)
        LCD1IN8.DisString(50, 40, magneticForce, LCD1IN8.Get_Color(LCD_COLOR.RED))
        LCD1IN8.LCD_DisplayWindows(50, 40, 160, 50)
        basic.pause(100)
    }
})
//  Poll the pitch sensor
//  every 100ms and update the display.
control.inBackground(function on_in_background4() {
    
    while (true) {
        LCD1IN8.DisString(50, 50, pitch, LCD1IN8.Get_Color(LCD_COLOR.WHITE))
        pitch = rightJustifyNumber(input.rotation(Rotation.Pitch), 4)
        LCD1IN8.DisString(50, 50, pitch, LCD1IN8.Get_Color(LCD_COLOR.RED))
        LCD1IN8.LCD_DisplayWindows(50, 50, 90, 50)
        basic.pause(100)
    }
})
//  Poll the roll sensor every 100ms and update the display.
control.inBackground(function on_in_background5() {
    
    while (true) {
        LCD1IN8.DisString(50, 60, roll, LCD1IN8.Get_Color(LCD_COLOR.WHITE))
        roll = rightJustifyNumber(input.rotation(Rotation.Roll), 4)
        LCD1IN8.DisString(50, 60, roll, LCD1IN8.Get_Color(LCD_COLOR.RED))
        LCD1IN8.LCD_DisplayWindows(50, 60, 90, 60)
        basic.pause(100)
    }
})
//  Poll the compass every 100ms and update the display.
control.inBackground(function on_in_background6() {
    
    while (true) {
        LCD1IN8.DisString(50, 30, heading, LCD1IN8.Get_Color(LCD_COLOR.WHITE))
        heading = rightJustifyNumber(input.compassHeading(), 3)
        LCD1IN8.DisString(50, 30, heading, LCD1IN8.Get_Color(LCD_COLOR.RED))
        LCD1IN8.LCD_DisplayWindows(50, 30, 90, 40)
        basic.pause(100)
    }
})
