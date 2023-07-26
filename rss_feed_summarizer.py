import feedparser
import streamlit as st
from langchain.chains.summarize import load_summarize_chain
from langchain.llms import VertexAI
from langchain.document_loaders import WebBaseLoader


def get_rss_feed(url):
    feed = feedparser.parse(url)

    return feed


def get_article(url):
    loader = WebBaseLoader(url)
    docs = loader.load()

    return docs


def get_llm_model(temperature=0.2, max_output_tokens=256, top_k=40, top_p=0.95):
    return VertexAI(
            model_name="text-bison@001",
            temperature=temperature,
            max_output_tokens=max_output_tokens,
            top_k=top_k,
            top_p=top_p,
        )

def summarize_article(doc_article, llm):
    doc_length = sum([len(d.page_content) for d in doc_article])
    print(f"article length: {doc_length}")

    chain = load_summarize_chain(llm, chain_type="stuff", verbose=True)

    text_summary = chain.run(doc_article)

    return text_summary


def main():
    st.title("RSS Feed Summary")

    url = st.text_input("Enter RSS feed URL", "https://cloudblog.withgoogle.com/products/data-analytics/rss/")
    if url:
        rss_feed = get_rss_feed(url)
        articles = rss_feed["entries"]

        number_of_articles = st.sidebar.number_input(
            "Number of articles to summarize", min_value=1, max_value=10, value=2
        )

        temperature = st.sidebar.slider("Temperature", 0.1, 1.0, value=0.2)
        max_output_tokens = st.sidebar.slider("maxOutputTokens", 1 , 1024, value=256)
        top_k = st.sidebar.slider("topK", 1, 40, value=40)
        top_p = st.sidebar.slider("topP", 0.0, 1.0, value=0.95)

        vertex_llm_text = get_llm_model(temperature, max_output_tokens, top_k, top_p)

        for article in articles[:number_of_articles]:
            title = article["title"]
            link = article["link"]
            text = get_article(link)

            summary = summarize_article(text, vertex_llm_text)

            st.divider()
            st.subheader(title, help=f"Published on {article['published']}")
            st.write(summary)
            st.markdown("[more...](%s)" % link)


if __name__ == "__main__":
    main()
