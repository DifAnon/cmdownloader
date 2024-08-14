import argparse
import requests
import os
from termcolor import colored
import tqdm

#для цветов
os.system('color')

#для команд
parser = argparse.ArgumentParser()
parser.add_argument("-f", "-file", help="Link to file", required=True)
parser.add_argument("-p", "-path", help="Path of file", required=True)
parser.add_argument("-n", "-name", help="Name of file with extension", required=True)
 
args = parser.parse_args()

response = requests.get(args.f)

#для проверки
if response.status_code != 200:
    print(colored(f"\nError! Error code: {response.status_code}", 'white', 'on_red'))
else:
#для закачки
    with open(f'{args.p}\\{args.n}', 'wb') as file:
        file.write(response.content)
        
    file_size = os.path.getsize(f'{args.p}\\{args.n}')

    for i in tqdm.tqdm(range(file_size)):
        pass
    #для отображения
    print(f"\n{colored('File Download!', 'white', 'on_green')}\n\nFile Name: {args.n}\nFile Size: {file_size}B\nFile Full Path: {args.p}\\{args.n}")

