from rss_feed_summarizer import get_rss_feed, get_article, summarize_article, get_llm_model

def test_get_rss_feed():
    rss_feed_url = "https://cloudblog.withgoogle.com/products/data-analytics/rss/"
    rss_feed = get_rss_feed(rss_feed_url)
    print(f"entries:{len(rss_feed['entries'])}")
    assert rss_feed is not None
    assert len(rss_feed["entries"]) > 0

def test_get_article():
    article_url = "https://cloud.google.com/blog/products/data-analytics/unlock-insights-faster-from-your-mysql-data-in-bigquery/"
    article_text = get_article(article_url)
    assert article_text is not None
    assert len(article_text) > 0

def test_summarize_article():
    article_url = "https://cloud.google.com/blog/products/data-analytics/unlock-insights-faster-from-your-mysql-data-in-bigquery/"
    article_text = get_article(article_url)

    summary = summarize_article(article_text, get_llm_model())

    print(summary)
