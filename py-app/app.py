from flask import Flask
import numpy as np
import requests

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello from Python App in Docker!"

@app.route('/random')
def random_number():
    """Генерирует случайное число с помощью NumPy"""
    try:
        number = np.random.randint(1, 101)
        return f"Random number: {number}"
    except Exception as e:
        return f"Error generating random number: {str(e)}", 500

@app.route('/ip')
def get_ip():
    """Получает ваш IP-адрес с помощью requests"""
    try:
        response = requests.get("https://api64.ipify.org?format=json")
        response.raise_for_status()  # Проверяем, что запрос успешен
        ip_data = response.json()
        return f"Your public IP is: {ip_data['ip']}"  # Убраны лишние обратные слэши
    except requests.exceptions.RequestException as e:
        return f"Error fetching IP: {str(e)}", 500
    except Exception as e:
        return f"Unexpected error: {str(e)}", 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)