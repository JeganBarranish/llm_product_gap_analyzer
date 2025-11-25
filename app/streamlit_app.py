# streamlit_app.py
import streamlit as st
import json
from scripts.analyzer import analyze, load_products

st.set_page_config(page_title='Product Feature Gap Analyzer', layout='wide')
st.title('LLM-Based Product Feature Gap Analyzer')

st.markdown('Upload a JSON file with your product and competitor descriptions, or use sample data.')

uploaded = st.file_uploader('Upload products JSON', type=['json'])
if uploaded:
    data = json.load(uploaded)
    with open('data/uploaded_products.json','w') as f:
        json.dump(data,f,indent=2)
    data_path = 'data/uploaded_products.json'
else:
    st.info('Using sample dataset from data/sample_products.json')
    data_path = 'data/sample_products.json'

show_prompt = st.checkbox('Show generated prompt', value=False)

if st.button('Run Analysis'):
    with st.spinner('Running analysis...'):
        # In offline env, analysis will return placeholder unless user configures API key
        api_key = st.text_input('OpenAI API Key (optional)', type='password')
        output = analyze(data_path, openai_api_key=api_key if api_key else None)
        if isinstance(output, str) and output.startswith('LLM_OUTPUT_PLACEHOLDER'):
            st.warning('No LLM key configured — showing generated prompt snippet.')
            st.code(output[:1000])
        else:
            try:
                parsed = json.loads(output)
                st.success('Parsed JSON output')
                st.json(parsed)
            except Exception:
                st.subheader('LLM Output')
                st.text(output)

st.sidebar.markdown('## Tips')
st.sidebar.markdown('- Ensure your JSON contains one `product` object and one or more `competitor` objects.')
st.sidebar.markdown('- Sample format located at `data/sample_products.json`')
