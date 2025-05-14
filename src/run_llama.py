import requests
import subprocess
import time

def check_ollama_running():
    try:
        response = requests.get("http://localhost:11434/api/tags")
        return response.status_code == 200
    except requests.exceptions.ConnectionError:
        return False

def start_ollama():
    if check_ollama_running():
        print("Ollama가 이미 실행 중입니다.")
        return
        
    try:
        print("Ollama를 시작합니다...")
        subprocess.Popen(["ollama", "run", "llama3.2"], 
                        stdout=subprocess.PIPE, 
                        stderr=subprocess.PIPE)
        time.sleep(5)
        print("Ollama가 성공적으로 시작되었습니다.")
    except Exception as e:
        print(f"Ollama 시작 중 오류 발생: {e}")
        exit(1)

if not check_ollama_running():
    print("Ollama가 실행되지 않았습니다. 시작합니다...")
    start_ollama()
