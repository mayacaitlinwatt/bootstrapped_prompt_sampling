# Bootstrapped Prompt Sampling (BPS)

This repository documents **Bootstrapped Prompt Sampling (BPS)**, a model-agnostic method for evaluating the distribution of large language model (LLM) outputs. Contributers include Stephen Watt, Brett South, Jay Ronquillo, and Jonathan Mauer. This methodology is applicable to knowledge mining, ontology development, AI safety and reproducibility, and prompt engineering. Research is ongoing.

Our goal is to examine the extent to which LLMs produce stable conceptual categories vs. semantic noise. Our particular use case is in knowledge mining, more specifically, patient unmet need in evaluation frameworks.

## Methods

The core of our methodology is running a single prompt 100+ times and analysing the distribution of outputs. This method is novel in that it uncovers the semantic landscape in which the LLM generates its outputs from. This landscape is reproducible, and is valuable in knowledge mining, ontology development, AI safety and reproducibility, and prompt engineering. Our particular use case is knowledge mining, where high-temperature, non-deterministic LLMs show promise for uncovering unmet patient need. Such high-temperature, non-deterministic LLMs are not utilised for different reasons, one being their tendancy to produce different outputs given the same prompt. This is an issue in use cases like healthcare where reproducibility is a priority. Our methodology overcomes this issue by producing distriutions of LLM outputs instead of single outputs. These distributions are stable, with knowledge ranked from high-frequency responses at the top to low-frequency "noise" at the bottom. 

Our chosen prompt was the following: please generate a list of domains that would enable a patient and physician to assess the value of a particular breast cancer treatment.

Models: Deepseek and ChatGPT 4o-mini.

---

## Discussion

Our high-frequency outputs included domains like "efficacy" and "cost," which are well-known, well-defined domains already in the ASCO framework, as well as low-frequency outputs, which we consider noise and included more ambiguous domains and rewordings of other domains (e.g. "Safety & Access"). Interestingly, there were domains that did not appear in the ASCO framework that were present in multiple iterations of BPS. These domains had a moderate frequency and appeared in the center of the distribution. They included references to things like "location" and "caregiver burden." Presence of these domains show promise for BPS as a knowledge-mining tool.
Further, domains already present in the ASCO framework dominated the top section of our distribution, hinting at a kind of concordence (as well as peace-of-mind that the LLM understood our context.) However, more validation is needed.

---

**Motivating questions:**
>"How many iterations does it take for the LLM to produce a stable distribution?"
>
>"How does the distribution change with small vs large changes to the prompt?"
> 
>"What does the distribution of high-temperature LLMs look like, vs low-temperature? Reasoning LLMs vs non-reasoning?"

---

## Pipeline Summary

Each stage of the workflow is implemented in a separate script under `src/`.

| Step | Script | Description |
|------|---------|-------------|
| 1 | `llm_call.py` / `llm_client.py`| Sends the same prompt to an LLM (DeepSeek and ChatGPT 4o-mini) 100 times and saves all outputs. |
| 2 | `extract_domains.py` | Extracts domains from the raw text outputs. |
| 3 | `map_domains.py` / `map_domains_round2.py` / `map_domains_openai`| Each unique domain name is assigned to 1 of 5 categories. These mappings were validated by a domain expert. Note: this step is not necessary to run BPS, it was simply to see if certain categories clustered differently in the distribution (e.g., if cost-related categories clustered differently to patient-preference categories)  |
| 4 | `categorical_analysis.py` | Produces a frequency distribution of the unique domain names. |

---

### Additional observations

- 100 DeepSeek generations produced about 165 unique domains, wheras ChatGPT 4o-mini produced about 65.
- ChatGPT had, in general, less word variation than Deepseek.
- The most frequent domain from ChatGPT ("Clinical Efficacy") appeared in 100% of responses, wheras Deepseek's ("Safety & Tolerability") appeared in only 60% of responses.
  
---

## Set-up

(1) You'll need to run: pip install requests
(2) Create a file called config.py with your OpenRouter API key (OPENROUTER_API_KEY = "sk-...") (one is provided when you make an OpenRouter account online).
(3) Begin by running llm_call.py. It'll take approximately 1 hour and 40 minutes as there's a rate limit.
