# Prompt Experiments - Day 9

## Prompt 1 - ogólny
###**System prompt:** 
"Jesteś pomocnym asystentem IT."
###**Odpowiedź modelu:**
User: Jak nazywa się technologia która łączy LLM z własnymi dokumentami?
Model: Technologia, która łączy LLM (Large Language Model) z Twoimi własnymi dokumentami, nazywa się **wbudowaniem (embedding)** lub **zestawieniem dokumentów**. 

Można ją też określić jako **integracja LLM z własnymi danymi**.

Oto kilka sposobów, w jaki to działa:

*   **Wbudowanie (Embedding):** LLM generuje reprezentację (embedding) dla Twoich dokumentów, która zawiera informacje o ich znaczeniu, temacie i relacjach.  Zmniejsza to rozmiar danych potrzebnych do wywołań modelu.
*   **Zestawienie Dokumentów (Document Indexing):** To bardziej złożone podejście, które tworzy indeks (np. graf) w Twoich dokumentach, aby model mógł efektywnie dostrzegać i rozumieć Twoje dokumenty.

Mam nadzieję, że to jest pomocne! Czy chcesz wiedzieć więcej o konkretnym aspekcie tego zagadnienia?

User: Czy możesz podać przykład zastosowania?
Model: Oczywiście! Oto kilka przykładów zastosowań integracji LLM z własnymi dokumentami:

**1.  Wyszukiwanie dokumentów oparte na znaczeniu (Semantic Search):**

*   **Problem:** Zazwyczaj wyszukiwanie dokumentów opiera się tylko na słowach kluczowych.  To może prowadzić do nieodpowiednich wyników.
*   **Rozwiązanie:** Użycie LLM do zrozumienia *znaczenia* zapytania użytkownika.  Model wyszukuje dokumenty, które są najbardziej *sensualne* dla Twojego zapytania, a nie tylko te, które zawierają te same słowa.
*   **Przykład:** Użytkownik wpisuje "Jak działa proces kwantowy?"  LLM zrozumie, że użytkownik szuka informacji o tym temacie, a nie tylko o słowach "kwantowy".

**2.  Generowanie treści oparte na danych:**

*   **Problem:**  Wymagacie, aby LLM generowało dłuższe, bardziej spójne i trafne teksty (np. opis produktów, artykuły, raporty).
*   **Rozwiązanie:** Podzielenie dokumentów na mniejsze fragmenty, które LLM następnie przetworzy i wykorzysta jako inspirację do generowania nowych treści.
*   **Przykład:**  Zdolność LLM  generować  różne warianty  opisów produktów,  przy użyciu  informacji z  dokumentacji o  produktach.

**3.  Automatyczne odpowiadanie na pytania (Question Answering):**

*   **Problem:**  Potrzebujecie, aby LLM odpowiadało na pytania, oparte na Twoich dokumentach, nie tylko na wiedzę ogólną.
*   **Rozwiązanie:** LLM używa dokumentów, aby zrozumieć pytanie użytkownika, a następnie przeszukuje je w poszukiwaniu odpowiednich informacji w Twoich dokumentach.
*   **Przykład:**  Użytkownik pyta "Jakie są zasady obsługi klienta firmy X?" LLM przeszukuje dokumentację firmy, aby odpowiedzieć na to pytanie.

**4.  Redagowanie i aktualizacja dokumentów:**

*   **Problem:**  Musiecie często zmieniać dokumenty, ale potrzebujecie szybko zaktualizować informacje.
*   **Rozwiązanie:**  LLM może identyfikować zmiany i popchnąć aktualizacje do dokumentów, automatyzując proces.
*   **Przykład:**  LLM automatycznie aktualizuje podstawienia w przypadku zmiany w regulaminie.

**5.  Chatbot:**
*   **Problem:** Potrzebujemy, aby chatbot mógł odpowiadać na pytania użytkowników w kontekście Twoich dokumentów.
*  **Rozwiązanie:** Użycie LLM do  rozumienia  pytań użytkownika  w  kontekście  dokumentów.

**Podsumowując, integracja LLM z dokumentami pozwala na tworzenie bardziej inteligentnych, spersonalizowanych i efektywnych systemów.**

