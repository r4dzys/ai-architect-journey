import ollama

def inicjuj_historie(system_prompt):
    return [{"role": "system", "content": system_prompt}]

def zapytaj_model(historia, model="gemma3:1b"):
    response = ollama.chat(model=model, messages=historia)
    return response["message"]["content"]

def main():
    historia = inicjuj_historie(
        "Jesteś doświadczonym AI Architektem. Odpowiadasz precyzyjnie i technicznie."
    )
    
    print("Chatbot gotowy. Wpisz 'koniec' aby zakończyć.\n")
    
    while True:
        pytanie = input("Ty: ")
        
        if pytanie.lower() == "koniec":
            print("Do zobaczenia!")
            break
        
        historia.append({"role": "user", "content": pytanie})
        odpowiedz = zapytaj_model(historia)
        historia.append({"role": "assistant", "content": odpowiedz})
        
        print(f"Model: {odpowiedz}\n")

if __name__ == "__main__":
    main()
