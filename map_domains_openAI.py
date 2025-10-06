import json

# 1. Define your mapping (fill in with your actual categories)
DOMAIN_TO_CATEGORY = {
"Access and Availability": "Other",
"Access to Care": "Cost",
"Access to Treatment": "Other",
"Accessibility and Availability": "Other",
"Adherence and Compliance": "Clinical effectiveness",
"Biomarker and Genetic Considerations": "Biomarkers and personalized medicine",
"Biomarker and Genetic Testing": "Biomarkers and personalized medicine",
"Biomarkers and Genetic Testing": "Biomarkers and personalized medicine",
"Clinical Efficacy": "Clinical effectiveness",
"Clinical Guidelines and Evidence": "Clinical effectiveness",
"Clinical Guidelines and Recommendations": "Clinical effectiveness",
"Comparative Effectiveness": "Clinical effectiveness",
"Cost-Effectiveness": "Cost",
"Cultural and Ethical Considerations": "Patient-centered outcomes and preferences",
"Economic Considerations": "Cost",
"Ethical Considerations": "Patient-centered outcomes and preferences",
"Genomic and Biomarker Considerations": "Biomarkers and personalized medicine",
"Guideline Recommendations": "Clinical effectiveness",
"Health System Factors": "Cost",
"Healthcare Provider Experience": "Other",
"Healthcare System Factors": "Cost",
"Impact on Comorbidities": "Biomarkers and personalized medicine",
"Impact on Future Treatment Options": "Other",
"Impact on Lifestyle": "Patient-centered outcomes and preferences",
"Impact on Lifestyle and Daily Living": "Patient-centered outcomes and preferences",
"Impact on Mental Health": "Patient-centered outcomes and preferences",
"Interdisciplinary Collaboration": "Other",
"Lifestyle and Functional Impact": "Patient-centered outcomes and preferences",
"Logistical Considerations": "Other",
"Long-Term Outcomes": "Clinical effectiveness",
"Long-term Outcomes": "Clinical effectiveness",
"Long-term Outcomes and Follow-up": "Clinical effectiveness",
"Long-term Outcomes and Survivorship": "Clinical effectiveness",
"Monitoring and Follow-Up": "Other",
"Multidisciplinary Care": "Cost",
"Patient Education and Engagement": "Other",
"Patient Education and Informed Decision-Making": "Other",
"Patient Education and Support": "Other",
"Patient Empowerment and Engagement": "Patient-centered outcomes and preferences",
"Patient Engagement and Shared Decision-Making": "Patient-centered outcomes and preferences",
"Patient Preferences and Values": "Patient-centered outcomes and preferences",
"Patient Support and Resources": "Cost",
"Patient and Family Impact": "Patient-centered outcomes and preferences",
"Patient and Provider Communication": "Other",
"Patient-Reported Outcomes": "Patient-centered outcomes and preferences",
"Personalization and Biomarkers": "Biomarkers and personalized medicine",
"Personalization and Genetic Factors": "Biomarkers and personalized medicine",
"Psychosocial Factors": "Patient-centered outcomes and preferences",
"Psychosocial Impact": "Patient-centered outcomes and preferences",
"Regulatory Approval and Market Access": "Other",
"Regulatory and Approval Status": "Clinical effectiveness",
"Research and Evidence Base": "Clinical effectiveness",
"Research and Innovation": "Other",
"Safety and Tolerability": "Clinical effectiveness",
"Social and Environmental Factors": "Patient-centered outcomes and preferences",
"Social and Family Considerations": "Patient-centered outcomes and preferences",
"Societal Impact": "Other",
"Socioeconomic Factors": "Cost",
"Support Systems": "Patient-centered outcomes and preferences",
"Supportive Care Needs": "Cost",
"Supportive Care Options": "Cost",
"Supportive Care and Management": "Cost",
"Supportive Care and Resources": "Cost",
"Treatment Accessibility": "Other",
"Treatment Administration": "Patient-centered outcomes and preferences",
"Treatment Guidelines and Evidence": "Clinical effectiveness"
}

with open("extracted_domains_openAI.json", "r", encoding="utf-8") as f:
    all_domains = json.load(f)

# 2. Append category for each domain
all_domains_with_categories = []
for response in all_domains:
    response_with_categories = []
    for domain in response:
        category = DOMAIN_TO_CATEGORY.get(domain, "Other")
        response_with_categories.append({"domain": domain, "category": category})
    all_domains_with_categories.append(response_with_categories)

# 3. Save the new structure
with open("domains_with_categories_openAI.json", "w", encoding="utf-8") as f:
    json.dump(all_domains_with_categories, f, ensure_ascii=False, indent=2)

print("Saved domains with categories to domains_with_categories_openAI.json")