import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

class Config:
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
    CHROMA_DB_PATH = os.getenv("CHROMA_DB_PATH", "./vector_db")
    
    @staticmethod
    def validate():
        if not Config.OPENAI_API_KEY or Config.OPENAI_API_KEY.startswith("sk-"):
            raise ValueError("❌ OPENAI_API_KEY is missing or invalid in .env file")

# Optional: Validate on import
# Config.validate()
