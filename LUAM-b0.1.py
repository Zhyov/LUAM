import random, os, requests, time
globLang = 'no-language'
ver = 'beta v0.1'
hapVer = requests.get("https://api.github.com/repos/LukeBlack952/HAP/releases/latest").json()
hapVer = hapVer['tag_name']
luamVer = requests.get("https://api.github.com/repos/LukeBlack952/LUAM/releases/latest").json()
luamVer = luamVer['tag_name']
hapFullRel = None
isBeta = None
itr = 0
if '.' in hapVer.replace('0.', ''):
    hapFullRel = False
else:
    hapFullRel = True
if 'beta' in luamVer:
    luamVer = luamVer.replace('eta ', '')
    isBeta = True
else:
    isBeta = False
if not os.path.exists('apps'):
    os.mkdir('apps')
def start():
    global itr
    if itr == 0:
        print(msg(0, globLang))
        itr += 1
    print(msg(2, globLang))
    check = input('>> ')
    if iToF('set.app', check):
        os.system('cls')
        apps()
    elif iToF('set.extr', check):
        os.system('cls')
        extra()
    elif iToF('exit', check):
        exit()
    else:
        os.system('cls')
        print(msg(1, globLang))
    start()
def apps():
    dir = os.listdir('apps')
    for i in dir:
        fil = os.path.splitext(i)[0]
        if 'HAP' in fil:
            curVer = i.replace('HAP-', '').replace('.py', '')
            if hapVer in fil:
                print(msg(5, globLang))
            else:
                print(msg(23, globLang))
    check = input('>> ')
    if iToF('app.hap', check):
        os.system('cls')
        dir = os.listdir('apps')
        for i in dir:
            fil = os.path.splitext(i)[0]
            if 'HAP' in fil:
                curVer = i.replace('HAP-', '').replace('.py', '')
                if hapVer in fil:
                    os.system('cls')
                    os.system('apps/HAP-' + curVer + '.py')
                    os.system('cls')
                    apps()
                else:
                    os.system('cls')
                    print(msg(15, globLang))
                    check = input('>> ')
                    if iToF('yes', check):
                        os.system('cls')
                        update('HAP')
                    elif iToF('no', check):
                        os.system('cls')
                        os.system('apps/HAP-' + curVer + '.py')
                        os.system('cls')
                        apps()
                    elif iToF('back', check):
                        os.system('cls')
                        apps()
                    else:
                        os.system('cls')
                        print(msg(1, globLang))
            else:
                print(msg(6, globLang))
                check = input('>> ')
                if iToF('yes', check):
                    os.system('cls')
                    install('HAP')
                elif iToF('back', check):
                    os.system('cls')
                    apps()
                else:
                    os.system('cls')
                    print(msg(1, globLang))
    elif iToF('back', check):
        os.system('cls')
        start()
    else:
        os.system('cls')
        print(msg(1, globLang))
def install(app):
    if app == 'HAP':
        print(msg(8, globLang))
        hapLink = 'https://github.com/LukeBlack952/HAP/releases/latest/download/HAP-' + hapVer + '.py'
        print(msg(9, globLang))
        hapReq = requests.get(hapLink, allow_redirects=True)
        print(msg(10, globLang))
        open('apps/HAP-' + hapVer + '.py', 'wb').write(hapReq.content)
        print(msg(11, globLang))
        print(msg(7, globLang))
        check = input('>> ')
        if iToF('back', check):
            os.system('cls')
            apps()
        else:
            os.system('cls')
            print(msg(1, globLang))
    else:
        return
