# AI Database Chat with n8n

Chat with PostgreSQL database using natural language powered by Groq LLM.

## Setup

### Prerequisites
- PostgreSQL installed locally
- n8n (running via Docker)
- Groq API key

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
2. Configure Groq Chat Model credential with your API key
3. Configure PostgreSQL credential
4. Model: `llama-3.3-70b-versatile`

## Usage
Ask questions like:
- "How many total orders are in the database?"
- "What are the top 5 best-selling products?"
- "Show me monthly sales trends"

## Workflow Components
- Trigger: Chat message received
- AI Agent with SQL tools
- PostgreSQL integration
- Memory for conversation context
