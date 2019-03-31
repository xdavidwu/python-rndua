class Formatter:

    def __init__(self):
        return

    def os_x_version_to_firefox(self,version):
        ver=version.split('.')
        return 'Macintosh; Intel Mac OS X %s.%s; '%(ver[0],ver[1])

    def os_x_version_to_chrome(self,version):
        return 'Macintosh; Intel Mac OS X '+version.replace('.','_')

    def windows_nt_version_to_ua(self,version,arch=''):
        return 'Windows NT '+version+arch

    def linux_distro_to_ua(self,distro,arch='x86_64'):
        return 'X11; '+distro+'Linux '+arch

    def android_environment_to_ua(self,env,lang='',firefox=False):
        res='Linux; '
        if lang!='': # old Android Browser
            res+='U; '
        res+='Android '
        if env[1]=='9.0.0':
            res+='9'
        elif env[1].startswith('8'):
            res+=env[1]
        elif env[1].endswith('.0'):
            res+=env[1][:-2]
        else:
            res+=env[1]
        res+='; '
        if lang!='':
            res+=lang+'; '
        elif firefox:
            res+='Mobile'
            return res
        res+=env[2]+' Build/'+env[0]
        return res
