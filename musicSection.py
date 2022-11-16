import requests
from basicsFunctions import *
from selenium import webdriver

def musicHome():
    speak('welcome to the music section, what type of music you want to listen.')
    query = takeCommand().lower()

    if 'top 15' in query:
        speak('hindi or english')
        lang = takeCommand().lower()
        if 'hindi' in lang:
            hindiTop15()
        if 'english' in lang:
            engTop15()

    elif 'romantic' in query:
        speak('hindi or english')
        lang = takeCommand().lower()
        if 'hindi' in lang:
            hindiRomantic()
        if 'english' in lang:
            engRomantic()
    else:
        speak('music not found')

def hindiTop15():
    try:
        driver = webdriver.Chrome()
        driver.get('https://music.youtube.com/playlist?list=PL_yIBWagYVjwYmv3PlwYk0b4vmaaHX6aL')
        button = driver.find_element_by_xpath("//paper-button[@id='button'][@aria-label='Shuffle']")
        button.click()
        playPause(driver)
    except Exception as e:
        print(e)

def engTop15():
    try:
        driver = webdriver.Chrome()
        driver.get('https://www.jiosaavn.com/featured/weekly-top-songs/LdbVc1Z5i9E_')
        
        button = driver.find_element_by_class_name('u-margin-bottom-none@sm')
        button.click()
        playPause(driver)
    except Exception as e:
        print(e)

def hindiRomantic():
    try:
        driver = webdriver.Chrome()
        driver.get('https://www.jiosaavn.com/featured/pop-romance/TQoDMbUj9ubc1EngHtQQ2g__')
        button = driver.find_element_by_class_name('play')
        button.click()
        playPause(driver)
    except Exception as e:
        print(e)

def engRomantic():
    try:
        driver = webdriver.Chrome()
        driver.get('https://www.jiosaavn.com/featured/heartbeats/8j,bJexTYcE_')
        button = driver.find_element_by_class_name('play')
        button.click()
        playPause(driver)
    except Exception as e:
        print(e)

def playPause(driver):
    state = takeCommand().lower()

    if 'pause' in state:
        try:
            pause = driver.find_element_by_id('pause')
            pause.click()
            playPause(driver)
        except Exception as e:
            close = driver.find_element_by_id('panel-close')
            close.click()
            playPause(driver)

    elif 'play' in state:
        try:
            play = driver.find_element_by_id('play')
            play.click()
            playPause(driver)
        except Exception as e:
            close = driver.find_element_by_id('panel-close')
            close.click()
            playPause(driver)
    
    elif 'next' in state:
        try:
            fwd = driver.find_element_by_class_name('next-button')
            fwd.click()
            playPause(driver)
        except Exception as e:
            close = driver.find_element_by_id('panel-close')
            close.click()
            playPause(driver)
    
    elif 'previous' in state:
        try:
            rew = driver.find_element_by_id('rew')
            rew.click()
            playPause(driver)
        except Exception as e:
            close = driver.find_element_by_id('panel-close')
            close.click()
            playPause(driver)

    elif 'stop music' in state:
        driver.close()

    elif 'close login' in state:
        close = driver.find_element_by_id('panel-close')
        close.click()
        playPause(driver)
        
    else:
        playPause(driver)