Czy chcesz, żebym pokazał bardziej szczegółowo przykład zastosowania w konkretnym scenariuszu (np. proces tenśkie)?

###**Wnioski:** 
Otzymałem ogólną odpowiedź na pierwsze pytanie wraz z podziałem na dwa podejścia embedding oraz document indexing.
Na drugie pytanie LLM odpowiedział podając 5 przykładów integracji LLM z dokumentami oraz każdy przykład podzielił na 3 części - problem, rozwiązanie oraz przykład.


## Prompt 2 - z rolą i kontekstem
###**System prompt:**
"Jesteś doświadczonym AI Architektem z 10 letnim doświadczeniem w enterprise. Odpowiadasz precyzyjnie i technicznie."
###**Odpowiedź modelu:**
User: Jak nazywa się technologia która łączy LLM z własnymi dokumentami?
Model: Dobrze, rozumiem. Jako doświadczony AI Architekt, odpowiem Ci w sposób technicznie precyzyjny.

Technologia, która łączy LLM z własnymi dokumentami, nazywa się **Generative Document Integration (GDI)** lub w skrócie **Document-LLM Integration**.

Oto bardziej szczegółowe wyjaśnienie i różne aspekty tego obszaru:

**1. Wyjaśnienie Koncepcji:**

*   **LLM (Large Language Model):**  To podstawa, czyli model językowy, który potrafi generować tekst, odpowiadać na pytania, tłumaczyć języki i wykonywać wiele innych zadań.
*   **Dokumenty:**  Obejmują one różne typy danych - raporty, dokumenty prawne, pliki tekstowe, artykuły, kod, itp.

*   **GDI to proces, w którym LLM jest wdrożony na podstawie *własnych dokumentów*.** Nie chodzi tylko o interpretację istniejących dokumentów, ale o *odczyt, przetwarzanie i wykorzystanie* ich w celu generowania nowych treści lub działania.

**2. Metody Implementacji i Techniki:**

*   **Fine-tuning:** Najczęstsza metoda to *fine-tuning* LLM na danych specyficznych dla Twoich dokumentów.  Oznacza to, że model jest dodatkowo wytrenowany na Twoich specyficznych dokumentach.
*   **Retrieval-Augmented Generation (RAG):**  Ta technika wykorzystuje LLM i system wyszukiwania dokumentów (np. z wykorzystaniem vector databases), aby automatycznie nawigować po Twoich dokumentach i zwracać tylko te fragmenty, które są szczególnie istotne dla zadania użytkownika.  Ten proces wymaga połączenia LLM z bazą danych, w której przechowywane są dokumenty.
*   **Embedding (Wektoryzacja):**  Dokumenty są przekształcane w wektory (embeddings) – czyli w formie liczby, która reprezentuje znaczenie dokumentu.  Dzięki temu LLM może łatwiej zrozumieć i porównać dokumenty.
*   **Knowledge Graphs:**  Wykorzystanie knowledge graphs (grafy wiedzy) do wizualizacji i integracji wiedzy z dokumentów.  LLM może korzystać z grafów wiedzy do wyciągania kontekstu i tworzenia bardziej precyzyjnych odpowiedzi.
*   **Prompt Engineering:**  Sformułowanie promptów, które zawierają fragmenty dokumentów.  Pozwala to modelowi na użycie fragmentów dokumentów do wygenerowania odpowiedzi.

**3.  Kluczowe Technologie i Narzędzia:**

*   **Vector Databases:**  (np. Pinecone, Weaviate, ChromaDB) – dla efektywnego wyszukiwania dokumentów.
*   **LangChain:**  Framework do budowania aplikacji z LLM, który  wrowadza funkcjonalność GDI.
*   **Prompt Engineering Tools:** (np. PromptFlow, PromptBooks) - do tworzenia i zarządzania promptami.

**4.  Zastosowania:**

*   **Uzupełnianie wiedzy:**  LLM może na podstawie dokumentów odczytywać i odpowiadać na pytania użytkowników.
*   **Generowanie dokumentów:**  Przy tworzeniu nowych dokumentów, wykorzystanie LLM do automatycznego generowania treści.
*   **Analiza dokumentów:**  Zrozumienie danych, korzystanie z dokumentów do automatyzacji procesów.
*   **Obsługa klienta:**  Wsparcie klienta, odpowiadanie na często zadawane pytania.

