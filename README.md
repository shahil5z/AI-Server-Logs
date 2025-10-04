# AI Server Logs 

Turn boring server/CLI logs into **detective-style stories** using AI.  
This project uses the **OpenAI API** to read raw log files and generate clear, human-readable narratives that explain what happened step by step.  

---

## Features
- Converts raw logs into **chronological stories**
- Uses **OpenAI GPT model** for smart, readable output
- Works with any `.txt` log file
- Lightweight & easy to extend  

---

## Project Structure
│── venv/ # Virtual environment
│── .env # Contains your API key
│── sample_logs.txt # Example log file
│── log_to_story.py # Main script
│── README.md # Documentation

---

## Setup Instructions

### 1. Clone / Open the Project

Navigate to your project folder:
```bash
cd "/mnt/x/Projects and Resume/AI Server Logs"
```

### 2. Create Virtual Environment

```
python3 -m venv venv
source venv/bin/activate
```
### 3. Install Dependencies

```
pip install openai python-dotenv rich
```
### 4. Add Your OpenAI API Key

Create a .env file in the project root:
```
OPENAI_API_KEY=your_api_key_here
```
---

## Usage

### 1.Put your logs into a file, e.g. sample_logs.txt

```
2025-10-04 02:03:15 ERROR Out of memory, process crashed
2025-10-04 02:05:42 WARN  User 'admin' attempted restart
2025-10-04 02:07:01 ERROR Restart failed: missing dependency
2025-10-04 02:15:22 INFO  Patch applied by user 'shahil'
2025-10-04 02:16:05 INFO  Service restarted successfully
```

### 2. Run the script:

```
python log_to_story.py
```

### 3. Output Sample Image:

-![image alt]()

---

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.