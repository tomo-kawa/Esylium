from selenium import webdriver

class WebDriverHandler(object):
    """WebDriver handler.
    This class wrapped the WebDriver.
    """

    def launch_firefox(self):
        """launch for firefox.
        """
        options = self.webdriver = webdriver.FirefoxProfile()
        options.accept_untrusted_certs = True
        options.accept_untrusted_cert_issuer = False
        self.webdriver = webdriver.Firefox(firefox_profile=options)
