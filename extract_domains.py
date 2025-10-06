import re
import json

def extract_domains_from_response(response_text):
    """
    Extracts domain names in the format '1. **Domain Name**' from a single LLM response.
    Returns only the domain name (not the number or period).
    """
    domains = []
    # Match lines like 1. **Domain Name**
    matches = re.findall(r"\d+\.\s+\*\*([^\*]+)\*\*", response_text)
    for match in matches:
        domains.append(match.strip())
    return domains

def extract_all_domains(filename):
    with open(filename, "r", encoding="utf-8") as f:
        content = f.read()

    # Split responses by the separator line
    responses = content.split('-' * 40)
    all_domains = []

    for resp in responses:
        domains = extract_domains_from_response(resp)
        if domains:
            all_domains.append(domains)

    return all_domains

if __name__ == "__main__":
    filename = "llm_outputs_openAI.txt"
    all_domains = extract_all_domains(filename)
    # Save to JSON file
    with open("extracted_domains_openAI.json", "w", encoding="utf-8") as f:
        json.dump(all_domains, f, ensure_ascii=False, indent=2)
    print("Extracted domains saved to extracted_domains_openAI.json")