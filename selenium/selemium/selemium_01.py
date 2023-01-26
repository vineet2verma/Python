import webbrowser


# https://docs.google.com/forms/d/e/1FAIpQLSeQE7uGN-_4GyBUs1Ry5y2wbpD3FCb3blfXQ9YloKfYsVBQwQ/viewform?entry.1429966859=SHOP&entry.1890821569=CREDIT+CARD&entry.574707600=453

amt = 123123
url = 'https://docs.google.com/forms/d/e/1FAIpQLSeQE7uGN-_4GyBUs1Ry5y2wbpD3FCb3blfXQ9YloKfYsVBQwQ/viewform?entry.1429966859=SHOP&entry.1890821569=CREDIT+CARD&entry.574707600=123' #+ amt

# chrome_path = r'C:\Program Files\Google\Chrome\Application\chrome.exe'

chrome_path = 'C:\Program Files\Google\Chrome\Application\chrome.exe %s --incognito'

# webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(chrome_path))
# webbrowser.get('chrome').open_new_tab(url)

webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(chrome_path))
webbrowser.get('chrome').open_new(url)


