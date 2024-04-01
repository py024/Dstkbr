import requests

def send(channel_id: int, token: str, message: str):
    url = 'https://discord.com/api/v9/channels/'+channel_id+'/messages'
    data = {"content": message}
    header = {"authorization": token}
    send = requests.post(url, data=data, headers=header)
    if send.status_code == 200:
        print(f"メッセージを送りました！(channelID:${channel_id},message:${message})")
    else:
     print(f"メッセージを送るのに失敗しました！(token:${token},channelID:${channel_id},message:${message})")

def nick(token: str, nick: str):
    url = 'https://discord.com/api/v9/users/@me'
    headers = {
        'authorization': token,
        'Content-Type': 'application/json',
    }
    data = {
        'nick': nick
    }
    response = requests.patch(url, headers=headers, json=data)
    
    if response.status_code == 200:
        print(f"ニックネームを変更しました！(新しいニックネーム: ${nick})")
    else:
        print(f"ニックネームの変更に失敗しました。")
   
