import ollama

def main():
  prompt()

def prompt():
  response = ollama.chat(
    model="gemma3:1b",
    messages=[{"role": "user", "content": "What is the purpose of life?"}]
)
  print(response["message"]["content"])

main()
