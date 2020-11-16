from selenium import webdriver
import time


class WhatsappBot:
    def __init__(self):
        self.mensagem = "Oi, eu sou um robô e estou mandando esta mensagem pra dizer que vamos dominar o mundo!"
        self.grupos = ["Grupo1", "Grupo2"]
        options = webdriver.ChromeOptions()
        options.add_argument('lang=pt-br')
        self.driver = webdriver.Chrome(executable_path=r'./chromedriver86.exe')

    def EnviarMensagens(self):
        self.driver.get('https://web.whatsapp.com')
        time.sleep(30)
        for grupo in self.grupos:
            grupo = self.driver.find_element_by_xpath(
                f"//span[@title='{grupo}']")
            time.sleep(10)
            grupo.click()
            text_box = self.driver.find_elements_by_class_name("_3uMse")
            time.sleep(10)
            for tb in text_box:
                tb.click()
                tb.send_keys(self.mensagem)
            btn_enviar = self.driver.find_element_by_xpath(
                "//span[@data-testid='send']")
            time.sleep(5)
            btn_enviar.click()
            time.sleep(5)


bot = WhatsappBot()
bot.EnviarMensagens()
