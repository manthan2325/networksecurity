"""
Helper script to get your current public IP address for MongoDB Atlas whitelisting
"""
import urllib.request
import json

def get_public_ip():
    """Get your current public IP address"""
    try:
        # Using multiple services for reliability
        services = [
            'https://api.ipify.org?format=json',
            'https://ifconfig.me/ip',
            'https://icanhazip.com'
        ]
        
        for service in services:
            try:
                if 'json' in service:
                    response = urllib.request.urlopen(service, timeout=5)
                    data = json.loads(response.read().decode())
                    ip = data.get('ip', '')
                else:
                    response = urllib.request.urlopen(service, timeout=5)
                    ip = response.read().decode().strip()
                
                if ip:
                    print(f"✓ Your public IP address is: {ip}")
                    print(f"\nTo whitelist this IP in MongoDB Atlas:")
                    print(f"1. Go to https://cloud.mongodb.com/")
                    print(f"2. Navigate to: Network Access → Add IP Address")
                    print(f"3. Add IP: {ip}")
                    print(f"4. Or use '0.0.0.0/0' to allow all IPs (less secure, for testing only)")
                    return ip
            except Exception as e:
                continue
        
        print("✗ Could not determine your public IP address")
        print("Please manually check your IP at: https://whatismyipaddress.com/")
        return None
    except Exception as e:
        print(f"Error getting IP address: {e}")
        return None

if __name__ == "__main__":
    get_public_ip()

