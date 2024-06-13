import os
import subprocess


def delete_avd(avd_name : str = ''):
    if not avd_name : return
    
    
    try:
        output = subprocess.check_output(
            f"avdmanager delete avd -n {avd_name}",
            shell=True
        ).decode()

        print(output.replace('\n','').strip())
        
    except subprocess.CalledProcessError as e:
        print(f"Error: {e.output}")
    return None

def check_avd_available():
    
    avd_list = subprocess.check_output(['emulator', '-list-avds'])
    avd_list = [avd for avd in avd_list.decode().split("\n") if avd]

    for avd in avd_list :
        if avd.startswith('xana_') :
            print('deleted avd :',avd)
            delete_avd(avd)

check_avd_available()