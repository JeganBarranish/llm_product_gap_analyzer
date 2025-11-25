# analyzer.py
# Main analysis logic (template). Uses embeddings + LLM to produce feature gap analysis.
# Replace LLM calls with OpenAI or local transformers generation in your environment.

import json
from scripts.embeddings import Embedder
from scripts.prompts import GAP_ANALYSIS_PROMPT

def load_products(path):
    with open(path,'r') as f:
        return json.load(f)

def build_competitor_texts(products):
    target = next(p for p in products if p['type']=='product')
    competitors = [p for p in products if p['type']=='competitor']
    return target, competitors

def format_competitors(competitors):
    return '\n'.join([f"- {c['name']}: {c['description']}" for c in competitors])

def generate_prompt(product, competitors):
    comp_text = format_competitors(competitors)
    return GAP_ANALYSIS_PROMPT.format(product_name=product['name'], product_desc=product['description'], competitors=comp_text)

def call_llm(prompt, model='gpt-3.5-turbo', openai_api_key=None):
    # Template for calling OpenAI — replace with actual API call where allowed.
    try:
        import openai
        openai.api_key = openai_api_key
        resp = openai.ChatCompletion.create(
            model=model,
            messages=[{'role':'user','content':prompt}],
            max_tokens=800,
            temperature=0.2
        )
        return resp['choices'][0]['message']['content']
    except Exception as e:
        print('OpenAI call failed or not configured. Returning prompt for debugging.')
        return 'LLM_OUTPUT_PLACEHOLDER: ' + prompt[:500]

def analyze(path, openai_api_key=None):
    products = load_products(path)
    product, competitors = build_competitor_texts(products)
    prompt = generate_prompt(product, competitors)
    llm_output = call_llm(prompt, openai_api_key=openai_api_key)
    return llm_output

if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('--data', default='data/sample_products.json')
    parser.add_argument('--openai_key', default=None)
    args = parser.parse_args()
    print('Running analysis on', args.data)
    out = analyze(args.data, openai_api_key=args.openai_key)
    print('\n--- LLM OUTPUT ---\n')
    print(out)
