import json
from collections import Counter
import matplotlib.pyplot as plt

def load_domains(filename):
    with open(filename, "r", encoding="utf-8") as f:
        all_domains = json.load(f)
    return all_domains

def count_domains(all_domains):
    flat_domains = [d["domain"] for response in all_domains for d in response]
    return Counter(flat_domains)

def get_domain_categories(all_domains):
    # Returns a dict: domain -> category (assumes all domains have the same category everywhere)
    domain_to_category = {}
    for response in all_domains:
        for d in response:
            domain_to_category[d["domain"]] = d["category"]
    return domain_to_category

if __name__ == "__main__":
    filename = "domains_with_categories_openAI.json"
    all_domains = load_domains(filename)
    domain_counts = count_domains(all_domains)
    domain_to_category = get_domain_categories(all_domains)

    # Assign a color to each category
    category_colors = {
        "Clinical effectiveness": "#1f77b4",
        "Cost": "#ff7f0e",
        "Patient-centered outcomes and preferences": "#2ca02c",
        "Biomarkers and personalized medicine": "#d62728",
        "Other": "#9467bd"
    }

    # Prepare data for plotting
    domains = [domain for domain, _ in domain_counts.most_common()]
    counts = [count for _, count in domain_counts.most_common()]
    categories = [domain_to_category.get(domain, "Other") for domain in domains]
    colors = [category_colors.get(cat, "#7f7f7f") for cat in categories]

    # Plot bar graph with larger figure and smaller y-tick labels
    plt.figure(figsize=(14, max(8, len(domains) * 0.4)))
    bars = plt.barh(domains, counts, color=colors)
    plt.xlabel('Frequency')
    plt.title('Domain Frequency Graph With Categories')
    plt.yticks(fontsize=8)  # Make y-axis labels smaller
    plt.tight_layout()
    plt.gca().invert_yaxis()  # Highest frequency at the top

    # Create legends
    handles = [plt.Rectangle((0,0),1,1, color=color) for color in category_colors.values()]
    plt.legend(handles, category_colors.keys(), title="Category")

    plt.savefig("domain_frequencies_bargraph_openAI.png", dpi=300)
    plt.show()