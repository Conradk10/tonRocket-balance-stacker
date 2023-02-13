# @tonRocketBot balance stacker
#### 💎 _Удобный помощник в сборе балансов._

<div align="center">

![Stars](https://img.shields.io/github/stars/ca4tuk/tonRocket-balance-stacker)
![Opened Issues](https://img.shields.io/github/issues-raw/ca4tuk/tonRocket-balance-stacker)
![License](https://img.shields.io/github/license/ca4tuk/tonRocket-balance-stacker)

</div>

## 🔨 Установка
1. Клонировать репозиторий: ``git clone https://github.com/ca4tuk/tonRocket-balance-stacker``
2. Перейти в директорию скрипта: ``cd tonRocket-balance-stacker``
3. Создать виртуальное окружение: ``python3 -m venv env``
4. Активировать виртуальное окружение: ``source env/bin/activate``
5. Установить зависимости: ``python3 -m pip install -r requirements.txt``
6. Вы прекрасны.

## ⚙️ Настройка конфига
_Действия ниже необязательны, при использовании большого количества аккаунтов <b>их можно и нужно пропустить</b>, все 
настроено за вас._
- Получение API пар (API_ID и API_HASH)
1. Переходим <a href="https://my.telegram.org">сюда</a> и авторизуемся через свой аккаунт.
2. Переходим в `API development tools`
3. Если приложение не создано, создаем: указываем любое имя английскими буквами, выбираем любую платформу и 
   сохраняем изменения, далее <b>копируем пару API_ID / API_HASH</b>.
4. Скопированные данные вставляем в config.py: API_ID в переменную `API_ID`, аналогично с `API_HASH`.

## ▶️ Запуск и использование
Активировать виртуальное окружение (п.4 в установке)

Запустить скрипт командой `python3 main.py @USERNAME`, где `USERNAME` - ваш @username в Telegram.
Или `python3 main.py`, указав при этом @username во время выполнения кода.

## 📝 Зависимости:
```
hikka-tl==1.24.10
loguru==0.6.0
```
