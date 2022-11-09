MQTT em Python - Com Dashboard

1-	Utilizando o VS Code e a versão do Python disponível;

2-	Você precisará instalar as bibliotecas:

  a.	paho-mqtt -  pip install paho-mqtt
  
  b.	tkinter – pip install tk

3-	Iremos utilizar o broker gratuito disponível em http://www.mqtt-dashboard.com/

4-	Para acompanhar a utilização do Broker utilizaremos o software https://mqtt-explorer.com/   -  https://github.com/thomasnordquist/MQTT-Explorer/releases/download/0.0.0-0.4.0-beta1/MQTT-Explorer-0.4.0-beta1.exe

5- Utilize os códigos disponíveis aqui neste repositório:

  a. O arquivo mqtt-publish.py possui um exemplo de agente responsável por gerar dados aleatórios e envia-los ao Broker.
  
  b. O arquivo mqtt-dash.py possui a interface gráfica responsável por apresentar os dados coletados do Broker, assim como enviar novos dados.
  
6- Após baixar os códigos você deve executar primeiro o mqtt-dash.py , você verá uma interface gráfica ainda sem valores;

7- Agora você deve executar o arquivo mqtt-publish.py e assim que as informações começarem a ser publicadas a interface aberta irá se atualizar e exibir as mesmas informações.

Desafios - Acrescente novas informações ao processo de movo a torna-lo mais próximo do seu projeto.

Teoria envolvida na prática
https://www.gta.ufrj.br/ensino/eel878/redes1-2019-1/vf/mqtt/

Exemplo mais detalhado em:

https://highvoltages.co/category/iot-internet-of-things/how-to-mqtt/
