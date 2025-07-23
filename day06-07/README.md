Harika iş çıkardın Rabia! 🎉
Bu kod için sana sade, açıklayıcı bir `README.md` taslağı hazırladım:

---

## 🕹️ Hangman Oyunu (Adam Asmaca)

Bu Python projesi, klasik bir **kelime tahmin oyunu**dur. Oyuncu, gizli bir kelimeyi harf harf tahmin eder ve her yanlış tahmin bir can kaybettirir. 6 yanlışta oyun biter.

---

### 🚀 Özellikler

* Rastgele kelime seçimi (`random.choice`)
* Oyuncuya kalan canları gösterme
* Harf tekrar kontrolü
* Doğru tahminleri yerinde gösterme
* ASCII sanatıyla görsel destek (`hangman_art`)
* Oyun kazanma/kaybetme bildirimi

---

### 📁 Dosya Yapısı

* `main.py` → Oyun mantığı
* `hangman_words.py` → Kelime listesi (`word_list`)
* `hangman_art.py` → Oyun görselleri (`logo`, `stages`)

---

### 🧠 Nasıl Çalışır?

1. Oyun başlarken `logo` yazdırılır.
2. `word_list` içinden rastgele bir kelime seçilir.
3. Oyuncuya "\_" ile gizlenmiş kelime gösterilir.
4. Oyuncu harf tahmin eder:

   * Doğruysa → harf yerleştirilir
   * Yanlışsa → 1 can kaybedilir
5. Tüm harfler bulunursa oyuncu kazanır 🎉
6. 6 yanlışta oyuncu kaybeder 💀

---

### 🧩 Kullanılan Yapılar

* `while not game_over:` → Oyun bitene kadar döngü
* `if guess in correct_letters:` → Tekrar tahmini engelleme
* `lives -= 1` → Yanlış tahminle can azaltma
* `display` → Güncel kelime görünümü

---

### 🎨 Görseller

ASCII ile oyun evreleri (`stages`) her can kaybında ekrana basılır:

```
+---+
|   |
O   |
/|\  |
/ \  |
    ===
```

---

Eğer bunu GitHub’a koymak istersen, bu README dosyasını direkt olarak kullanabilirsin!
İstersen `.md` dosyası olarak da sana hazırlayabilirim. Hazır olayım mı? 💪
