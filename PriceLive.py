#AmirAli Pyrovi
import turtle
import requests
url = "https://raw.githubusercontent.com/iran-market/iran-market.github.io/main/data/popular.json"
screen = turtle.Screen()
screen.setup(600, 400)
screen.title("قیمت دلار و طلا")
screen.bgcolor("#101820")
t = turtle.Turtle()
t.hideturtle()
t.speed(0)
t.penup()
def write_text(x, y, text, color, size):
    t.goto(x, y)
    t.color(color)
    t.write(text, align="center", font=("Vazirmatn", size, "bold"))
def draw_box():
    t.goto(-240, 160)
    t.setheading(0)
    t.pensize(3)
    t.color("#00D9FF")
    t.pendown()
    for i in range(2):
        t.forward(480)
        t.right(90)
        t.forward(320)
        t.right(90)
    t.penup()
def draw_button():
    t.goto(-90, -120)
    t.setheading(0)
    t.color("#00FF99")
    t.pensize(2)
    t.pendown()
    for i in range(2):
        t.forward(180)
        t.left(90)
        t.forward(40)
        t.left(90)
    t.penup()
    write_text(0, -110, "به‌روزرسانی قیمت", "#00FF99", 15)
def update_price():
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        data = response.json()["data"]
        dollar = None
        gold = None
        for item in data:
            if item["symbol"] == "USD_IRR_FREE":
                dollar = item["price"]
            elif item["symbol"] == "GOLD_18K_IRR":
                gold = item["price"]
        dollar_text = format(dollar, ",") if dollar is not None else "ناموجود"
        gold_text = format(gold, ",") if gold is not None else "ناموجود"
        t.clear()
        draw_box()
        write_text(0, 105, "قیمت لحظه‌ای بازار", "#00D9FF", 25)
        write_text(0, 45, "قیمت دلار: " + dollar_text + " تومان", "#00FF66", 20)
        write_text(0, -5, "قیمت طلای ۱۸ عیار: " + gold_text + " تومان", "#FFD54F", 20)
        draw_button()
    except Exception as e:
        print("خطا:", e)
def click_button(x, y):
    if -90 <= x <= 90 and -120 <= y <= -80:
        update_price()
draw_box()
write_text(0, 105, "قیمت لحظه‌ای بازار", "#00D9FF", 19)
write_text(0, 45, "قیمت دلار: ---", "#00FF66", 14)
write_text(0, -5, "قیمت طلای ۱۸ عیار: ---", "#FFD54F", 14)
draw_button()
screen.onclick(click_button)
turtle.done()
