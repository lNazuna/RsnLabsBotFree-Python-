<h1 align="center"><b>RsnChat</b> <img src="https://i.ibb.co/0J89TrT/rsn-bot-1.png" width="30" style="border-radius: 50%; margin-bottom: -5px"></h1>

<div align="center">
  <p><i>A powerful Discord AI chat bot with multiple models and personalities</i></p>
  
  ![Version](https://img.shields.io/badge/version-1.0.0-blue)
  ![Python](https://img.shields.io/badge/python-3.8%2B-blue)
  ![RsnChat](https://img.shields.io/badge/rsnchat-5.0.0b1-blue?)
  ![License](https://img.shields.io/badge/license-MIT-green)
  ![Uptime](https://img.shields.io/badge/uptime-99.9%25-brightgreen)
  ![Updated](https://img.shields.io/badge/updated-2025--04--17-orange)
</div>

## ✨ Features

- 🧠 **Advanced AI Models**: Support for multiple AI models:
  - GPT
  - GPT-4
  - Claude
  - Gemini
  - Deepseek (V3 and R1)
  - Llama
  - Grok 3 (including R1)

- 🛡️ **Permission System**: Detailed hierarchical control:
  - Administrators: Full access to all functionalities
  - Moderators: AI channel management
  - Users: Bot interaction in configured channels

- ⚙️ **Custom Channel Configuration**: Configure different AI models in different channels

## 📋 Table of Contents

- [Installation](#-installation)
- [Configuration](#-configuration)
- [Commands](#-commands)
- [Permission System](#-permission-system)
- [AI Models](#-ai-models)
- [FAQ](#-frequently-asked-questions)
- [Troubleshooting](#-troubleshooting)
- [Contributing](#-contributing)
- [License](#-license)

## 🚀 Installation

### Prerequisites

- Python 3.8+
- Discord developer account with a created bot
- RsnChat API key

```bash
# Clone the repository
git clone https://github.com/rsnlabs/rsnlabs.py-free-bot.git

# Enter the directory
cd rsnlabs.py-free-bot

# Install dependencies
pip install -r requirements.txt

# Copy the example configuration file
cp config.example.json config.json
```

## ⚙️ Configuration

Edit the config.json file with your information:

```json
{
  "token": "YOUR_DISCORD_BOT_TOKEN",
  "prefix": "!",
  "owner_ids": [123456789012345678],
  "rsnchat_key": "YOUR_RSNCHAT_API_KEY",
  "guild_only": false,
  "guild_id": 123456789012345678
}
```

### Configuration Variables

| Variable | Description |
|----------|-------------|
| token | Your Discord bot token |
| prefix | Prefix for traditional commands |
| owner_ids | Bot owner IDs (array) |
| rsnchat_key | API key for RsnChat service |
| guild_only | Sets whether slash commands are global or per server |
| guild_id | Main server ID (if guild_only is true) |

## 🔧 Commands

### AI Configuration Commands

| Command | Description | Permission |
|---------|-------------|------------|
| /setup setchannel | Configure an AI model in a channel | Moderator+ |
| /setup updatemodel | Update the model in an existing channel | Moderator+ |
| /setup removechannel | Remove AI configuration from a channel | Moderator+ |
| /setup listchannels | List all configured channels | Moderator+ |

## 🔐 Permission System

The bot has three permission levels:

### 👑 Administrator
- Full access to all bot functionalities
- Manages all channel configurations
- Requirements: Administrator permission or server owner

### 🛡️ Moderator
- Can configure and manage AI channels
- Requirements: Permission to manage channels, messages or kick members

### 👤 Regular User
- Can use the AI chat in configured channels
- No access to configuration commands

## 🧠 AI Models

| Model | Description | Speed | Quality |
|-------|-------------|-------|---------|
| GPT | Standard model with good balance | ⚡⚡⚡ | ⭐⭐⭐ |
| GPT-4 | More advanced version with better understanding | ⚡⚡ | ⭐⭐⭐⭐⭐ |
| Claude | Good for natural conversations | ⚡⚡⚡ | ⭐⭐⭐⭐ |
| Gemini | Google's model with good contextual understanding | ⚡⚡⚡ | ⭐⭐⭐⭐ |
| Deepseek V3 | Advanced model for complex topics | ⚡⚡ | ⭐⭐⭐⭐ |
| Deepseek R1 | Optimized version for quick responses | ⚡⚡⚡⚡ | ⭐⭐⭐ |
| Llama | Open-source model with good performance | ⚡⚡⚡ | ⭐⭐⭐ |
| Grok 3 | Advanced conversational model | ⚡⚡ | ⭐⭐⭐⭐ |
| Grok 3 R1 | Refined version of Grok 3 | ⚡⚡ | ⭐⭐⭐⭐⭐ |

## ❓ Frequently Asked Questions

**Q: How do I get an RsnChat API key?**  
A: Visit rsnchat.com to register and get your API key.

**Q: Can the bot be used in multiple servers?**  
A: Yes, just set the guild_only option to false in the config.json file.

**Q: Can I change the AI model after configuring a channel?**  
A: Yes, use the /setup updatemodel command to update the model of an already configured channel.

**Q: How many channels can I configure with the bot?**  
A: There is no technical limit to the number of channels that can be configured.

## 🔧 Troubleshooting

### Bot does not respond to commands
- Check if the bot has the necessary permissions in Discord
- Confirm that the bot token is correct in config.json
- Check the logs for command synchronization errors

### RsnChat API errors
- Check if your API key is valid
- Confirm that you have enough credits in your RsnChat account
- Check if the RsnChat service is online

### Bot does not respond to messages
- Confirm that the channel was configured using /setup setchannel
- Check if the bot has permissions to send messages in that channel
- Check the logs for specific API errors

## 🤝 Contributing

Contributions are welcome! If you want to contribute:

1. Fork the project
2. Create a branch for your feature (git checkout -b feature/new-functionality)
3. Commit your changes (git commit -m 'Adding new functionality')
4. Push to the branch (git push origin feature/new-functionality)
5. Open a Pull Request

## 📜 License

This project is licensed under the MIT license. See the LICENSE file for more details.

<div align="center">
  <p>Developed with ❤️ by lNazuna (BOT) and Rstacx (API) </p>
  <p>
    <a href="https://api.rnilaweera.lk/discord">Discord</a> •
    <a href="https://github.com/lNazuna">GitHub (Nazuna)</a> •
    <a href="https://github.com/Rstacx">GitHub (Rstacx)</a> •
    <a href="https://github.com/rsnlabs/rsnchat-py">Rsnchat-py</a>
  </p>
  <p>Last updated: 2025-04-17</p>
</div>