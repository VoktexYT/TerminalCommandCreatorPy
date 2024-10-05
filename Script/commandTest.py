from Bash.command import Command
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

command = Command()
options = Options()

options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')


@command.add(only_one_value=str)
def https(value):
    try:
        driver = webdriver.Chrome(executable_path='chromedriver', chrome_options=options)
        driver.get(value)

        print(20*'-'+'\n')
        print('WebSite name:', driver.title)
        print('WebSite url:', driver.current_url)
        print('-')
        print('App cache:', driver.application_cache)
        print('-')
        print('Capabilities:', driver.capabilities)
        print('-')
        print('WebBrowser name:', driver.name)
        print('WebBrowser version:', driver.capabilities['browserVersion'])
        print('-')
        print('Driver name:', driver.name)
        print('Driver version:', driver.capabilities[driver.name]['chromedriverVersion'].split(' ')[0])
        print(20*'-'+'\n')

        driver.close()
    except:
        print('error...')
