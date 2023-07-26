from rss_feed_summarizer import get_rss_feed, get_article, summarize_article, get_llm_model, sanitize_summary

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

def test_sanitize_summary():
    summary = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
    """

    text_only = sanitize_summary(summary)

    assert len(text_only) > 0
    assert "href" not in text_only
    assert "</p>" not in text_only
    assert "<a" not in text_only