from flask import Flask, request, jsonify
import os
from functools import reduce
import math
import requests

app = Flask(__name__)

# ==================== CONFIGURATION ====================
# IMPORTANT: Replace with your actual Chitkara email
OFFICIAL_EMAIL = "your.email@chitkara.edu.in"

# Set this as environment variable: export GEMINI_API_KEY='your_key_here'
GEMINI_API_KEY = os.environ.get('GEMINI_API_KEY', '')

# ==================== HELPER FUNCTIONS ====================

def validate_request_body(data):
    """Validate that exactly one key is present"""
    if not data:
        return False, "Request body is empty"
    
    valid_keys = {'fibonacci', 'prime', 'lcm', 'hcf', 'AI'}
    request_keys = set(data.keys())
    
    if len(request_keys) != 1:
        return False, "Request must contain exactly one key"
    
    if not request_keys.issubset(valid_keys):
        return False, f"Invalid key. Must be one of: {valid_keys}"
    
    return True, None


def generate_fibonacci(n):
    """Generate Fibonacci series up to n terms"""
    if not isinstance(n, int):
        raise ValueError("Fibonacci input must be an integer")
    if n < 0:
        raise ValueError("Fibonacci input must be non-negative")
    if n == 0:
        return []
    if n == 1:
        return [0]
    
    fib_series = [0, 1]
    for i in range(2, n):
        fib_series.append(fib_series[-1] + fib_series[-2])
    
    return fib_series[:n]


def is_prime(num):
    """Check if a number is prime"""
    if num < 2:
        return False
    if num == 2:
        return True
    if num % 2 == 0:
        return False
    for i in range(3, int(math.sqrt(num)) + 1, 2):
        if num % i == 0:
            return False
    return True


def filter_primes(numbers):
    """Filter prime numbers from an array"""
    if not isinstance(numbers, list):
        raise ValueError("Prime input must be an array")
    if not numbers:
        raise ValueError("Prime array cannot be empty")
    if not all(isinstance(x, int) for x in numbers):
        raise ValueError("All elements must be integers")
    
    return [num for num in numbers if is_prime(num)]


def calculate_gcd(a, b):
    """Calculate GCD of two numbers"""
    while b:
        a, b = b, a % b
    return abs(a)


def calculate_hcf(numbers):
    """Calculate HCF (GCD) of an array of numbers"""
    if not isinstance(numbers, list):
        raise ValueError("HCF input must be an array")
    if not numbers:
        raise ValueError("HCF array cannot be empty")
    if not all(isinstance(x, int) for x in numbers):
        raise ValueError("All elements must be integers")
    if any(x == 0 for x in numbers):
        raise ValueError("HCF array cannot contain zero")
    
    return reduce(calculate_gcd, numbers)


def calculate_lcm_two(a, b):
    """Calculate LCM of two numbers"""
    return abs(a * b) // calculate_gcd(a, b)


def calculate_lcm(numbers):
    """Calculate LCM of an array of numbers"""
    if not isinstance(numbers, list):
        raise ValueError("LCM input must be an array")
    if not numbers:
        raise ValueError("LCM array cannot be empty")
    if not all(isinstance(x, int) for x in numbers):
        raise ValueError("All elements must be integers")
    if any(x == 0 for x in numbers):
        raise ValueError("LCM array cannot contain zero")
    
    return reduce(calculate_lcm_two, numbers)


def get_ai_response(question):
    """Get AI response using Google Gemini API"""
    if not isinstance(question, str):
        raise ValueError("AI input must be a string")
    if not question.strip():
        raise ValueError("AI question cannot be empty")
    
    if not GEMINI_API_KEY:
        raise ValueError("GEMINI_API_KEY not configured")
    
    try:
        # Google Gemini API endpoint
        url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-pro:generateContent?key={GEMINI_API_KEY}"
        
        headers = {'Content-Type': 'application/json'}
        
        payload = {
            "contents": [{
                "parts": [{
                    "text": f"{question}\n\nProvide only a single word answer, nothing else."
                }]
            }],
            "generationConfig": {
                "temperature": 0.1,
                "maxOutputTokens": 10
            }
        }
        
        response = requests.post(url, json=payload, headers=headers, timeout=10)
        
        if response.status_code == 200:
            result = response.json()
            answer = result['candidates'][0]['content']['parts'][0]['text'].strip()
            # Extract first word
            first_word = answer.split()[0].strip('.,!?;:')
            return first_word
        else:
            raise ValueError(f"AI API error: {response.status_code}")
            
    except requests.exceptions.Timeout:
        raise ValueError("AI API timeout")
    except requests.exceptions.RequestException as e:
        raise ValueError(f"AI API connection error: {str(e)}")
    except (KeyError, IndexError) as e:
        raise ValueError(f"AI API response parsing error: {str(e)}")


# ==================== ROUTES ====================

@app.route('/health', methods=['GET'])
def health_check():
    """Health check endpoint"""
    return jsonify({
        "is_success": True,
        "official_email": OFFICIAL_EMAIL
    }), 200


@app.route('/bfhl', methods=['POST'])
def process_request():
    """Main POST endpoint for processing requests"""
    try:
        # Get JSON data
        data = request.get_json(force=True, silent=True)
        
        if data is None:
            return jsonify({
                "is_success": False,
                "error": "Invalid JSON or empty request body"
            }), 400
        
        # Validate request structure
        is_valid, error_msg = validate_request_body(data)
        if not is_valid:
            return jsonify({
                "is_success": False,
                "error": error_msg
            }), 400
        
        # Process based on key
        result_data = None
        
        if 'fibonacci' in data:
            result_data = generate_fibonacci(data['fibonacci'])
        
        elif 'prime' in data:
            result_data = filter_primes(data['prime'])
        
        elif 'lcm' in data:
            result_data = calculate_lcm(data['lcm'])
        
        elif 'hcf' in data:
            result_data = calculate_hcf(data['hcf'])
        
        elif 'AI' in data:
            result_data = get_ai_response(data['AI'])
        
        # Return success response
        return jsonify({
            "is_success": True,
            "official_email": OFFICIAL_EMAIL,
            "data": result_data
        }), 200
    
    except ValueError as ve:
        return jsonify({
            "is_success": False,
            "error": str(ve)
        }), 400
    
    except Exception as e:
        return jsonify({
            "is_success": False,
            "error": f"Internal server error: {str(e)}"
        }), 500


@app.errorhandler(404)
def not_found(error):
    """Handle 404 errors"""
    return jsonify({
        "is_success": False,
        "error": "Endpoint not found"
    }), 404


@app.errorhandler(405)
def method_not_allowed(error):
    """Handle 405 errors"""
    return jsonify({
        "is_success": False,
        "error": "Method not allowed"
    }), 405


@app.errorhandler(500)
def internal_error(error):
    """Handle 500 errors"""
    return jsonify({
        "is_success": False,
        "error": "Internal server error"
    }), 500


# ==================== MAIN ====================

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False)