def checkAutoUpdate():
    print(msg(17,globLang))
    dir = os.listdir()
    for i in dir:
        fil = os.path.splitext(i)[0]
        if 'LUAM' in fil:
            curVer = i.replace('LUAM-', '').replace('.py', '')
            if not luamVer in fil:
                os.system('cls')
                print(msg(16,globLang))
            else:
                os.system('cls')
                start()
    check = input('>> ')
    if iToF('no', check):
        os.system('cls')
        start()
    elif iToF('yes', check):
        print(msg(14, globLang))
        os.remove(i)
        print(msg(8, globLang))
        luamLink = 'https://github.com/LukeBlack952/LUAM/releases/latest/download/LUAM-' + luamVer + '.py'
        print(msg(9, globLang))
        luamReq = requests.get(luamLink, allow_redirects=True)
        print(msg(10, globLang))
        open('LUAM-' + luamVer + '.py', 'wb').write(luamReq.content)
        print(msg(11, globLang))
        exit()
    else:
        return
def update(app):
    if app == 'HAP':
        print(msg(12, globLang))
        dir = os.listdir('apps')
        for i in dir:
            fil = os.path.splitext(i)[0]
            print(msg(13, globLang))
            if 'HAP' in fil:
                print(msg(14, globLang))
                os.remove('apps/' + i)
        print(msg(11, globLang))
        print(msg(8, globLang))
        hapLink = 'https://github.com/LukeBlack952/HAP/releases/latest/download/HAP-' + hapVer + '.py'
        print(msg(9, globLang))
        hapReq = requests.get(hapLink, allow_redirects=True)
        print(msg(10, globLang))
        open('apps/HAP-' + hapVer + '.py', 'wb').write(hapReq.content)
        print(msg(11, globLang))
        print(msg(7, globLang))
        check = input('>> ')
        if iToF('back', check):
            os.system('cls')
            apps()
        else:
            os.system('cls')
            print(msg(1, globLang))
    else:
        return
def extra():
    print(msg(22, globLang))
    check = input('>> ')
    if iToF('set.seti', check):
        os.system('cls')
        settings()
    elif iToF('set.cred', check):
        os.system('cls')
        credits()
    elif iToF('back', check):
        os.system('cls')
        start()
    else:
        os.system('cls')
        print(msg(1, globLang))
    settings()
def settings():
    print(msg(3, globLang))
    check = input('>> ')
    if iToF('set.lang', check):
        os.system('cls')
        lang(True)
    elif iToF('back', check):
        os.system('cls')
        extra()
    else:
        os.system('cls')
        print(msg(1, globLang))
    settings()
def lang(sm):
    global globLang, itr
    if sm == False:
        print('\nSelect a language:\n1 - en (English)\n2 - es (Español)\n3 - ru (Русский)')
        check = input('>> ')
        if check == '1' or check.lower() == 'english' or check.lower() == 'en':
            globLang = 'en'
        elif check == '2' or check.lower() == 'español' or check.lower() == 'espanol' or check.lower() == 'es':
            globLang = 'es'
        elif check == '3' or check.lower() == 'русский' or check.lower() == 'ru':
            globLang = 'ru'
        else:
            os.system('cls')
            print('\nSorry, that is not an option. Did you spell it correctly?')
            lang(False)
    elif sm == True:
        print('\nSelect a language:\n1 - en (English)\n2 - es (Español)\n3 - ru (Русский)\n- Back')
        check = input('>> ')
        if check == '1' or check.lower() == 'english' or check.lower() == 'en':
            globLang = 'en'
            if itr == 1:
                itr -= 1
        elif check == '2' or check.lower() == 'español' or check.lower() == 'es':
            globLang = 'es'
            if itr == 1:
                itr -= 1
        elif check == '3' or check.lower() == 'русский' or check.lower() == 'ru':
            globLang = 'ru'
            if itr == 1:
                itr -= 1
        elif check.lower() == 'back':
            os.system('cls')
            settings()
        else:
            os.system('cls')
            print('\nSorry, that is not an option. Did you spell it correctly?')
            lang(True)
    os.system('cls')
    if sm == False:
        checkAutoUpdate()
    else:
        start()
def credits():
    print(msg(21, globLang))
    print(msg(7, globLang))
    check = input('>> ')
    if iToF('back', check):
        os.system('cls')
        extra()
    else:
        os.system('cls')
        print(msg(1, globLang))
    credits()
