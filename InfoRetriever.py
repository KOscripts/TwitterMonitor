from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time


class InfoRetriever():

    def __init__(self):
        self.browser = webdriver.Chrome()
        self.browser.set_window_size(1200, 800)
#preload function is to load the webdriver to minimize delay upon receiving tweet of interest from stream.
    def preload(self):
        self.browser.get('https://www.google.com/')

#below is sample code for how you may want to interact with the webpage retrieved from the url extracted from 
#the tweet of interest, change the following to suit your needs.
    def info_retrieve(self, url):
        start_time = time.time()
        self.browser.get(url)
        step_one = True

        try:
            Purchase_button = self.browser.find_element_by_xpath(
                'button1 xpath')
            Purchase_button.click()
            print(' button 1 was successful')
        except:
            try:
                Purchase_button = self.browser.find_element_by_xpath(
                   'button2 xpath' )
                Purchase_button.click()
                print('button 2 was successful')
            except:
                try:
                    Purchase_button = self.browser.findElement(
                        By.XPATH('button3 xpath'))
                    Purchase_button.click()
                    print('button 3 was successful')
                except:
                    try:
                        Purchase_button = self.browser.findElement(
                            By.XPATH('button4 xpath'))
                        Purchase_button.click()
                        print('button 4 was successful')
                    except:
                        try:
                            Purchase_button = self.browser.findElement(
                                By.XPATH('button5 xpath'))
                            Purchase_button.click()
                            print('pbutton 5 was successful')
                        except:
                            try:
                                Purchase_button = self.browser.findElement(
                                    By.XPATH('button6 xpath'))
                                Purchase_button.click()
                                print('button 6 was successful')
                            except:
                                try:
                                    Purchase_button = self.browser.find_element_by_xpath(
                                        '//button[1]')
                                    Purchase_button.click()
                                    print(' button 7 was successful')
                                except:
                                    try:
                                        Purchase_button = self.browser.find_element_by_xpath(
                                            '//a[1]')
                                        Purchase_button.click()
                                        print(' button 8 was successful')
                                    except:
                                        print('All buttons failed')
                                        step1 = False
                                        self.screenshot('')
                                        self.html('')
        if step_one == True:
            form = self.browser.find_element_by_xpath('//form[1]')
            self.screenshot('Pageform')
            self.html('Pageform', form)
            print('Successful probe')
            print('Completed task in:', time.time() - start_time)
        else:
            pass
#screenshot will take a screen shot of the generated webpage this will happen upon success or failure of the above
#function
    def screenshot(self, filename):
        self.browser.save_screenshot(
            fr'insertDirectoryPath{filename}.png')
#html retrieves page source for the generated webpage and also upon forms selenium tries to interact with
    def html(self, pagename, tagname='none'):

        TotalHtml = self.browser.page_source
        with open(r'insertDirectoryPath\Totalhtml.html', 'w', encoding='utf-8') as fp:
            fp.write(TotalHtml)

        if tagname != 'none':
            innerHtml = tagname.get_attribute('innerHTML')
            with open(r'insertDirectoryPath\innerhtml.docx', 'w', encoding='utf-8') as fp:
                fp.write(innerHtml)

        else:
            pass
