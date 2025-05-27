Отлично, я перенесу стиль из README Open WebUI в ваш проект. Вот адаптированная версия README для вашего Telegram-бота **Against Toxic** в аналогичном стиле:

---

# Against Toxic Telegram Bot 🤖

![GitHub stars](https://img.shields.io/github/stars/Eraly-ml/against-toxic-bot?style=social)
![GitHub forks](https://img.shields.io/github/forks/Eraly-ml/against-toxic-bot?style=social)
![GitHub watchers](https://img.shields.io/github/watchers/Eraly-ml/against-toxic-bot?style=social)
![GitHub repo size](https://img.shields.io/github/repo-size/Eraly-ml/against-toxic-bot)
![GitHub language count](https://img.shields.io/github/languages/count/Eraly-ml/against-toxic-bot)
![GitHub top language](https://img.shields.io/github/languages/top/Eraly-ml/against-toxic-bot)
![GitHub last commit](https://img.shields.io/github/last-commit/Eraly-ml/against-toxic-bot?color=red)

**Against Toxic** is a simple but powerful Telegram bot that **automatically detects and removes toxic messages** from group chats. It helps you keep your community clean and respectful using machine learning.

> \[!TIP]
> Want to protect your community from hate speech, insults, and toxic behavior? Deploy **Against Toxic** in minutes and moderate with confidence!

---

## ✨ Key Features

* 🧠 **Toxicity Detection with Detoxify**
  Uses the powerful Detoxify model to analyze messages for toxicity.

* ❌ **Auto-deletion of Toxic Messages**
  Immediately deletes messages containing insults, hate, threats, or obscene language.

* ⚠️ **Warning System**
  Notifies group members about deleted messages and the reason behind the removal.

* 📊 **Logging**
  Saves details of toxic messages (user, message, toxicity scores) to a CSV file for moderation analytics.

* 💬 **Multi-language Support** *(coming soon)*
  Extendable for multilingual toxicity detection.

---

## 🛠️ Installation

### 🔌 Requirements

* Python 3.8+
* Telegram Bot Token from [@BotFather](https://t.me/BotFather)
* `pip install -r requirements.txt`

### 🚀 Quickstart

1. **Clone the repository:**

   ```bash
   git clone https://github.com/Eraly-ml/against-toxic-bot.git
   cd against-toxic-bot
   ```

2. **Install dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

3. **Set your bot token:**

   Create a `.env` file or export an environment variable:

   ```env
   TELEGRAM_TOKEN=your_bot_token_here
   ```

4. **Run the bot:**

   ```bash
   python bot.py
   ```

---

## ⚙️ How It Works

The bot listens for new messages in Telegram groups. When a message arrives:

1. It passes the message text to the `Detoxify` model.
2. If the message is flagged as toxic (above a configurable threshold), it is deleted.
3. A warning message is posted in the group.
4. The message content and toxicity scores are logged.

---

## 📂 Project Structure

```
against-toxic-bot/
├── bot.py             # Main bot logic
├── detector.py        # Toxicity detection (Detoxify wrapper)
├── logger.py          # CSV logger for moderation
├── requirements.txt   # Dependencies
└── README.md          # This file
```

---

## 📈 Example

A user sends:

> "You're such an idiot!"

Bot detects high toxicity and deletes the message, then posts:

> 🚫 Message deleted due to toxic language.

And logs:

```
Username, Message, Toxicity Score
john_doe, "You're such an idiot!", 0.92
```

---

## 🙌 Contributing

Pull requests are welcome! If you want to improve detection, add features, or fix bugs — feel free to contribute.

---

## 📃 License

MIT License © [Eraly](https://github.com/Eraly-ml)

---

## 💬 Support

If you need help or have questions, feel free to open an [issue](https://github.com/Eraly-ml/against-toxic-bot/issues) or reach out via Telegram.