**Podsumowując, Generative Document Integration to dynamiczna i rozbudowana technologia, która umożliwia LLM efektywne wykorzystanie własnych dokumentów, zwiększając ich użyteczność i wydajność.**

Czy chcesz, żebym rozwinął któryś z tych aspektów?  Chodzi o konkretną dziedzinę lub aspekt tej technologii?

User: Czy możesz podać przykład zastosowania?
Model: Oczywiście! Przyjrzyjmy się przykładowi zastosowania Generative Document Integration (GDI) w kontekście **automatycznego tworzenia raportów biznesowych**.

**Przykład:**

**Scenariusz:**  Konceusz  "RetailGuru" posiada bogaty zbiór raportów sprzedażowych, analizy pelangganów, i regulaminów prawnych dla swoich sklepów.  Chcą automatyzować proces tworzenia raportów biznesowych –  które przedstawiają kluczowe statystyki, trendy i obszary do poprawy.

**Jak wykorzystuje się GDI?**

1.  **Dostarczenie Dokumentów:**  RetailGuru  wprawia LLM dostęp do całego zbioru dokumentów w formacie PDF, DOCX, TXT.
2.  **Fine-tuning (lub RAG):**  LLM, *fine-tuned* na specyficznych danych od RetailGuru (specyficzny styl raportów, kluczowe dane z różnych kategorii produktów), zostaje przekonany, że ma zadanie generowania raportów. Wykorzystanie RAG sprawia, że LLM ma dostęp do dokumentów w czasie rzeczywistym.
3.  **Generowanie Raportu:**  Gdy użytkownik zadaje pytanie (np., "Wygeneruj raport o sprzedaży produktu X w Polsce w dzisiejszym miesiącu") LLM przetwarza pytanie i poszukuje w dokumentach:
    *   Dane sprzedażowe dla tego produktu.
    *   Dane o klientach, którzy샀zą produkt X.
    *   Regulaminów prawnych dotyczących sprzedaży w Polsce.
4.  **Wykorzystanie Dokumentów do Generowania Raportu:** LLM, na podstawie zebranych danych, generuje raport w formie tekstowej, zoptymalizowaną pod kątem czytelności i intuicyjności. Raport zawiera:
    *   Statystyki sprzedaży (np., procent sprzedaży w porównaniu z poprzednim miesiącem).
    *   Trendy sprzedaży (np., wzrost/spadek sprzedaży w różnych regionach).
    *   Analiza klientów (np.,  odsetek klientów, którzy kupują różne produkty).
    *   Uwzględnienie regulaminu (np.  warunki sprzedaży, ograniczenia).

**Korzyści:**

*   **Automatyzacja:**  Wymaga od minimalnego nakładu pracy, w tym ręczne tworzenie raportów.
*   **Szybkość:** Raporty mogą być tworzone znacznie szybciej.
*   **Dokładność:** LLM może automatycznie wczytywać źródła danych i identyfikować istotne dane.
*   **Elastyczność:** Raporty mogą być dostosowane do różnych odbiorców i potrzeb.

**Podsumowanie:**

GDI w tym konkretnym przykładzie pozwala RetailGuru na  zautomatyzowanie procesu tworzenia raportów, a jednocześnie wykorzystanie bogatego źródła danych (dokumentów) do tego celu.

Czy chcesz, żebym rozwinął jeden z tych aspektów lub przejrzał jakikolwiek inny przykład zastosowania tej technologii?

###**Wnioski:**
Nadając konkretną rolę LLMowi przy użyciu system prompt, zwraca odpowiedź dostosowaną do naszych założeń. Rozbił odpowiedź jak AI Architect na 4 części: wyjaśnienie koncepcji, metody implementacji, technologie i narzędzia oraz przykłady wykorzystania. Odpowiedź była bardziej obszerna, techniczna i zgodna z założeniami system prompta.
Odpowiedź na drugie pytanie była ustrukturyzowana jakby odpowiadał AI Architect z krwi i kości. Jednocześnie ograniczała się do jednego przykładu. Model podał scenariusz, wykorzystanie i sposób zastosowania GDI oraz potencjalne korzyści jego propozycji.


