import os
import subprocess

def check_avd_available(avd_name : str = ''):
    if not avd_name : return False
    
    avd_list = subprocess.check_output(['emulator', '-list-avds'])
    avd_list = [avd for avd in avd_list.decode().split("\n") if avd]
    if avd_name in avd_list :
        return True
    return False

def create_avd(avd_name : str = ''):
    if not avd_name : return
    
    if check_avd_available(avd_name) : 
        print('The avd is available')
        return
    
    try:
        output = subprocess.check_output(
            f'''avdmanager create avd -n {avd_name} -k "system-images;android-29;default;x86" -b x86 -c 100M -d 7 -f''',
            shell=True
        ).decode()
        
        print(output.replace('\n','').strip())
                    
    except subprocess.CalledProcessError as e:
        print(f"Error: {e.output}")
    return None

def delete_avd(avd_name : str = ''):
    if not avd_name : return
    
    if not check_avd_available(avd_name) : 
        print('The avd is not available')
        return
    
    try:
        output = subprocess.check_output(
            f"avdmanager delete avd -n {avd_name}",
            shell=True
        ).decode()

        print(output.replace('\n','').strip())
        
    except subprocess.CalledProcessError as e:
        print(f"Error: {e.output}")
    return None

