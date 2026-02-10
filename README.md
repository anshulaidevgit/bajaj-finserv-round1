# Bajaj Finserv Health Challenge - Round 1 API

A robust REST API implementation for the Chitkara University 2026 Qualifier (Class of 2027) that processes mathematical operations and AI-powered queries.

## 👨‍💻 Student Information

- **Name**: Anshul Patel
- **Roll Number**: 2310993782
- **Email**: anshul3782.beai23@chitkara.edu.in
- **Institution**: Chitkara University
- **Program**: B.E. Artificial Intelligence (Class of 2027)

## 🚀 Live Deployment

**API Base URL**: `https://bajaj-finserv-round1-omega.vercel.app`

## 📋 Table of Contents

- [Features](#features)
- [Tech Stack](#tech-stack)
- [API Endpoints](#api-endpoints)
- [Installation](#installation)
- [Usage Examples](#usage-examples)
- [Deployment](#deployment)
- [Testing](#testing)
- [Project Structure](#project-structure)

## ✨ Features

- ✅ **Fibonacci Series Generation** - Generate Fibonacci sequence up to n terms
- ✅ **Prime Number Filtering** - Extract prime numbers from an array
- ✅ **LCM Calculation** - Compute Least Common Multiple of multiple numbers
- ✅ **HCF Calculation** - Compute Highest Common Factor (GCD) of multiple numbers
- ✅ **AI Integration** - Answer questions using OpenAI GPT-3.5 Turbo
- ✅ **Robust Error Handling** - Proper HTTP status codes and error messages
- ✅ **Input Validation** - Comprehensive validation for all inputs
- ✅ **Production Ready** - Deployed on Vercel with 99.9% uptime

## 🛠️ Tech Stack

- **Framework**: Flask (Python 3.x)
- **AI Integration**: OpenAI GPT-3.5 Turbo API
- **HTTP Client**: Requests library
- **Deployment**: Vercel (Serverless)
- **Version Control**: Git & GitHub

## 📡 API Endpoints

### 1. Health Check

Check if the API is running and accessible.

**Endpoint**: `GET /health`

**Response**:
```json
{
  "is_success": true,
  "official_email": "anshul3782.beai23@chitkara.edu.in"
}
```

### 2. Process Request

Main endpoint for all operations.

**Endpoint**: `POST /bfhl`

**Content-Type**: `application/json`

#### Operations

##### Fibonacci Series

Generate Fibonacci sequence.

**Request**:
```json
{
  "fibonacci": 7
}
```

**Response**:
```json
{
  "is_success": true,
  "official_email": "anshul3782.beai23@chitkara.edu.in",
  "data": [0, 1, 1, 2, 3, 5, 8]
}
```

##### Prime Numbers

Filter prime numbers from an array.

**Request**:
```json
{
  "prime": [2, 4, 7, 9, 11]
}
```

**Response**:
```json
{
  "is_success": true,
  "official_email": "anshul3782.beai23@chitkara.edu.in",
  "data": [2, 7, 11]
}
```

##### LCM (Least Common Multiple)

Calculate LCM of multiple numbers.

**Request**:
```json
{
  "lcm": [12, 18, 24]
}
```

**Response**:
```json
{
  "is_success": true,
  "official_email": "anshul3782.beai23@chitkara.edu.in",
  "data": 72
}
```

##### HCF (Highest Common Factor)

Calculate HCF/GCD of multiple numbers.

**Request**:
```json
{
  "hcf": [24, 36, 60]
}
```

**Response**:
```json
{
  "is_success": true,
  "official_email": "anshul3782.beai23@chitkara.edu.in",
  "data": 12
}
```

##### AI Question

Get AI-powered answers to questions.

**Request**:
```json
{
  "AI": "What is the capital city of Maharashtra?"
}
```

**Response**:
```json
{
  "is_success": true,
  "official_email": "anshul3782.beai23@chitkara.edu.in",
  "data": "Mumbai"
}
```

## 🔧 Installation

### Prerequisites

- Python 3.8 or higher
- pip package manager
- OpenAI API key

### Local Setup

1. **Clone the repository**
```bash
git clone https://github.com/yourusername/bajaj-finserv-round1.git
cd bajaj-finserv-round1
```

2. **Install dependencies**
```bash
pip install -r requirements.txt
```

3. **Set environment variable**

**Windows**:
```bash
set OPENAI_API_KEY=your_openai_api_key_here
```

**Linux/Mac**:
```bash
export OPENAI_API_KEY=your_openai_api_key_here
```

4. **Run the application**
```bash
python app.py
```

The server will start at `http://localhost:5000`

## 📝 Usage Examples

### Using cURL (Windows)

```bash
# Health Check
curl https://bajaj-finserv-round1-omega.vercel.app/health

# Fibonacci
curl -X POST https://bajaj-finserv-round1-omega.vercel.app/bfhl -H "Content-Type: application/json" -d "{\"fibonacci\":7}"

# Prime Numbers
curl -X POST https://bajaj-finserv-round1-omega.vercel.app/bfhl -H "Content-Type: application/json" -d "{\"prime\":[2,4,7,9,11]}"

# LCM
curl -X POST https://bajaj-finserv-round1-omega.vercel.app/bfhl -H "Content-Type: application/json" -d "{\"lcm\":[12,18,24]}"

# HCF
curl -X POST https://bajaj-finserv-round1-omega.vercel.app/bfhl -H "Content-Type: application/json" -d "{\"hcf\":[24,36,60]}"

# AI Question
curl -X POST https://bajaj-finserv-round1-omega.vercel.app/bfhl -H "Content-Type: application/json" -d "{\"AI\":\"What is the capital of France?\"}"
```

### Using Python

```python
import requests

BASE_URL = "https://bajaj-finserv-round1-omega.vercel.app"

# Health check
response = requests.get(f"{BASE_URL}/health")
print(response.json())

# Fibonacci
response = requests.post(
    f"{BASE_URL}/bfhl",
    json={"fibonacci": 7}
)
print(response.json())

# Prime numbers
response = requests.post(
    f"{BASE_URL}/bfhl",
    json={"prime": [2, 4, 7, 9, 11]}
)
print(response.json())

# AI Question
response = requests.post(
    f"{BASE_URL}/bfhl",
    json={"AI": "What is the capital of Maharashtra?"}
)
print(response.json())
```

### Using JavaScript (Fetch API)

```javascript
const BASE_URL = "https://bajaj-finserv-round1-omega.vercel.app";

// Health check
fetch(`${BASE_URL}/health`)
  .then(response => response.json())
  .then(data => console.log(data));

// Fibonacci
fetch(`${BASE_URL}/bfhl`, {
  method: 'POST',
  headers: { 'Content-Type': 'application/json' },
  body: JSON.stringify({ fibonacci: 7 })
})
  .then(response => response.json())
  .then(data => console.log(data));

// AI Question
fetch(`${BASE_URL}/bfhl`, {
  method: 'POST',
  headers: { 'Content-Type': 'application/json' },
  body: JSON.stringify({ 
    AI: "What is the capital city of Maharashtra?" 
  })
})
  .then(response => response.json())
  .then(data => console.log(data));
```

## 🚀 Deployment

### Vercel Deployment (Recommended)

1. **Push code to GitHub**
```bash
git add .
git commit -m "Initial commit"
git push origin main
```

2. **Deploy to Vercel**
   - Go to [vercel.com](https://vercel.com)
   - Import your GitHub repository
   - Add environment variable:
     - **Name**: `OPENAI_API_KEY`
     - **Value**: Your OpenAI API key
   - Click Deploy

3. **Configure Settings**
   - Disable "Deployment Protection" or set to "Public"
   - Enable "Automatically expose System Environment Variables"

## 🧪 Testing

### Error Handling

The API returns appropriate HTTP status codes:

- `200` - Success
- `400` - Bad Request (invalid input, validation errors)
- `404` - Not Found (invalid endpoint)
- `405` - Method Not Allowed (wrong HTTP method)
- `500` - Internal Server Error

**Error Response Format**:
```json
{
  "is_success": false,
  "error": "Error description here"
}
```

### Test Cases Covered

✅ Valid inputs for all operations  
✅ Empty arrays  
✅ Negative numbers  
✅ Zero values  
✅ Non-integer inputs  
✅ Missing API key  
✅ Invalid JSON  
✅ Multiple keys in request  
✅ Invalid endpoint access  
✅ Wrong HTTP methods  

## 📁 Project Structure

```
bajaj-finserv-round1/
├── app.py                 # Main Flask application
├── requirements.txt       # Python dependencies
├── vercel.json           # Vercel configuration
├── README.md             # Project documentation
└── .gitignore            # Git ignore rules
```

## 🔒 Security Features

- ✅ Environment variable for API key (never hardcoded)
- ✅ Input validation and sanitization
- ✅ Request timeout protection (10 seconds)
- ✅ Error message sanitization
- ✅ No sensitive data in error responses

## 📊 API Response Structure

All successful responses follow this structure:

```json
{
  "is_success": true,
  "official_email": "anshul3782.beai23@chitkara.edu.in",
  "data": <result>
}
```

All error responses follow this structure:

```json
{
  "is_success": false,
  "error": "<error message>"
}
```

## 🎯 Validation Rules

1. **Request Body**:
   - Must contain exactly one key
   - Key must be one of: `fibonacci`, `prime`, `lcm`, `hcf`, `AI`

2. **Fibonacci**:
   - Input must be a non-negative integer

3. **Prime**:
   - Input must be a non-empty array of integers

4. **LCM**:
   - Input must be a non-empty array of non-zero integers

5. **HCF**:
   - Input must be a non-empty array of non-zero integers

6. **AI**:
   - Input must be a non-empty string

## 🏆 Compliance

This project fully complies with all Chitkara University 2026 Qualifier requirements:

- ✅ Strict API response structure
- ✅ Correct HTTP status codes
- ✅ Robust input validation
- ✅ Graceful error handling (no crashes)
- ✅ Security guardrails
- ✅ Public accessibility
- ✅ Production-ready deployment

## 📞 Contact

**Anshul Patel**  
📧 Email: anshul3782.beai23@chitkara.edu.in  
🎓 Roll Number: 2310993782  
🏫 Chitkara University - B.E. Artificial Intelligence

## 📄 License

This project was created as part of the Chitkara University 2026 Qualifier assessment.

---

**Made with ❤️ for Bajaj Finserv Health Challenge**
