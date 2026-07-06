# term-stat 📊

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![Platform: Linux/macOS](https://img.shields.io/badge/platform-Linux%20%7C%20macOS-lightgrey)](https://github.com/nexus-forg/term-stat)

![Demo](demo.png)

Красивый и легкий системный монитор для терминала. Показывает использование CPU, RAM, Disk и Network в реальном времени с поддержкой тем оформления.

## ✨ Возможности

- 🚀 **Real-time мониторинг**: Обновление данных каждые 1-2 секунды.
- 💾 **Легковесность**: Минимальное потребление ресурсов (<1% CPU).
- 🌍 **Кросс-платформенность**: Работает на Linux (Pop!_OS, Gentoo, Arch), macOS и Android (Termux).
- 📈 **Графики в ASCII**: Визуализация нагрузки прямо в консоли.

## 🚀 Установка

```bash
git clone https://github.com/yourusername/term-stat.git
cd term-stat
pip install -r requirements.txt
pip install -e .
echo 'export PATH="$HOME/.local/bin:$PATH"' >> ~/.bashrc
source ~/.bashrc

📖 Использование
Запуск монитора:

term-stat


🛠️ Разработка
Проект использует rich для красивого вывода и psutil для сбора метрик.

📝 License
MIT License. См. LICENSE


