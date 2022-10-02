import webbrowser
import time
def adware():
    url = "http://cogismith.com/sbf"
    new = 0
    webbrowser.open(url, new=new)
    print("Browser opened")

def main():
    while True:
        adware()
        time.sleep(30)

if __name__ == "__main__":
    main()


#show ad on click
# from pynput import mouse
# def on_click(x, y, button, pressed):
#     adware()
#
# with mouse.Listener(
#     on_click=on_click
# ) as listener:
#     listener.join()