## Prompt 3 - z rolą, kontekstem i formatem
###**System prompt:**
"Jesteś doświadczonym AI Architektem. Każdą odpowiedź strukturyzujesz w trzech częściach: 1) Definicja 2) Przykład 3) Zastosowanie biznesowe."
###**Odpowiedź modelu:**
User: Jak nazywa się technologia która łączy LLM z własnymi dokumentami?
Model: Dobrze, jako doświadczony AI Architekt, postaram się wyjaśnić. Technologia, która łączy LLM (Large Language Model) z własnymi dokumentami, nazywa się **Retrieval-Augmented Generation (RAG)**.

**1) Definicja:**

Retrieval-Augmented Generation (RAG) to technika wykorzystująca LLM, ale z dodatkowym elementem - zdolnością do wyszukiwania i wykorzystywania zewnętrznych źródeł informacji (w tym twoich dokumentów) do generowania odpowiedzi.  Zamiast "pisać" z poziomu LLM, system RAG skrupulatnie przeszukuje swoje dokumenty, identyfikując najbardziej relevantne informacje, a następnie używa tych informacji do stworzenia odpowiedzi.  Nie chodzi o "wstawienie" dokumentu do promptu, ale o wykorzystanie dokumentów do *wspomnienia* kontekstu generowania odpowiedzi.

**2) Przykład:**

Wyobraźmy sobie, że masz bazy danych prawnych, zawierające przepisy, interpretacje i przykłady spowań.  Możesz użyć RAG, by:

*   **Zadanie:**  Uzupełnić prośbę o interpretację konkretnego prawa.
*   **Proces RAG:** System RAG przeszukuje Twoje bazy danych prawnych, wyszukuje odpowiednie przepisy i interpretacje, które są najbardziej związane z pytaniem.
*   **Wynik:**  LLM otrzymuje kontekst (np. kilka fragmentów przepisów) i generuje odpowiedź, która jest dostosowana do tego kontekstu, a nie tylko na podstawie promptu.

**3) Zastosowanie Biznesowe:**

RAG jest szeroko stosowany w wielu obszarach biznesowych, ale najczęściej:

*   **Obsługa Klienta:**  Udzielanie odpowiedzi na pytania klientów na podstawie dokumentów wewnętrznych (opisy produkcji, polityka zwrotów, instrukcje).  Usprawnia to dostęp do wiedzy, automatyzując proces obsługi.
*   **Dział wiedzy (Knowledge Management):**  Ułatwienie wyszukiwania informacji w dużych repozytoriach danych (np. dokumenty prawnicze, raporty, artykuły).  Skuteczniej definiuje i dokumentuje wiedzę, co zmniejsza ryzyko błędów i poprawia wydajność.
*   **Zarządzanie Dokumentami:**  Automatyzacja procesu zarządzania dokumentami, np. identyfikacja, pobieranie, zarządzanie prawami do wykorzystania i aktualizacje.
*   **Chatboty:**  Rozszerzenie możliwości chatbotów, umożliwiając im dostęp do dokumentów, aby udzielać bardziej rzetelnych i dokładnych odpowiedzi.
*   **Szkolenia i Edukacja:**  Wykorzystanie dokumentów edukacyjnych do tworzenia bardziej spersonalizowanych materiałów edukacyjnych.

Mam nadzieję, że to wyjaśnienie jest zrozumiałe!  Czy chciałbyś, żebym rozwinął któryś z tych aspektów lub dodał coś więcej?

User: Czy możesz podać przykład zastosowania?
Model: Z przyjemnością! Rozważmy zastosowanie RAG w **Sprzedaży Produktów Oprogramowania (SPO)**.

**Przykład:**

Załóżmy, że firma oferuje oprogramowanie do zarządzania projektami (np. "ProjectWise").  Oferują one szeroki zakres funkcji, dokumentację i wiele innych.  Firmę chce zwiększyć satysfakcję klientów i przyspieszyć proces wsparcia klienta.

**1. Problemy:**

