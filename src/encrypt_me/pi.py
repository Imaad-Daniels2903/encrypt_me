import requests
from pathlib import Path
import json

def digits(start: int = 0, num_digits: int = 100) -> str:
    """
    Fetches a specific range of Pi digits from the Pi.delivery API.
    
    :param start: The starting digit index (0 is the initial '3').
    :param num_digits: How many digits to fetch (max 1000 per request).
    :return: A string of the requested Pi digits.
    """
    url = "https://api.pi.delivery/v1/pi"
    params = {
        "start": start,
        "numberOfDigits": num_digits
    }
    
    pi_cache = "pi.json"
    
    if Path(pi_cache).exists() :
        with open(pi_cache, "r") as pi :
            digits = json.load(pi)
            
            if len(digits["digits"]) < num_digits : 
                    try:
                        response = requests.get(url, params=params)
                        response.raise_for_status()  # Raise an error for bad status codes (4ff or 5ff)
                        
                        data = response.json()
                        digits["digits"] = data.get("content", "")
                        
                        with open(pi_cache, "w") as file :
                            json.dump(digits, file, indent=4)
                            return "".join(digits["digits"])
                        
                    except requests.exceptions.RequestException as e:
                        print(f"Error fetching data from API: {e}")
                        return ""
                    
            else :
                    return "".join(digits["digits"][0:params["numberOfDigits"]])
                
            
    else :
        try:
            response = requests.get(url, params=params)
            response.raise_for_status()  # Raise an error for bad status codes (4ff or 5ff)
            
            data = response.json()
            content = data.get("content", "")
            
            new_data = {"digits" : list(content)}
            with open(pi_cache, "w") as file :
                json.dump(new_data, file, indent=4)
                
            return content
            
        except requests.exceptions.RequestException as e:
            print(f"Error fetching data from API: {e}")
            return ""
