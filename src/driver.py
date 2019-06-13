from selenium import webdriver

class WebDriverHandler(object):

    def __init__(self):
        pass

    def launch_firefox(self):
        options = self.webdriver = webdriver.FirefoxProfile()
        options.accept_untrusted_certs = True
        options.accept_untrusted_cert_issuer = False
        self.webdriver = webdriver.Firefox(firefox_profile=options)
