# Module containing all Favorite urls and browsers

import webbrowser


def print_browesers():
    print("Choose Your favorite browser:")
    for key in browsers.keys():
        print(key)


def print_urls():
    print("Choose the website:")
    for key in urls.keys():
        print(key)


def open(browser, website):
    selected_browser = list(browsers.values())[browser - 1]
    selected_websit = list(urls.values())[website - 1]
    brow = webbrowser.get(selected_browser)
    brow.open(selected_websit)


browsers = {"1.chrome": "google-chrome", "2.firefox": "firefox"}

urls = {
    "1.Youtube": "https://www.youtube.com/",
    "2.Facebook": "https://www.facebook.com/",
    "3.Linked In": "https://www.linkedin.com/",
    "4.Gmail": "https://mail.google.com/",
}
