import requests
import pandas as pd

def fetch_citations(paper_ids):
    """Semantic Scholarから指定された論文IDの引用数を取得する関数"""
    citations = []
    for id in paper_ids:
        try:
            response = requests.get(f"https://api.semanticscholar.org/v1/paper/arXiv:{id}")
            citation_count = len(response.json()['citations'])
        except:
            citation_count = 0
        citations.append(citation_count)
    return citations