import unittest
import os
import django
import appium
import subprocess
import random

from appium.webdriver.appium_service import AppiumService
from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
from PIL import Image

from log import Log
from utils import set_log, reduce_img_size
from conf import PRJ_PATH
from conf import LOG_LEVEL, LOG_DIR, LOG_IN_ONE_FILE

# setup django settings
from django.conf import settings
if not os.environ.get('DJANGO_SETTINGS_MODULE', ''):
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'surviral_avd.settings')
django.setup()

from twbot.bot import InstaBot
from twbot.utils import start_app, random_sleep
from verify import FuncaptchaAndroidUI, RecaptchaAndroidUI
from twbot.actions.profile import ProfilePage
from twbot.actions.tweet import Tweet
from utils import run_cmd, pkill_process_after_waiting
from utils import *

LOGGER = set_log(PRJ_PATH, __file__, __name__, log_level=LOG_LEVEL,
        log_dir=LOG_DIR)


class TestAvd(unittest.TestCase):

    def test_get_avd_options(self):
        #  tw = InstaBot('android_274')
        tw = InstaBot('android_387')
        options = tw.get_avd_options()
        LOGGER.info(f'AVD options: {options}')

    def start_appium(self, port):
        # start appium server
        LOGGER.debug(f'Start appium server, port: {port}')
        server = AppiumService()
        server.start(
            args=["--address", "127.0.0.1", "-p", str(port), "--session-override"]
        )
        if server.is_running and server.is_listening:
            LOGGER.info('Appium server is running')
            return server
        else:
            LOGGER.info('Appium server is not running')
            return False

    def stop_appium(self):
        LOGGER.debug(f'Start to kill appium')

        try:
            # Kill all running appium instances
            kill_cmd = "kill -9 $(pgrep -f appium)"
            kill_process = subprocess.Popen(
                [kill_cmd],
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                shell=True,
            )
            # suppress ResourceWarning: unclosed file <_io.BufferedReader name=11>
            kill_process.stdout.close()
            kill_process.stderr.close()
            kill_process.wait()
        except Exception as e:
            LOGGER.exception(e)

    def start_emulator(self, name, timezone):
        LOGGER.debug(f'Start AVD: ["emulator", "-avd", "{name}"] + '
                f'["-timezone", "{timezone}"]')
        device = subprocess.Popen(
            ["emulator", "-avd", f"{name}", '-timezone', '{timezone}'],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            universal_newlines=True,
        )
        device.stdout.close()
        device.stderr.close()

        return device


    def get_driver(self, port=4723):
        try:
            opts = {
                "platformName": "Android",
                #  "platformVersion": "9.0",    # comment it in order to use other android version
                "automationName": "uiautomator2",
                "noSign": True,
                "noVerify": True,
                "ignoreHiddenApiPolicyError": True,
                #  "systemPort": "8212",
                # "udid": f"emulator-{self.emulator_port}",
            }

            LOGGER.debug('Start appium driver')
            LOGGER.debug(f'Driver capabilities: {opts}')

            app_driver = webdriver.Remote(
                f"http://localhost:{port}/wd/hub",
                desired_capabilities=opts,
                keep_alive=True,
            )
            self.start_driver_retires = 0
        except Exception as e:
            LOGGER.exception(e)
            raise e

        return app_driver


    def send_views(self):
        self.start_appium(port=4725)
        self.get_driver(port=4725)
        ...
    
