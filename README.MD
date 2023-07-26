## Installation

1. Clone repository https://github.com/makh-sada/rss-feed-summarizer.
2. Create a virtual environment.
3. Activate virtual environment.
4. Install the required dependecies.

```
python3 -m venv venv
```
### Activate the virtual environment
```
source venv/bin/activate
```
### Install the required dependencies
```
pip install -r requirements.txt
```

## Running the tests
Execute the following command to run the tests.
```
pytest
```
Expected output
```
The tests should pass without any errors.
```

## Running application locally
Ensure you have authenticated to Google Cloud using `gcloud auth application-default login` or provided service account credentials. For details instructions follow https://cloud.google.com/docs/authentication/provide-credentials-adc#local-dev

Run from application folder 
```
streamlit run rss_feed_summarizer.py
```

## Deactivate the virtual environment
```
deactivate
```