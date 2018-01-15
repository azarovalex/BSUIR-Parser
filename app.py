import requests     
import numpy as np   
import pandas as pd  
import time          

page_link = 'http://iis.bsuir.by/#/login'
response = requests.get(page_link)
print(response)