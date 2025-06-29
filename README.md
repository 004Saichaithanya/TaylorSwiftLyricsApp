# 🎶 Taylor Swift Lyrics & Word Cloud Generator 🎶

An interactive Streamlit web app that lets you enter the title of a Taylor Swift song, fetches the lyrics link from the Genius API, and generates a visually appealing word cloud based on sample lyrics.

---

## 📌 Project Overview

This project combines APIs, data visualization, and web app development using **Python and Streamlit**.  
Due to copyright restrictions from Genius, the API provides only a link to the lyrics page. The app uses a placeholder text for the word cloud generation as a demonstration.

---

## 📖 Approach

1. **User inputs a Taylor Swift song title**
2. The app uses the **Genius API** to search for the song and fetch its lyrics page link.
3. Displays the Genius lyrics page link to the user.
4. Generates a **Word Cloud** from a simulated sample lyrics text.
5. Displays the word cloud image using **Matplotlib**.

---

## 📦 Dependencies

The following Python libraries are required:

- `streamlit`
- `requests`
- `wordcloud`
- `matplotlib`
- `python-dotenv`

---

## ⚙️ How to Run Locally

1️⃣ **Clone this repository**

```bash
git clone https://github.com/yourusername/TaylorSwiftLyricsApp.git
cd TaylorSwiftLyricsApp
````

2️⃣ **Create a virtual environment (optional but recommended)**

```bash
python -m venv env
source env/bin/activate   # On Mac/Linux
env\Scripts\activate      # On Windows
```

3️⃣ **Install the dependencies**

```bash
pip install -r requirements.txt
```

4️⃣ **Set your Genius API Token**

* Create a `.env` file in the project root.
* Add your token like this:

```
GENIUS_ACCESS_TOKEN=your_actual_token_here
```

5️⃣ **Run the Streamlit app**

```bash
streamlit run app.py
```

---

## 🚀 Deploy on Streamlit Cloud

1. Push your code to a GitHub repository.
2. Go to [Streamlit Community Cloud](https://streamlit.io/cloud) and sign in with GitHub.
3. Click **‘New app’** and connect your repo.
4. In **App settings**, under **Secrets**, add:

```
GENIUS_ACCESS_TOKEN = "your_actual_token_here"
```

5. Deploy and share your app link!

---

## 📌 Example Song Titles to Try

* `Love Story`
* `Blank Space`
* `Shake It Off`
* `You Belong With Me`
* `Enchanted`
* `Cruel Summer`

---

## 📸 Sample Screenshot

![image](https://github.com/user-attachments/assets/8f6136b6-09f3-4d1e-b017-5ed9ab82052e)


---

## 📚 License

This project is intended for educational and personal use only.
Genius API terms prohibit distributing or storing full lyrics content.

---

## ⭐ Author

**Sai Chaithanya Poloju**

---

```

---

