# AI Database Chat with n8n

Chat with PostgreSQL database using natural language powered by Groq LLM.

## Setup

### Prerequisites
- PostgreSQL installed locally
- n8n (running via Docker)
- Gemini API key

### Database Setup
1. Create database: `online_retail`
2. Import your CSV data
3. Connection details:
   - Host: `host.docker.internal` (for Docker) or `127.0.0.1`
   - Database: `online_retail`
   - User: your_username
   - Port: 5432

### n8n Configuration
1. Import the workflow JSON file
2. Configure Gemini Chat Model credential with your Gemini AI studio API key
3. Configure PostgreSQL credential
4. Model: `Gemini 3 Flash`

## Usage
Ask questions like:
- "Provide first 100 rows"
- "Most Sold Item"
- "Try to Categorize items"

## Workflow Components
- Trigger: Chat message received
- AI Agent with SQL tools
- PostgreSQL integration
- Memory for conversation context