def iToF(type, chk):
    if type == 'back':
        if chk.lower() == 'back' or chk.lower() == 'volver' or chk.lower() == 'назад':
            return True
    elif type == 'exit':
        if chk.lower() == 'exit' or chk.lower() == 'salir' or chk.lower() == 'выход':
            return True
    elif type == 'set.extr':
        if chk.lower() == 'extra' or chk.lower() == 'дополнительно':
            return True
    elif type == 'set.lang':
        if chk.lower() == 'language' or chk.lower() == 'idioma' or chk.lower() == 'язык':
            return True
    elif type == 'set.cred':
        if chk.lower() == 'credits' or chk.lower() == 'créditos' or chk.lower() == 'creditos' or chk.lower() == 'кредиты':
            return True
    elif type == 'set.seti':
        if chk.lower() == 'settings' or chk.lower() == 'ajustes' or chk.lower() == 'настройки':
            return True
    elif type == 'set.app':
        if chk.lower() == 'applications' or chk.lower() == 'aplicaciones' or chk.lower() == 'применение':
            return True
    elif type == 'yes':
        if chk.lower() == 'yes' or chk.lower() == 'sí' or chk.lower() == 'si' or chk.lower() == 'да':
            return True
    elif type == 'no':
        if chk.lower() == 'no' or chk.lower() == 'нет':
            return True
    elif type == 'app.hap':
        if chk.lower() == 'hap':
            return True
