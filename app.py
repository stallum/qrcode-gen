# esse projeto tem objetivo criar uma ferramenta pessoal de uso próprio
import qrcode
from PIL import Image
import os
import re

class createQrCode():

    def form():
        link = input('insira o link do seu qrcode aqui: \n')
        name = input('insira aqui que nome você quer dar a seu QrCode: \n')
        name_treted = createQrCode.tratamentoNome(name=name)
        return link, name_treted
    

    def criarQrcode(link):
        img = qrcode.make(link)
        
        createQrCode.salvarQrCode(img)

    def tratamentoNome(name):
        name = re.sub(r"\s", "_", name)
        name = re.sub(r'[<>:"/\\|?*]', '', name)
        name = name.replace("'", "")
        return name

        
    
    def salvarQrCode(img, name):
        output_path = '_qrcodes'

        if not os.path.exists(output_path, name):
            os.makedirs(output_path)
            print('Diretório criado com sucesso!')

        

        img.save(f'{name}.png')


        return name

if __name__ == "__main__":
    
    link_do_qrcode, nome_do_arquivo = createQrCode.form()
    createQrCode.criarQrcode(link_do_qrcode, nome_do_arquivo)
    print(f"QR Code '{nome_do_arquivo}.png' criado com sucesso!")
