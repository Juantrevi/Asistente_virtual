import pyttsx3
import speech_recognition as sr
import pywhatkit
import yfinance as yf
import pyjokes
import webbrowser
import datetime
import wikipedia
import abrir_historias

#Opciones de voz / idioma
id1 = 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_ES-MX_SABINA_11.0'
id2 = 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0'

# Escuchar el microfono y devolver el audio como texto
def transformar_audio_en_texto():
    #Almacenar el reconocedor en una variable
    r = sr.Recognizer()

    #Configurar el microfono
    with sr.Microphone() as origen:

        #Pequeño tiempo de espera desde que se activa el volumen a empezar a escuchar
        r.pause_threshold = 0.8

        #Informar que comenzo la grabacion
        print('Ya puedes hablar')

        #Guardar lo que escuche como audio
        audio = r.listen(origen)

        try:
            #Buscar en google lo que haya escuchado
            pedido = r.recognize_google(audio, language="es-ar")

            #Imprimir en pantalla lo que se diji
            print('Dijiste: ' + pedido)

            #Devovler a pedido.
            return pedido

        #En caso que no comprenda el audio
        except sr.UnknownValueError:

            #Prueba de que no comprendio el audio
            print("Ups, no entendi")

            #Devolver error
            return "Sigo esperando"

        #En caso de grabar el audio pero que no pudo pasarlo a string
        except sr.RequestError:

            #Prueba de que no comprendio el audio
            print("Ups, no se que paso. No entendi")

            #Devolver error
            return "Sigo esperando, error inesperado"

        #En caso de errores que no sepamos que fue
        except:

            #Prueba de que no comprendio el audio
            print("Ups, no entendi, algo salio mal")

            #Devolver error
            return "Sigo esperando, no se que paso..."


#Funcion para que el asistente pueda ser escuchado
def hablar(mensaje):

    #Encender el motor de pyttsx3
    engine = pyttsx3.init()
    engine.setProperty('voice', id1)

    #Pronunciar mensaje
    engine.say(mensaje)
    engine.runAndWait()


#Tener en cuenta que se pueden descargar varias voces, leccion 183
#Las que tenemos aca son estas.
#Para ver las que tenemos:
# engine = pyttsx3.init()
# for v in engine.getProperty('voices'):
#     print(v)


#Informar el dia de la semana
def pedir_dia():

    #Crear la variable con datos de hoy
    dia = datetime.date.today()
    print(dia)

    #Crear variable para el dia de la semana
    dia_semana = dia.weekday()
    print(dia_semana)

    #Diccionario que contenga los nombre de los dias
    calendario = {0:'Lunes',
                  1:'Martes',
                  2:'Miércoles',
                  3:'Jueves',
                  4:'Viernes',
                  5:'Sábado',
                  6:'Domingo'}

    #Decir el dia de la semana
    hablar(f'Hoy es {calendario[dia_semana]}')


#Informar que hora es
def pedir_hora():

    #Crear una variable con datos de la hora
    hora = datetime.datetime.now()
    hora = f'Hola Juan, en este momento son las {hora.hour} horas con {hora.minute} minutos y {hora.second} segundos'
    print(hora)

    #Decir la hora
    hablar(hora)

#Hacer un saludo inicial
def saludo_inicial():

    #Crear variable con datos de hora
    hora = datetime.datetime.now()
    if hora.hour < 6 or hora.hour > 20:
        momento = f'Hola, Explicame ¿qué hacés trabajando a las {hora.hour} horas? '
    elif 6 <= hora.hour < 13:
        momento = f'Hola, Estas en un horario razonable de trabajo, son las {hora.hour} horas y {hora.minute}.'
    else:
        momento = 'Hola, Estas en un horario que ya podrias ir pensando en irte a tu casa y dejar de joder'


    #Decir el saludo
    hablar(f'{momento}, Son las {hora.hour} horas y {hora.minute} minutos. Soy margaríta, la hija de Kuki.'
           f' Trabajo mejor en grupo pediátrico que vos.'
           f'Por mas que todavía no se hablar, el tío Juan (Que en verdad es mi papá) y es mejor que maxi, me '
           f'esta dando una inteligencia superior a la tuya.'
           f' Por favor, decime ¿en qué te puedo ayudar?.')

#Funcion central del asistente
def pedir_cosas():

    #Activar el saludo inicial
    saludo_inicial()

    #Variable de corte
    comenzar = True

    #Loop central
    while comenzar:

        #Activar el microfono y guardar el pedido en un string
        pedido = transformar_audio_en_texto().lower()

        if 'abrir youtube' in pedido:
            hablar('Por mas que abra youtube, nacho lo bloqueo. Ponete a laburar hijo de puta')
            webbrowser.open('https://www.youtube.com')
            continue
        elif 'abrir google' in pedido:
            hablar('Ahora lo abro, pero espero que no sea para boludear. No lo quiero a Maxi')
            webbrowser.open('https://www.google.com')
            continue
        elif 'abrir gomedisys' in pedido:
            hablar('Me gusta que no boludees y trabajes, abriendo gomedysis. Nacho estaria muy orgulloso de vos')
            webbrowser.open('https://gomedisys.welii.com/')
            continue
        elif 'qué día es hoy' in pedido:
            pedir_dia()
            continue
        elif 'qué hora es' in pedido:
            pedir_hora()
            continue
        elif 'descárgame las historias' in pedido:
            hablar('Era hora que te pongas a trabajar. Ahí las descargo, mandale saludos a papá')
            abrir_historias.descargar_historias()
            continue
        elif 'margarita buscar sobre' in pedido:
            pedido = pedido.replace('margaríta buscar sobre', '')
            hablar(f'Buscando sobre {pedido}, espero que sea algo de medicína')
            wikipedia.set_lang('es')
            resultado = wikipedia.summary(pedido, sentences=1)
            hablar('No es de medícina, pero por ahora la voy a dejar pasar, maxi se la come.')

            hablar(resultado)
            continue


pedir_cosas()


















