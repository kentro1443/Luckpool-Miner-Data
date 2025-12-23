import requests
import json
import time
import os

# --- CONFIGURATION ---
WALLET = "" #ADD YOUR ADDRESS HERE
URL = f"https://luckpool.net/verus/miner/{WALLET}"

def clean_print(key, value, indent=0):
    """Helper to print keys and values cleanly without brackets/quotes."""
    spacer = " " * indent
    if value is None:
        value = "0 (or None)"
    
    
    clean_key = key.replace("Sols", " Sols").capitalize()
    
    print(f"{spacer}{clean_key:<25}: {value}")

def main():
    while True:
        try:
            
            response = requests.get(URL, timeout=10)
            
            
            os.system('cls' if os.name == 'nt' else 'clear')
            
            print(f"--- LUCKPOOL MINER STATS ---")
            
            if response.status_code == 200:
                data = response.json()
                
                
                for key, value in data.items():
                    
                    
                    if key == "workers" and isinstance(value, list):
                        print(f"\n{key.capitalize()}:")
                        if not value:
                            print("  (No workers active)")
                        for worker in value:
                            
                            print(f"  - {worker}")
                    
                    
                    else:
                        clean_print(key, value)
                        
            else:
                print(f"Error: {response.status_code}")
                
        except Exception as e:
            print(f"Error: {e}")

        
        print("\n(Updating in 60s... Press Ctrl+C to stop)")
        time.sleep(60)

if __name__ == "__main__":
    main()