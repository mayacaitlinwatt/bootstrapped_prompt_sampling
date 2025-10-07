# Bootstrapped Prompt Sampling (BPS)

This repository documents **Bootstrapped Prompt Sampling (BPS)**, a model-agnostic method for evaluating the consistentsy of large language model (LLM) outputs. Contributers include Stephen Watt, Brett South, Jay Ronquillo, and Jonathan Mauer, and is applicable to knowledge mining, ontology development, AI safety and reproducibility, and prompt engineering. 

Our goal was to examine the extent to which LLMs produce stable conceptual categories vs. semantic noise. Our particular use case is patient-centered research, more specifically, patient values in breast cancer treatment. 

The core of our methodology is running a single prompt multiple times and graphing the outputs -- doing so ensures we observe the given LLM's entire semantic landscape of a particular prompt or domain. We are essentially reverse-engineering the sample space in which an LLM generates reponses from for use cases where a high temperature is valuable, but responses must be reproducible. Patient-centered research is one such use case, where we're interested in mining knowledge on unmet patient need, but must do so in a way that's valid and reproducible, which LLM's struggle with. 

Our work produced distributions that were stable and provided new knowledge. This new knowledge was found in domains that appeared a moderate amount, i.e. domains like "location", "caregiver burden", etc. that are not as common as "efficacy" and "cost", but are more common than domains that appear only once, and are classified as noise. These domains which appear a moderate amount are not a part of existing frameworks (e.g. the ASCO framework) but are produced stochastically by the LLM (and sometimes by more than one LLM), making BPS an LLM-agnostic and generalizable knowledge mining tool.

---

## Overview

The same prompt was sent to an LLM 100 times using a custom Python client.  
The responses were processed, cleaned, categorized, and analyzed for stability across runs.

**Core questions:**
> “What domains would enable a patient and physician to assess the value of a particular breast cancer treatment?”
> 
> "Does the distribution of outputs change if the prompt changes?"
> 
> "Does a different LLM generate the same distribution?"

---

## Pipeline Summary

Each stage of the workflow is implemented in a separate script under `src/`.

| Step | Script | Description |
|------|---------|-------------|
| 1 | `llm_call.py` / `llm_client.py`| Sends the same prompt to an LLM (DeepSeek and ChatGPT 4o-mini) 100 times and saves all outputs. |
| 2 | `extract_domains.py` | Extracts domains from the raw text outputs. |
| 3 | `map_domains.py` / `map_domains_round2.py` / `map_domains_openai`| Each unique domain name is assigned to 1 of 5 categories. These mappings were validated by a domain expert. Note: We also asked the LLM to do this task, but the outputs had errors in the domain names. Also, this step is not necessary to run BPS, it was simply to see if certain categories clustered differently in the distribution (e.g., if cost-related categories were clustered towards the top of the distribution, or if patient-preference categories were clustered towards the tail)  |
| 4 | `categorical_analysis.py` | Produces a frequency distribution of the unique domain names. |

---

### Key Observations
- 100 DeepSeek generations produced about 165 unique domains, wheras ChatGPT 4o-mini produced about 65.
- ChatGPT had, in general, less word variation than Deepseek.
- The most frequent domain from ChatGPT ("Clinical Efficacy") appeared in 100% of responses, wheras Deepseek ("Safety & Tolerability") appeared in 60% of responses.

### Discussion
- Deepseek produced almost 3 times as many unique domains as ChatGPT. Although it was "noisier" than ChatGPT, they weren't necessarily incorrect -- many were the same domain just worded differently.
- When we re-ran the DeepSeek model, the domain names of the top half of the distribution remained stable. This is promising for use cases that require stable and reproducible knowledge mining.

---

## Set-up

(1) You'll need to run: pip install requests
(2) Create a file called config.py with just your OpenRouter API key (OPENROUTER_API_KEY = "sk-...") (one is provided when you make an OpenRouter account online).
(3) Begin by running llm_call.py. It'll take approximately 1 hour and 40 minutes as there's a rate limit.
