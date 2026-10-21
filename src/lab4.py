import re

def process_server_logs(log_data: str) -> dict:
    """Витягує IP-адреси, час доступу та URL-адреси з логів сервера."""
    try:
        if not isinstance(log_data, str):
            raise ValueError("Вхідні дані повинні бути рядком.")
            
        # Регулярні вирази
        ip_pattern = r'\b(?:\d{1,3}\.){3}\d{1,3}\b'
        time_pattern = r'\[(.*?)\]' # Очікується формат на кшталт [10/Oct/2000:13:55:36 -0700]
        url_pattern = r'(?:GET|POST|PUT|DELETE)\s([^\s]+)\sHTTP'
        
        return {
            "IP-адреси": re.findall(ip_pattern, log_data),
            "Час доступу": re.findall(time_pattern, log_data),
            "URL-адреси": re.findall(url_pattern, log_data)
        }
    except Exception as e:
        return {"Помилка": str(e)}

def extract_vehicle_models(text: str) -> list:
    """Знаходить моделі транспортних засобів формату HY-400, AC-X1."""
    try:
        # Патерн: дві великі літери, дефіс, далі літери та/або цифри
        pattern = r'\b[A-Z]{2}-[A-Z0-9]+\b'
        return re.findall(pattern, text)
    except Exception as e:
        print(f"Сталася помилка: {e}")
        return []

sample_log = '192.168.1.1 - - [21/Sep/2026:11:42:28 +0300] "GET /index.html HTTP/1.1" 200'
sample_text = 'Наші нові транспортні моделі HY-400 та AC-X1 вже доступні, на відміну від старої XT.'

print("--- Результати Варіант 2 ---")
print("Логи:", process_server_logs(sample_log))
print("Транспортні засоби:", extract_vehicle_models(sample_text))
            print(f"Виникла помилка: {e}")

if __name__ == '__main__':
    main()
