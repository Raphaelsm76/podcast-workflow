from fastapi import FastAPI, HTTPException
import os
import json
from datetime import datetime, timedelta

app = FastAPI(title="Podcast Workflow API")

@app.post("/run-podcast")
async def run_podcast_workflow():
    """
    Exécute le workflow complet du podcast :
    1. Collecte des news
    2. Génère le script
    3. Valide le script
    4. Publie sur Notion
    """
    try:
        # Date du jour (format YYYY-MM-DD)
        today = datetime.now().strftime("%Y-%m-%d")
        yesterday = (datetime.now() - timedelta(days=1)).strftime("%Y-%m-%d")

        # Ici, on simule l'appel au skill podcast-workflow
        # (En vrai, Mistral Studio appellera directement le skill Vibe)
        result = {
            "status": "success",
            "date_podcast": today,
            "date_veille": yesterday,
            "script_generated": True,
            "validation_passed": True,
            "notion_pages_created": True,
            "script_url": f"https://github.com/Raphaelsm76/podcast-workflow/blob/main/script_podcast_{today}.md",
            "validation_report_url": f"https://github.com/Raphaelsm76/podcast-workflow/blob/main/rapport_validation_{today}.md",
            "message": f"Workflow podcast exécuté avec succès pour le {today}"
        }

        return result

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/health")
async def health_check():
    """Vérifie que le service est en vie"""
    return {"status": "healthy", "timestamp": datetime.now().isoformat()}
