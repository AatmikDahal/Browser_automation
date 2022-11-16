from parser.page_parser import useless_page 
from selenium.webdriver.chrome.service import Service
from selenium import webdriver


def launch_browser():
    chrome_driver = Service(r"C:\Users\lenovo\Downloads\chromedriver_win32\chromedriver.exe")
    brave_browser = r'C:\Program Files\BraveSoftware\Brave-Browser\Application\brave.exe'

    Option =webdriver.ChromeOptions()
    Option.binary_location = brave_browser
    Option.add_experimental_option('excludeSwitches', ['enable-logging'])
    Option.add_experimental_option('detach',True)

    browser = webdriver.Chrome(service=chrome_driver, options=Option)

    browser.get('https://theuselessweb.com/')
    return browser    
    

go_to_site = useless_page(launch_browser())
go_to_site.search 