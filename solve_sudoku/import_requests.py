import requests

def fetch_board():
    url = "https://sugoku.onrender.com/board?difficulty=random"
    response = requests.get(url)
    board:dict[str: list] = response.json()
    lboard:list[list] = board['board']
    a= ' '
    for i in range(len(lboard)):
        a += str(lboard[i])
    a = a.replace('[', '')
    a = a.replace(',', '')
    a = a.replace(']', '')
    a = a.replace(' ', '')
    a = a.replace('0', '.')
    return a





