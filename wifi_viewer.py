import subprocess

def get_wifi_profiles():
    profiles = subprocess.check_output("netsh wlan show profiles", shell=True).decode('utf-8', errors='ignore')
    profile_names = [line.split(":")[1].strip() for line in profiles.split("\n") if "All User Profile" in line]
    return profile_names

def get_wifi_password(profile):
    result = subprocess.check_output(f'netsh wlan show profile "{profile}" key=clear', shell=True).decode('utf-8', errors='ignore')
    for line in result.split("\n"):
        if "Key Content" in line:
            return line.split(":")[1].strip()
    return None

def main():
    print("\n" + "="*40)
    print(" 📶 WiFi Password Viewer")
    print("="*40 + "\n")
    
    profiles = get_wifi_profiles()
    
    if not profiles:
        print("[-] No WiFi profiles found!")
        return
    
    for i, profile in enumerate(profiles, 1):
        print(f"[{i}] {profile}")
    
    try:
        choice = int(input("\nChoose WiFi number: "))
        selected = profiles[choice - 1]
        password = get_wifi_password(selected)
        
        print("\n" + "-"*40)
        print(f"WiFi Name : {selected}")
        print(f"Password : {password if password else 'No Password / Open Network'}")
        print("-"*40 + "\n")
        
    except (ValueError, IndexError):
        print("[-] Invalid choice!")

if __name__ == "__main__":
    main()