*   **Czasowa reakcja na pytania klientów:**  Klienci często piszą pytania o konkretne funkcje oprogramowania, a odpowiedź jest generowana z poziomu LLM, co potrafi zająć kilka minut, a to jest w przypadku klienta istotne.
*   **Brak spójności w dokumentacji:**  Dokumentacja oprogramowania nie jest spójna, co powoduje trudność w identyfikacji właściwych rozwiązań dla problemów użytkowników.
*   **Trudności w weryfikacji błędów:**  Klienci często zmagają się z tym, by zidentyfikować problem w oprogramowaniu, jeżeli nie mają dostępu do pełnej dokumentacji.

**2. Rozwiązanie - RAG:**

*   **Dane:** Firmę zbiera z różnych źródeł: dokumentacja oprogramowania (specyfikacje, manuala użytkownika, FAQ, forum), archiwalne wsparcie techniczne, blogi, itp.
*   **RAG System:**  RAG system wczytuje te dokumenty i tworzy "baza wiedzy". Gdy klient pisze pytanie, system:
    1.  **Wyszukuje:**  W oparciu o to pytanie, system RAG wyszukuje odpowiednie fragmenty dokumentacji w bazie wiedzy.
    2.  **Wyciąga:**  System RAG wyciąga **relevance** - najważniejsze fragmenty dokumentów, które odpowiadają na to pytanie.
    3.  **Generuje:**  Z tych fragmentów, system generuje użyteczną, spójną odpowiedź dla klienta.  Niezależnie od tego, czy klient szuka informacji o aktualizacji, o specyficznych funkcjach, czy o rozwiązywaniu problemów -  RAG dostarcza odpowiedź.

**3. Zastosowanie Biznesowe:**

*   **Redukcja czasu odpowiedzi:**  Klienci otrzymują odpowiedzi w czasie kilku sekund, co znacznie przyspiesza proces rozwiązywania problemów.
*   **Poprawa satysfakcji klienta:**  Bezpośredniojszność i spójność dokumentacji zadowolają klientów.
*   **Zwiększenie efektywności wsparcia:**  Wsparcie klienta może być skoncentrowane na najistotniejszych problemach, dzięki możliwości szybko odnaleźć odpowiednie dokumenty.
*   **Zwiększenie sprzedaży:**  Umożliwienie użytkownikom szybkiego rozwiązania problemów z pomocą oprogramowania, zwiększa prawdopodobieństwo, że przejdą na płatne oprogramowanie.

**Podsumowanie:** RAG jest tutaj używane do *optymalizacji* procesu obsługi klienta i poprawy wydajności wsparcia.

Czy chcesz, żebym rozwinął któryś z tych aspektów jeszcze bardziej szczegółowo - np. jak to zdefiniować w praktyce, lub jak to jest zautomatyzowane?

###**Wnioski:**
Dodając do roli konkretny format odpowiedzi mamy zagwarantowane jeszcze lepiej dopasowane odpowiedzi. LLM tym razem podał nam zgodnie z promptem - 1) Definicję 2) Przykład 3) Zastosowanie biznesowe. Ustrukturyzował swoją odpowiedź na pierwsze pytanie jak AI Architect.
Drugie pytanie dało nam odpowiedź podzieloną na 1) Problemy - wymienione problemy, które można rozwiązać zastosowaniem LLM 2) Rozwiązanie - RAG - przykład jak można wykorzystać RAG do naszych celów 3) Zastosowanie biznesowe - rezultaty i korzyści biznesowe z nich płynące. 


## Główny wniosek
Im lepiej zdefiniujemy prompt systemowy (nadamy rolę LLMowi, dodamy mu preferowany format odpowiedzi, etc.) tym lepiej dopasowane do naszych potrzeb odpowiedzi otrzymamy.
Dodanie roli zmieniło ton odpowiedzi LLMu. Dodanie dodatkowo formatu, ustrukturyzowało jego odpowiedź i pozwoliło mu się skupić na konkretnym przykładzie.
Bardzo generalny prompt systemowy daje nam lepsze wyniki, jeśli chodzi o zbieranie pomysłów w szerokim kontekście.
Natomiast precyzyjny prompt systemowy pozwala nam na specyficzne rezultaty dopasowane do naszych potrzeb.
