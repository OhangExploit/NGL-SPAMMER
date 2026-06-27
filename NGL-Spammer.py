import requests
import random
import time
import os
import sys
import json
from datetime import datetime
from concurrent.futures import ThreadPoolExecutor, as_completed

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    CYAN = '\033[96m'
    MAGENTA = '\033[95m'

class NGLSpammer:
    
    def __init__(self):
        self.banner()
        self.get_user_input()
        self.load_messages()
        self.start_spamming()
    
    def banner(self):
        os.system('clear' if os.name == 'posix' else 'cls')
        print(f"""
{bcolors.CYAN}
         TOOLS – NGL SPAMMER
         AUTHOR : OhangExpoilt
{bcolors.ENDC}
        """)
    
    def get_user_input(self):
        print(f"{bcolors.WARNING}[+] Enter target username:{bcolors.ENDC}")
        self.username = input(f"{bcolors.OKGREEN}[?] NGL Username: {bcolors.ENDC}").strip()
        
        if not self.username:
            print(f"{bcolors.FAIL}[!] Username cannot be empty!{bcolors.ENDC}")
            sys.exit(1)
        
        print(f"\n{bcolors.WARNING}[+] Number of messages to send:{bcolors.ENDC}")
        max_input = input(f"{bcolors.OKGREEN}[?] Number of messages (default 50): {bcolors.ENDC}").strip()
        self.max_messages = int(max_input) if max_input.isdigit() else 50
        
        print(f"\n{bcolors.WARNING}[+] Message file:{bcolors.ENDC}")
        print(f"{bcolors.OKBLUE}   - Default: messages.txt{bcolors.ENDC}")
        print(f"{bcolors.OKBLUE}   - Custom: [path/file.txt]{bcolors.ENDC}")
        file_input = input(f"{bcolors.OKGREEN}[?] Message file (default messages.txt): {bcolors.ENDC}").strip()
        self.messages_file = file_input if file_input else "messages.txt"
        
        print(f"\n{bcolors.WARNING}[+] Delay between messages (seconds):{bcolors.ENDC}")
        print(f"{bcolors.OKBLUE}   - Default: 5-15 Random seconds{bcolors.ENDC}")
        delay_input = input(f"{bcolors.OKGREEN}[?] Minimum delay (default 5): {bcolors.ENDC}").strip()
        self.min_delay = int(delay_input) if delay_input.isdigit() else 5
        delay_input2 = input(f"{bcolors.OKGREEN}[?] Maximum delay (default 15): {bcolors.ENDC}").strip()
        self.max_delay = int(delay_input2) if delay_input2.isdigit() else 15
        
        print(f"\n{bcolors.WARNING}[+] Sending mode:{bcolors.ENDC}")
        print(f"{bcolors.OKBLUE}   1. Sequential (1 thread){bcolors.ENDC}")
        print(f"{bcolors.OKBLUE}   2. Parallel (multi thread){bcolors.ENDC}")
        mode_input = input(f"{bcolors.OKGREEN}[?] Select a mode (1/2): {bcolors.ENDC}").strip()
        self.mode = mode_input if mode_input in ['1', '2'] else '1'
        
        if self.mode == '2':
            thread_input = input(f"{bcolors.OKGREEN}[?] Number of threads(default 5): {bcolors.ENDC}").strip()
            self.threads = int(thread_input) if thread_input.isdigit() else 5
        
        print(f"\n{bcolors.OKBLUE}[+] Target: {self.username}{bcolors.ENDC}")
        print(f"{bcolors.OKBLUE}[+] Max messages: {self.max_messages}{bcolors.ENDC}")
        print(f"{bcolors.OKBLUE}[+] Messages file: {self.messages_file}{bcolors.ENDC}")
        print(f"{bcolors.OKBLUE}[+] Delay: {self.min_delay}-{self.max_delay}s{bcolors.ENDC}")
        print(f"{bcolors.OKBLUE}[+] Mode: {'Parallel' if self.mode == '2' else 'Sequential'}{bcolors.ENDC}\n")
    
    def load_messages(self):
        try:
            if os.path.exists(self.messages_file):
                with open(self.messages_file, 'r', encoding='utf-8') as f:
                    self.messages = [line.strip() for line in f if line.strip()]
                print(f"{bcolors.OKGREEN}[+] Loaded {len(self.messages)} messages from {self.messages_file}{bcolors.ENDC}")
            else:
                print(f"{bcolors.WARNING}[!] File {self.messages_file} Not found!{bcolors.ENDC}")
                print(f"{bcolors.WARNING}[+] Creating messages.txt file with default messages{bcolors.ENDC}")
                self.create_default_messages()
        except Exception as e:
            print(f"{bcolors.FAIL}[!] Error loading messages: {e}{bcolors.ENDC}")
            sys.exit(1)
        
        if not self.messages:
            print(f"{bcolors.FAIL}[!] No messages in{self.messages_file}{bcolors.ENDC}")
            sys.exit(1)
    
    def create_default_messages(self):
        default_messages = [
            "Hi there!",
            "You're amazing!",
            "Keep up the good work!",
            "I love your content!",
            "You're so inspiring!",
            "Have a great day!",
            "You deserve the best!",
            "Stay blessed!",
            "You're a star!",
            "Keep shining!",
            "Sending you lots of love!",
            "You're beautiful inside and out!",
            "Your energy is contagious!",
            "You make the world a better place!",
            "I'm your biggest fan!",
            "You're doing great!",
            "Don't ever give up!",
            "You're so talented!",
            "Your smile is infectious!",
            "You're one of a kind!",
            "I appreciate you!",
            "You're so strong!",
            "Keep being awesome!",
            "You're a legend!",
            "You're the best!"
        ]
        
        try:
            with open("messages.txt", 'w', encoding='utf-8') as f:
                for msg in default_messages:
                    f.write(msg + '\n')
            self.messages = default_messages
            print(f"{bcolors.OKGREEN}[+] Created messages.txt with {len(default_messages)} default messages{bcolors.ENDC}")
        except Exception as e:
            print(f"{bcolors.FAIL}[!] Error creating messages.txt: {e}{bcolors.ENDC}")
            sys.exit(1)
    
    def random_delay(self):
        delay = random.randint(self.min_delay, self.max_delay)
        time.sleep(delay)
        return delay
    
    def generate_device_id(self):
        return ''.join(random.choices('0123456789abcdef', k=42))
    
    def send_message(self, username, message):
        device_id = self.generate_device_id()
        url = "https://ngl.link/api/submit"
        
        headers = {
            "User-Agent": f"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.{random.randint(0,20)}) Gecko/20100101 Firefox/109.0",
            "Accept": "*/*",
            "Accept-Language": "en-US,en;q=0.5",
            "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
            "X-Requested-With": "XMLHttpRequest",
            "Sec-Fetch-Dest": "empty",
            "Sec-Fetch-Mode": "cors",
            "Sec-Fetch-Site": "same-origin",
            "Referer": f"https://ngl.link/{username}",
            "Origin": "https://ngl.link"
        }
        
        data = {
            "username": username,
            "question": message,
            "deviceId": device_id,
            "gameSlug": "",
            "referrer": ""
        }
        
        try:
            response = requests.post(url, data=data, headers=headers, timeout=10)
            timestamp = datetime.now().strftime("%H:%M:%S")
            
            if response.status_code == 200:
                print(f"{bcolors.OKGREEN}[{timestamp}]Message sent: {message[:30]}...{bcolors.ENDC}")
                return True, message
            else:
                print(f"{bcolors.FAIL}[{timestamp}] Failed. Status: {response.status_code}{bcolors.ENDC}")
                return False, message
                
        except requests.exceptions.Timeout:
            print(f"{bcolors.FAIL}[!] Timeout error{bcolors.ENDC}")
            return False, message
        except requests.exceptions.ConnectionError:
            print(f"{bcolors.FAIL}[!] Connection error{bcolors.ENDC}")
            return False, message
        except Exception as e:
            print(f"{bcolors.FAIL}[!] Error: {e}{bcolors.ENDC}")
            return False, message
    
    def worker(self, username, message):
        return self.send_message(username, message)
    
    def start_spamming(self):
        print(f"{bcolors.WARNING}[+] Starting spam to @{self.username}...{bcolors.ENDC}")
        print(f"{bcolors.WARNING}[+] Sending {self.max_messages} messages...{bcolors.ENDC}\n")
        
        success_count = 0
        fail_count = 0
        
        if self.mode == '1':
            for i in range(self.max_messages):
                msg = random.choice(self.messages)
                success, _ = self.send_message(self.username, msg)
                
                if success:
                    success_count += 1
                else:
                    fail_count += 1
                
                progress = ((i + 1) / self.max_messages) * 100
                print(f"{bcolors.OKBLUE}[+] Progress: {i+1}/{self.max_messages} ({progress:.1f}%) | Success: {success_count} | Fail: {fail_count}{bcolors.ENDC}")
                
                if i < self.max_messages - 1:
                    delay = self.random_delay()
                    print(f"{bcolors.WARNING}[+] Waiting {delay}s...{bcolors.ENDC}")
                
                if (i + 1) % 5 == 0 and i < self.max_messages - 1:
                    break_time = random.randint(15, 30)
                    print(f"{bcolors.WARNING}[+] Taking a short human-like break ({break_time}s)...{bcolors.ENDC}")
                    time.sleep(break_time)
        
        else:
            with ThreadPoolExecutor(max_workers=self.threads) as executor:
                futures = []
                messages_to_send = [random.choice(self.messages) for _ in range(self.max_messages)]
                
                for i, msg in enumerate(messages_to_send):
                    futures.append(executor.submit(self.worker, self.username, msg))
                    
                    if (i + 1) % 10 == 0:
                        print(f"{bcolors.OKBLUE}[+] Submitted {i+1}/{self.max_messages} messages...{bcolors.ENDC}")
                    
                    if i < self.max_messages - 1:
                        delay = random.randint(1, 3)
                        time.sleep(delay)
                
                for i, future in enumerate(as_completed(futures)):
                    success, msg = future.result()
                    if success:
                        success_count += 1
                    else:
                        fail_count += 1
                    
                    progress = ((i + 1) / self.max_messages) * 100
                    if (i + 1) % 5 == 0:
                        print(f"{bcolors.OKBLUE}[+] Progress: {i+1}/{self.max_messages} ({progress:.1f}%) | Success: {success_count} | Fail: {fail_count}{bcolors.ENDC}")
        
        print(f"\n{bcolors.OKGREEN}{'='*60}{bcolors.ENDC}")
        print(f"{bcolors.OKGREEN}[+] SPAM COMPLETED!{bcolors.ENDC}")
        print(f"{bcolors.OKGREEN}[+] Total messages sent: {self.max_messages}{bcolors.ENDC}")
        print(f"{bcolors.OKGREEN}[+] Success: {success_count}{bcolors.ENDC}")
        print(f"{bcolors.OKGREEN}[+] Failed: {fail_count}{bcolors.ENDC}")
        print(f"{bcolors.OKGREEN}[+] Success rate: {(success_count/self.max_messages)*100:.1f}%{bcolors.ENDC}")
        print(f"{bcolors.OKGREEN}{'='*60}{bcolors.ENDC}")

if __name__ == "__main__":
    try:
        spammer = NGLSpammer()
    except KeyboardInterrupt:
        print(f"\n{bcolors.WARNING}[!] User interrupted!{bcolors.ENDC}")
        sys.exit(0)
    except Exception as e:
        print(f"{bcolors.FAIL}[!] Error: {e}{bcolors.ENDC}")
        sys.exit(1)