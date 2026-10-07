# AI Prompt Injection Firewall

An AI-powered security layer designed to detect and mitigate prompt injection attacks in Large Language Model (LLM) applications.

## Project Overview

The AI Prompt Injection Firewall analyzes user prompts before they are sent to an LLM. The system will use rule-based detection, machine learning-based classification, and risk scoring to identify potentially malicious prompts.

## Planned Classification

- SAFE
- SUSPICIOUS
- MALICIOUS

## Planned Decisions

- SAFE → ALLOW
- SUSPICIOUS → FLAG
- MALICIOUS → BLOCK

## Technology Stack

### Frontend
- React
- TypeScript
- Vite
- Tailwind CSS

### Backend
- Python
- FastAPI
- Uvicorn

### AI/ML
- PyTorch
- Hugging Face Transformers
- DistilBERT
- Scikit-learn

### Database
- MongoDB

### Development
- Visual Studio Code
- Git
- GitHub
- Docker

## Current Status

### Phase 1 — Project Setup

Completed:

- Project structure
- Python 3.12 virtual environment
- FastAPI backend
- Uvicorn server
- Root API
- Health-check API
- Swagger API documentation

## Backend API

### Root

`GET /`

### Health Check

`GET /api/health`

### API Documentation

`GET /docs`

## Project Structure

```text
AI-Prompt-Injection-Firewall/
├── backend/
│   ├── app/
│   │   ├── api/
│   │   ├── core/
│   │   ├── detectors/
│   │   ├── models/
│   │   ├── schemas/
│   │   ├── services/
│   │   └── main.py
│   └── requirements.txt
├── frontend/
├── ml/
│   ├── datasets/
│   ├── evaluation/
│   ├── models/
│   └── training/
├── tests/
├── docs/
├── docker/
├── .env.example
├── .gitignore
└── README.md