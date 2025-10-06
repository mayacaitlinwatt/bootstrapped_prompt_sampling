from llm_client import LLMClient

if __name__ == "__main__":
    client = LLMClient(model="openai/gpt-4o-mini")
    prompt = "Please generate a list of domains that would enable a patient and physician to assess the value of a particular breast cancer treatment."
    outputs = []
    for i in range(100):
        response = client.generate(prompt)
        outputs.append(f"Response {i+1}:\n{response}\n{'-'*40}\n")
    with open("llm_outputs.txt", "w", encoding="utf-8") as f:
        f.writelines(outputs)
    print("Saved 100 LLM responses to llm_outputs.txt")