#https://www.youtube.com/watch?v=H-XpwSz4x8Y
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import telepot
import time, sys

options = webdriver.ChromeOptions()
options.add_argument(r"--user-data-dir=C:\Users\Gilson Barbosa\AppData\Local\Google\Chrome\User Data\Profile 3") #e.g. 
options.add_argument(r'--profile-directory=YourProfileDir') #e.g. Profile 3
options.headless = False
navegador = webdriver.Chrome(options=options, service=Service(ChromeDriverManager().install()))

url = f'https://www.viajanet.com.br/passagens-aereas/madrugada'

while True:
    try:
        navegador.get(url)
        time.sleep(5)
        navegador.execute_script("document.getElementsByClassName('-md -default eva-3-btn-ghost')[0].click()")
        
        for x in range(1,11):

            # Divs que estão as informações   
            div       = navegador.find_element_by_xpath(f'//*[@id="Offers_9834"]/meta-component/div/offers/div/div[2]/offer-card[{x}]/div/a') 
            div1      = navegador.find_element_by_xpath(f'//*[@id="Offers_9834"]/meta-component/div/offers/div/div[2]/offer-card[{x}]/div/a/div/div[2]/div/offer-card-info/div[3]')
            imagem    = navegador.find_element_by_xpath(f'//*[@id="Offers_9834"]/meta-component/div/offers/div/div[2]/offer-card[{x}]/div/a/div/div[1]/img')
            tipo      = navegador.find_element_by_xpath(f'//*[@id="Offers_9834"]/meta-component/div/offers/div/div[2]/offer-card[{x}]/div/a/div/div[2]/div/div/ul/li/span/span')
            preco     = navegador.find_element_by_xpath(f'//*[@id="Offers_9834"]/meta-component/div/offers/div/div[2]/offer-card[{x}]/div/a/div/div[2]/offer-card-pricebox/div/div[2]/div/span[2]')
            
            # Id do anuncio 1
            titulo    = div.get_attribute('title')
            link      = div.get_attribute('href')
            descricao = div1.get_attribute('outerText')
            imagem1   = imagem.get_attribute('src')
            tipo1     = tipo.get_attribute('outerText')
            preco1    = preco.get_attribute('outerText')

            # Mensagem do telegram
            postagem  = '{} \n\n{}\n\n{}\n\nR$ {},00\n\n{}'.format(titulo,descricao,tipo1,preco1,link)

            # Bot telegram
            chave     = '5898560730:AAGd42BUUpsMKTR_9_WZ8H2OqrZoLDEWvLk'
            bot       = telepot.Bot(chave)
            resposta  = bot.getUpdates()
            
            bot.sendPhoto(-847974863, imagem1)
            bot.sendMessage(-847974863, postagem)

            time.sleep(10)

    except Exception as e:
        print('A busca falhou')
    
    for i in range(30,-1,-1):
        sys.stdout.write("\rNova busca vai ser executada em: {}".format(i))
        sys.stdout.flush()
        time.sleep(1)

    print ("\nRealizando Nova busca")