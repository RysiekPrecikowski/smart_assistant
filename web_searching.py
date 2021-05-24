import webbrowser
from recognition_engine import Recognition_engine

def search_google(phrase):
    if len(phrase) < 1:
        phrase = Recognition_engine().get_transcript(text="what do you wanna find?")

    term = phrase
    url = "https://www.google.com.tr/search?q={}".format(term)
    webbrowser.register('chrome',
        None,
        webbrowser.BackgroundBrowser("C://Program Files//Google//Chrome//Application//chrome.exe"))
    webbrowser.get('chrome').open(url)

def search_youtube(phrase):
    if len(phrase) < 1:
        phrase = Recognition_engine().get_transcript(text="what do you wanna find?")

    term = phrase
    url = "https://www.youtube.com.tr/search?q={}".format(term)
    webbrowser.register('chrome',
        None,
        webbrowser.BackgroundBrowser("C://Program Files//Google//Chrome//Application//chrome.exe"))
    webbrowser.get('chrome').open(url)



if __name__ == '__main__':
    search_google("kotki")
    search_youtube("kotki")

