import requests, os #requests(3rd party Module)

dir_path = os.path.join(os.getcwd(),'CN All Lectures')
if not os.path.exists(dir_path):
    os.mkdir(dir_path,0o666)

for lecNum in range(1,37):

    url = "https://drqasimali.com/wp-content/uploads/2019/01/CN-Lec-"+('0' if lecNum < 9 else '') +str(lecNum)+".ppt"

    print(f'Downloading Lecture Number {lecNum}')
    response = requests.get(url,stream = True)
    
    if response.status_code == 200:
  
        with open(os.path.join(dir_path,f'Lecture-{lecNum}.ppt'), 'wb') as ppt: 
            for block in response.iter_content(chunk_size=1024):
                ppt.write(block)

print('successfully downloaded')
