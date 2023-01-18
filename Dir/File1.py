import requests, webbrowser


def check_facebook():
    try:
        response = requests.get("https://www.facebook.com", timeout=5)
        response.raise_for_status()
        print("Facebook is up and running!")
    except (requests.exceptions.RequestException, requests.exceptions.Timeout) as e:
        print("Facebook is down:", e)

def open_facebook():
    try:
        webbrowser.open("https://www.facebook.com", new=2, autoraise=True)
        print("Facebook is opened in the browser!")
    except Exception as e:
        print("Error Occured: ", e)



check_facebook()
open_facebook()