def msg(type, lang):
    if lang == 'en':
        if int(type) == 0:
            return '\n### Welcome to LUAM ' + ver + '! ###'
        elif int(type) == 1:
            return '\nSorry, that is not an option. Did you spell it correctly?'
        elif int(type) == 2:
            return '\nWhat would you like to do?\n- Applications\n- Extra\n- Exit'
        elif int(type) == 3:
            return '\nWhat would you like to do?\n- Language\n- Back'
        elif int(type) == 4:
            return '\nThis feature has still not been added.'
        elif int(type) == 5:
            return '\nWhat application would you like to check?\n- HAP\n- Back'
        elif int(type) == 6:
            return '\nThis application is not installed. Do you wish to install it?\n- Yes\n- Back'
        elif int(type) == 7:
            return '\nIf you want to go back, type "Back".'
        elif int(type) == 8:
            return 'Getting link...'
        elif int(type) == 9:
            return 'Getting request...'
        elif int(type) == 10:
            return 'Installing...'
        elif int(type) == 11:
            return 'Done!'
        elif int(type) == 12:
            return 'Organising files...'
        elif int(type) == 13:
            return 'Finding outdated files...'
        elif int(type) == 14:
            return 'Removing...'
        elif int(type) == 15:
            return '\nThis application is outdated. Do you wish to update it?\n- Yes\n- No\n- Back'
        elif int(type) == 16:
            return '\nLUAM is outdated. Do you wish to update it?\n- Yes\n- No'
        elif int(type) == 17:
            return 'Checking for updates...'
        elif int(type) == 21:
            return '\nCredits:\n- Code: Luke\n- Translations:\n-- English: Luke\n-- Spanish: Luke\n-- Russian: DeepL Translate\n- Ideas: Luke'
        elif int(type) == 22:
            return '\nWhat  would you like to do?\n- Settings\n- Credits\n- Back'
        elif int(type) == 23:
            return '\nWhat application would you like to check?\n- HAP (Outdated)\n- Back'
    elif lang == 'es':
        if int(type) == 0:
            return '\n### Bienvenido a LUAM ' + ver + '! ###'
        elif int(type) == 1:
            return '\nLo siento, eso no es una opción. ¿Lo has escrito correctamente?'
        elif int(type) == 2:
            return '\n¿Qué te gustaría hacer?\n- Aplicaciones\n- Extra\n- Salir'
        elif int(type) == 3:
            return '\n¿Qué te gustaría hacer?\n- Idioma\n- Volver'
        elif int(type) == 4:
            return '\nEsta función aún no se ha añadido.'
        elif int(type) == 5:
            return '\n¿Qué aplicación le gustaría comprobar?\n- HAP\n- Volver'
        elif int(type) == 6:
            return '\nEsta aplicación no está instalada. ¿Desea instalarla?\n- Sí\n- Volver'
        elif int(type) == 7:
            return '\nSi desea volver atrás, escriba "Volver".'
        elif int(type) == 8:
            return 'Obteniendo enlace...'
        elif int(type) == 9:
            return 'Obteniendo solicitud...'
        elif int(type) == 10:
            return 'Instalando...'
        elif int(type) == 11:
            return '¡Listo!'
        elif int(type) == 12:
            return 'Organizando archivos...'
        elif int(type) == 13:
            return 'Buscando archivos desactualizados...'
        elif int(type) == 14:
            return 'Eliminando...'
        elif int(type) == 15:
            return '\nEsta aplicación está desactualizada. ¿Desea actualizarla?\n- Sí\n- No\n- Volver'
        elif int(type) == 16:
            return '\nLUAM está desactualizado. ¿Desea actualizarlo?\n- Sí\n- No'
        elif int(type) == 17:
            return 'Buscando actualizaciones...'
        elif int(type) == 21:
            return '\nCréditos:\n- Código: Luke\n- Traducciones:\n-- Inglés: Luke\n-- Español: Luke\n-- Ruso: DeepL Traductor\n- Ideas: Luke'
        elif int(type) == 22:
            return '\n¿Qué te gustaría hacer?\n- Ajustes\n- Créditos\n- Volver'
        elif int(type) == 23:
            return '\n¿Qué aplicación le gustaría comprobar?\n- HAP (Desactualizado)\n- Volver'
    elif lang == 'ru':
        if int(type) == 0:
            return '\n### Добро пожаловать в LUAM ' + ver + '! ###'
        elif int(type) == 1:
            return '\nИзвините, это не вариант. Вы правильно написали?'
        elif int(type) == 2:
            return '\nЧто бы вы хотели сделать? \n- Применение\n- Дополнительно\n- Выход'
        elif int(type) == 3:
            return '\nЧто бы вы хотели сделать? \n- Язык\n- Назад'
        elif int(type) == 4:
            return '\nЭта функция до сих пор не добавлена.'
        elif int(type) == 5:
            return '\nКакое приложение вы хотите проверить?\n- HAP\n- Назад'
        elif int(type) == 6:
            return '\nЭто приложение не установлено. Вы хотите установить его?\n- Да\n- Назад'
        elif int(type) == 7:
            return '\nЕсли вы хотите вернуться назад, введите "Назад".'
        elif int(type) == 8:
            return 'Получение ссылки...'
        elif int(type) == 9:
            return 'Получение заявки...'
        elif int(type) == 10:
            return 'Устанавливая...'
        elif int(type) == 11:
            return 'Готов!'
        elif int(type) == 12:
            return 'Упорядочивание файлов...'
        elif int(type) == 13:
            return 'Нахождение устаревших файлов...'
        elif int(type) == 14:
            return 'Удаляя...'
        elif int(type) == 15:
            return '\nЭто приложение устарело. Вы хотите обновить его?\n- Да\n- Нет\n- Назад'
        elif int(type) == 16:
            return '\nLUAM устарел. Хотите ли вы обновить его?\n- Да\n- Нет'
        elif int(type) == 17:
            return 'Проверяем обновления...'
        elif int(type) == 21:
            return '\nКредиты:\n- Код: Luke\n- Переводы:\n-- Английский: Luke\n-- Испанский: Luke\n-- Русский: DeepL Translate\n- Идеи: Luke'
        elif int(type) == 22:
            return '\nЧто бы вы хотели сделать?\n- Настройки\n- Кредиты\n- Назад'
        elif int(type) == 23:
            return '\nКакое приложение вы хотите проверить?\n- HAP (Outdated)\n- Назад'
    elif lang == 'no-language':
        return 'Language Error'
lang(False)
