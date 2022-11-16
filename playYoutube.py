from youtube_search import YoutubeSearch
import json
from basicsFunctions import takeCommand
from basicsFunctions import speak
from selenium import webdriver

def getLink(query):
    results = YoutubeSearch(query, max_results=1).to_json()

    jsonArray=json.loads(results)

    print(jsonArray)
    try:
        link="https://www.youtube.com/watch?v=Y963o_1q71M"
        # link="https://www.youtube.com"+jsonArray['videos'][0]['link']
        return link
    except Exception as e:
        speak("sorry, i cant find any music or video.")
        return "zero"

def playMain(query):
    link=getLink(query)
    if link == "zero":
        return False
    driver=None
    try:
        driver = webdriver.Chrome()
        driver.get(link)
        button = driver.find_element_by_class_name('ytp-play-button')
        button.click()
        driver=driver
        playPause(driver)
    except Exception as e:
        print(e)
        playPause(driver)

def playPause(driver):
    state = takeCommand().lower()
    if 'pause' in state:
        try:
            pause = driver.find_element_by_class_name('ytp-play-button')
            pause.click()
            playPause(driver)
        except Exception as e:
            playPause(driver)

    elif 'play' in state:
        try:
            play = driver.find_element_by_class_name('ytp-play-button')
            play.click()
            playPause(driver)
        except Exception as e:
            playPause(driver)
    
    elif 'next' in state:
        try:
            fwd = driver.find_element_by_class_name('ytp-next-button')
            fwd.click()
            playPause(driver)
        except Exception as e:
            playPause(driver)
    
    # elif 'previous' in state:
    #     try:
    #         rew = driver.find_element_by_id('rew')
    #         rew.click()
    #         playPause(driver)
    #     except Exception as e:
    #         close = driver.find_element_by_id('panel-close')
    #         close.click()
    #         playPause(driver)

    elif 'stop video' in state:
        driver.close()
        
    else:
        playPause(driver)