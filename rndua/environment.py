import random

class EnvironmentGenerator:

    def __init__(self):
        # from https://apple.fandom.com/wiki/List_of_Mac_OS_versions
        self.os_x_32=['10.4.4','10.4.5','10.4.6','10.4.7','10.4.8',
                '10.4.9','10.4.10','10.4.11','10.5.0','10.5.1',
                '10.5.2','10.5.3','10.5.4','10.5.5','10.5.6','10.5.7',
                '10.5.8','10.6.0','10.6.1','10.6.2','10.6.3','10.6.4',
                '10.6.5','10.6.6','10.6.7','10.6.8','10.7.0','10.7.1',
                '10.7.2','10.7.3','10.7.4','10.7.5']
        self.os_x_64=['10.8.0','10.8.1','10.8.2','10.8.3','10.8.4',
                '10.8.5','10.9.0','10.9.1','10.9.2','10.9.3','10.9.4',
                '10.9.5','10.10.0','10.10.1','10.10.2','10.10.3',
                '10.10.4','10.10.5','10.11.0','10.11.1','10.11.2',
                '10.11.3','10.11.4','10.11.5','10.11.6','10.12.0',
                '10.12.1','10.12.2','10.12.3','10.12.4','10.12.5',
                '10.12.6','10.13.0','10.13.1','10.13.2','10.13.3',
                '10.13.4','10.13.5','10.13.6','10.14.0','10.14.1',
                '10.14.2','10.14.3','10.14.4']

    def get_os_x_versions(self,x86=False,x64=True):
        pool=[]
        if x86:
            pool+=self.os_x_32
        if x64:
            pool+=self.os_x_64
        return pool

    def get_random_os_x_version(self,x86=False,x64=True):
        pool=self.get_os_x_versions(x86=x86,x64=x64)
        return pool[random.randint(0,len(pool)-1)]

    def os_x_version_to_firefox(self,version):
        ver=version.split('.')
        return ver[0]+'.'+ver[1]

    def os_x_version_to_chrome(self,version):
        return version.replace('.','_')