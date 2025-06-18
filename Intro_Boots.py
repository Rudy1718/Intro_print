import os
import sys
import pyautogui
import shutil
import requests
import webbrowser
import subprocess
import threading
import re
import time
import asyncio
import itertools
from concurrent.futures import ThreadPoolExecutor, wait
from glob import glob
from queue import Queue
from fake_headers import Headers
from selenium import webdriver



def boots():
    os.system("")

    class bcolors:
        OKGREEN = '\033[92m'
        ENDC = '\033[0m'

    print(bcolors.OKGREEN + r"""  
  ___     ____                    _         
 |_ _|   | __ )    ___     ___   | |_   ___ 
  | |    |  _ \   / _ \   / _ \  | __| / __|
  | |    | |_) | | (_) | | (_) | | |_  \__ \
 |___|   |____/   \___/   \___/   \__| |___/
                                                                            
    """ + bcolors.ENDC) 

    time.sleep(50)

boots()