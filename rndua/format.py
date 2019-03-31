class Formatter:

    def __init__(self):
        return

    def os_x_version_to_firefox(self,version):
        ver=version.split('.')
        return 'Macintosh; Intel Mac OS X %s.%s; '%(ver[0],ver[1])

    def os_x_version_to_chrome(self,version):
        return 'Macintosh; Intel Mac OS X '+version.replace('.','_')

    def windows_nt_version_to_ua(self,version):
        return 'Windows NT '+version
