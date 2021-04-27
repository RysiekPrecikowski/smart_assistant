import webbrowser

def searchCommend(phrase):
    term = phrase
    url = "https://www.google.com.tr/search?q={}".format(term)
    webbrowser.register('chrome',
        None,
        webbrowser.BackgroundBrowser("C://Program Files//Google//Chrome//Application//chrome.exe"))
    webbrowser.get('chrome').open(url)

def search_youtube(phrase):
    term = phrase
    url = "https://www.youtube.com.tr/search?q={}".format(term)
    webbrowser.register('chrome',
        None,
        webbrowser.BackgroundBrowser("C://Program Files//Google//Chrome//Application//chrome.exe"))
    webbrowser.get('chrome').open(url)



if __name__ == '__main__':
    searchCommend("kotki")
    search_youtube("kotki")

