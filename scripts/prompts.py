# prompts.py
# Centralized prompt templates for the Product Feature Gap Analyzer.

GAP_ANALYSIS_PROMPT = """You are a product manager assistant. Given the following input:

Product: {product_name}
Description: {product_desc}

Competitors:
{competitors}

Task:
1) List features that competitors have which the product lacks or where the product is weaker.
2) For each gap, provide:
   - short description
   - priority (High/Medium/Low)
   - suggested approach (one-paragraph)
3) Suggest top 5 features to add with rationale and estimated user impact.

Provide output as JSON with keys: gaps (list), recommendations (list).
"""
