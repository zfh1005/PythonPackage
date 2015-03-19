import configparser

IQ_TEST_FINISHED_FILE_NAME = r'TestStartUp.ini'

class myconfigparser(configparser.ConfigParser):
    def __intt__(self, defaults = None):
        configparser.ConfigParser.__init__(self, defaults = None)
    def optionxform(self, optionstr):
        return optionstr

def readIniFileValue(filename, section, option):
    cf = myconfigparser()
    cf.read(filename)
    if section in cf.sections():
        if option in cf.options(section): 
            return cf.get(section, option)
        else:
            return 'please check %s in %s.'%(option, section)
    else:
        return 'please check %s in %s.'%(section, filename)
    
def writeIniFileValue(filename, section, option, value):
    cf = myconfigparser()
    cf.read(filename)
    cf.set(section, option, value)
    cf.write(open(filename, 'w'))
 
if __name__ == '__main__':
    writeIniFileValue(IQ_TEST_FINISHED_FILE_NAME, "TESTER_CONTROL", "CTRL_MODE", "0")
    print(readIniFileValue(IQ_TEST_FINISHED_FILE_NAME, "TESTER_CONTROL", "CTRL_MODE")) 
        
