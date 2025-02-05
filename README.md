
# Against Toxic Telegram Bot

## Описание

**Against Toxic Telegram Bot** — это Telegram-бот, предназначенный для автоматического анализа и удаления токсичных сообщений в группах и каналах. Он использует модель **Detoxify** для определения токсичности текста и автоматически удаляет сообщения, которые содержат токсичные выражения. Бот также отправляет предупреждения о токсичности в чат и записывает информацию о токсичных сообщениях в CSV-файл.

---

## Основные функции

- **Удаление токсичных сообщений**: Бот анализирует все входящие сообщения в чате и удаляет те, которые содержат токсичные выражения, такие как оскорбления, угрозы, расизм и другие виды ненависти.
- **Предупреждения о токсичности**: В случае удаления токсичного сообщения, бот отправляет предупреждение в чат с указанием категорий токсичности.
- **Логирование**: Все токсичные сообщения и их характеристики записываются в CSV-файл для дальнейшего анализа и мониторинга.
- **Улучшение атмосферы общения**: Этот бот помогает поддерживать позитивную атмосферу в чате, предотвращая распространение токсичного контента.

---

## Требования

Для работы бота необходимо установить следующие библиотеки:

```bash
pip install -r requirements.txt
```

### Зависимости

- `python-telegram-bot==20.3`: Для работы с Telegram API.
- `python-dotenv==1.0.0`: Для загрузки конфиденциальных данных из файла `.env`.
- `detoxify==0.7.0`: Для анализа токсичности сообщений.
- `torch==2.0.1`: Для работы Detoxify, так как эта библиотека использует PyTorch.
- `nest-asyncio==1.5.8`: Для поддержки вложенных циклов asyncio.

---

## Настройка

1. Создайте файл `.env` в корне проекта и добавьте ваш токен Telegram-бота:

    ```text
    TELEGRAM_TOKEN=your_telegram_bot_token
    ```

2. Добавьте бота в ваш Telegram-чат (группу или канал).
3. Убедитесь, что у бота есть права на удаление сообщений в чате.

---

## Как запустить

1. Скачайте или клонируйте репозиторий на свой компьютер.
2. Установите все зависимости с помощью команды:

    ```bash
    pip install -r requirements.txt
    ```

3. Запустите бота:

    ```bash
    python bot.py
    ```

4. Убедитесь, что токен правильно загружается из файла `.env`.

---

## Как использовать

1. После запуска бота добавьте его в вашу группу или канал.
2. Убедитесь, что у бота есть права на удаление сообщений.
3. Бот начнёт автоматически анализировать входящие текстовые сообщения на токсичность.
4. Если сообщение окажется токсичным, оно будет удалено, а в чат будет отправлено предупреждение о токсичности.

---

## Логирование

Все токсичные сообщения записываются в файл `bot_logs.csv`. Пример строки лога:

```csv
Timestamp,         User_ID,    Username,  Chat_ID,  Chat_Title, Message,                   Action,    Toxic_Categories
2025-01-18 12:34:56, 123456789, username, 987654321, Test Chat, "Это ужасное сообщение!", Deleted, toxicity, insult
```

---

## Поддержка

Для любых вопросов или проблем с настройкой бота создайте **issue** на GitHub, и я постараюсь вам помочь.

### Контактные данные

- **Telegram**: [EralyF](https://t.me/eralyf)
