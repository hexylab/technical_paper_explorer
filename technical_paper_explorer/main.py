from paper_fetcher import fetch_papers
from citation_fetcher import fetch_citations

def main():
    # 論文データを取得
    papers = fetch_papers(search_query="all:deep learning",max_results=10)
    
    # 論文IDに基づいて引用数を取得
    paper_ids = papers['id'].tolist()
    citations = fetch_citations(paper_ids)
    
    # 引用数をDataFrameに追加
    papers['citations'] = citations
    
    # 結果を引用数の降順でソート
    sorted_papers = papers.sort_values(by='citations', ascending=False)
    
    # 結果を表示
    print(sorted_papers)
    
    # 結果をCSVファイルに保存
    sorted_papers.to_csv('papers_with_citations.csv', index=False)
    print("結果が 'papers_with_citations.csv' に保存されました。")

if __name__ == "__main__":
    main()
