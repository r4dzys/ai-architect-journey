import ollama

def inicjuj_historie(system_prompt):
    return [{"role": "system", "content": system_prompt}]

def dodaj_wiadomosc(historia, rola, tresc):
    historia.append({"role": rola, "content": tresc})
    return historia

def zapytaj_model(historia, model="gemma3:1b"):
    response = ollama.chat(model=model, messages=historia)
    odpowiedz = response["message"]["content"]
    dodaj_wiadomosc(historia, "assistant", odpowiedz)
    return odpowiedz

def chatbot(system_prompt, pytania):
    historia = inicjuj_historie(system_prompt)

    for pytanie in pytania:
        dodaj_wiadomosc(historia, "user", pytanie)
        odpowiedz = zapytaj_model(historia)
        print(f"User: {pytanie}")
        print(f"Model: {odpowiedz}\n")

# Uruchomienie
chatbot(
    system_prompt="Jesteś doświadczonym AI Architektem. Każdą odpowiedź strukturyzujesz w trzech częściach: 1) Definicja 2) Przykład 3) Zastosowanie biznesowe.",
    pytania=[
        "Jak nazywa się technologia która łączy LLM z własnymi dokumentami?",
        "Czy możesz podać przykład zastosowania?"
    ]
)
