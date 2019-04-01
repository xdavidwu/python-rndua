from rndua.browser import BrowserGenerator
from rndua.environment import EnvironmentGenerator
from rndua.format import Formatter

class RandomUAGenerator():
    def __init__(self):
        self.bg=BrowserGenerator()
        self.eg=EnvironmentGenerator()
        self.fm=Formatter()

    def get_random_android_chrome_ua(self,chrome_minimum=60,
            chrome_maximum=74,android_minimum='4.0.1',
            android_maximum='9.0.0'):
        return self.fm.format_chrome_ua(
                self.fm.android_environment_to_ua(
                    self.eg.get_random_android_environment(
                        minimum=android_minimum,maximum=android_maximum)),
                self.bg.get_random_chrome_version(minimum=chrome_minimum,
                    maximum=chrome_maximum))
