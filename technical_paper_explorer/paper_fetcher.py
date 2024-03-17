import arxiv
import pandas as pd

def fetch_papers(search_query, max_results=10):
    """arXivから指定されたクエリに基づいて論文データを取得する関数"""
    client = arxiv.Client()
    search = arxiv.Search(
        query=search_query,
        max_results=max_results,
        sort_by=arxiv.SortCriterion.SubmittedDate,
        sort_order=arxiv.SortOrder.Descending,
    )

    # 結果を保存するための空のリストを初期化
    papers_data = []
    
    # 検索結果を取得
    for result in client.results(search):
        papers_data.append({
            "title": result.title,
            "id": result.entry_id.split('/abs/')[-1],
            "arxiv_url": result.entry_id,
            "published": result.published,
            "summary": result.summary
        })
    
    # 結果をDataFrameに変換
    papers_df = pd.DataFrame(papers_data)
    
    return papers_df