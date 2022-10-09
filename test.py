import requests
import os
import subprocess

r = subprocess.call('ping -c 1 10.14.119.8', stdin=None, stdout=None, stderr=None, shell=True)
print(r)