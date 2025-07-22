
# 💬 Multi-Client TCP Chat Application — Department-Based

![Python](https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python)
![TCP Socket](https://img.shields.io/badge/Socket-TCP-brightgreen?style=for-the-badge&logo=socketdotio)
![Multi-Threaded](https://img.shields.io/badge/Threads-Multi--Client-informational?style=for-the-badge&logo=codeforces)
![Platform](https://img.shields.io/badge/Platform-Cross--Platform-lightgrey?style=for-the-badge)
![License](https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Completed-success?style=for-the-badge)

---

## 🧠 Project Overview

The **Multi-Client TCP Chat App** is a lightweight, real-time terminal chat system written in Python using sockets and threads.

This app simulates an internal messaging system between employees of different departments (e.g., HR, Sales, Tech). Each message includes the **sender’s department and name**, and all messages are logged with timestamps.

---

## 🛠️ Features

### 🖥️ Server (`chat_server.py`)
- Accepts **multiple client connections** using threads
- Broadcasts messages to **all users** with department-name prefix
- Stores all messages in `chat_log.txt`
- Handles disconnections gracefully
- Supports custom `/list` command to show online users

### 💻 Client (`chat_client.py`)
- Prompts for **Department** and **Name** at start
- Real-time **sending/receiving** of messages using threading
- Displays messages with timestamps and sender info
- `/list` command displays all connected clients from the server

---

## 📁 Project Structure

```

📦 tcp-chat-app
┣ 📄 chat\_server.py       # Server-side logic (multi-threaded)
┣ 📄 chat\_client.py       # Client-side terminal chat
┗ 📄 chat\_log.txt         # Auto-generated chat logs

````

---

## 🚀 Getting Started

### ▶️ 1. Start the Server

```bash
python chat_server.py
````

✅ The server listens on `127.0.0.1:5555` (you can change this inside the script).

---

### 🧑‍💻 2. Start the Clients (Run in separate terminals)

```bash
python chat_client.py
```

🟨 On launch, enter:

* Department: e.g., `HR`
* Name: e.g., `Alice`

Type your messages and chat with others instantly.

---

## 💬 Sample Chat Output

```
[HR - Alice] Good morning, team!
[Sales - Bob] Morning Alice!
```

Type `/list` at any time to see all currently connected users.

---

## 📝 Chat Logging

Every message is saved automatically to `chat_log.txt` like:

```
[2025-07-22 13:30:05] [Sales - Alice] Hello everyone!
```

🔐 Logs help maintain audit trails or review past conversations.

---

## 📚 Educational Value

This project is great for learning:

| Concept                   | Demonstrated ✅ |
| ------------------------- | -------------- |
| Python `socket` module    | ✅              |
| Multi-threading           | ✅              |
| Client-server networking  | ✅              |
| Logging with timestamps   | ✅              |
| Terminal-based UI         | ✅              |
| Command parsing (`/list`) | ✅              |

---

## 🧩 Custom Commands

| Command  | Description                       |
| -------- | --------------------------------- |
| `/list`  | View list of all connected users  |
| `Ctrl+C` | Disconnect from server gracefully |

---

## 🔧 Requirements

* ✅ Python 3.6 or above
* ✅ No external libraries needed

Run it out-of-the-box!

```
Server running at 127.0.0.1:5555...
Client connected: HR - Alice
Client connected: Sales - Bob
[Sales - Bob]: Hello everyone!
```

</details>

---

## 🧑‍💻 Author

**Saad Khan**
📧 [saad@example.com](mailto:saad0652004@gmail.com)
🌐 [GitHub: @saadoxyz](https://github.com/saadoxyz)

---
```
