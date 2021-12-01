import subprocess # Used to launch external applications
from configparser import ConfigParser # Used to parse in the run_config.ini file

def run(software) :
    config = ConfigParser()
    config.read('commands/run/run_config.ini')

    software = software.upper()

    if not config.has_option('paths', software) :
        print(f'Path for {software} not available. Please check the commands/run/run_config.ini file.')
        return
    
    path = config.get('paths', software)
    
    subprocess.run(path)