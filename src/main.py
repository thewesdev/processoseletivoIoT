from machine import Pin, SPI, I2C
from ili9341 import Display
from ft6206 import Touch
import colors
import math
import time

spi = SPI(
  2,
  baudrate=20_000_000,
  sck=Pin(18),
  mosi=Pin(23)
)

i2c = I2C(
    0,
    scl=Pin(22),
    sda=Pin(21),
    freq=400_000
)

display = Display(spi, Pin(4), Pin(2), Pin(16), rotation=180)
display.clear()

touch = Touch(i2c, display)

has_screen_drawned = False
has_timer_started = False
has_timer_paused = False

last_touch = False

WIDTH = display.width
HEIGHT = display.height
cx = WIDTH // 2
cy = HEIGHT // 2 - 40
r = 100
timer_total = 25 * 60
timer = timer_total
timer_text_x = int((WIDTH // 2) - 20)
timer_text_y = 260

print("Teste")

last_tick = time.ticks_ms()

while True:
    now = time.ticks_ms()

    if not has_screen_drawned:
        display.draw_circle(cx, cy, r, colors.WHITE)
        display.draw_text8x8(timer_text_x, timer_text_y, "25:00", colors.WHITE, colors.BLACK)
        has_screen_drawned = True
    
    if has_screen_drawned:
        points = touch.position
        is_touching = bool(points)

        x = None
        y = None
        if is_touching:
            x, y = points[0]

            if not last_touch:
                dx = x - cx
                dy = y - cy

                inside_circle = dx * dx + dy * dy <= r * r

                if inside_circle:
                    if not has_timer_started:
                        has_timer_started = True
                        last_tick = now
                    else:
                        has_timer_paused = not has_timer_paused

                        if not has_timer_paused:
                            last_tick = now
            
        last_touch = is_touching
    
    if has_timer_started and not has_timer_paused:
        while time.ticks_diff(time.ticks_ms(), last_tick) >= 1000:
            last_tick += 1000
            timer -= 1

            m = timer // 60
            s = timer % 60
            timer_text = f"{m:02}:{s:02}"

            step = 2 * math.pi / timer_total

            i = timer_total - timer

            t1 = i * step - math.pi / 2
            t2 = (i + 1) * step - math.pi / 2

            x1 = int(cx + r * math.cos(t1))
            y1 = int(cy + r * math.sin(t1))

            x2 = int(cx + r * math.cos(t2))
            y2 = int(cy + r * math.sin(t2))

            display.draw_line(x1, y1, x2, y2, colors.WHITE)
            display.fill_rectangle(timer_text_x - 30, timer_text_y - 10, 60, 20, colors.BLACK)
            display.draw_text8x8(timer_text_x, timer_text_y, timer_text, colors.WHITE, colors.BLACK)
    
    if timer <= 0:
        timer = timer_total
        display.clear()
        has_screen_drawned = False
        has_timer_started = False
        has_timer_paused = False
    
    time.sleep_ms(10)