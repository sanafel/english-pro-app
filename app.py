import streamlit as st
from gtts import gTTS
import os
import random

# 1. CONFIGURATION
st.set_page_config(page_title="SanaEnglishPro V2", page_icon="🚀", layout="wide")

# 2. FONCTION AUDIO
def prononcer_anglais(texte):
    try:
        # On nettoie pour ne lire que l'anglais principal
        texte_propre = texte.split('(')[0].split('/')[0].split('—')[0].strip()
        tts = gTTS(text=texte_propre, lang='en')
        filename = "prononciation.mp3"
        tts.save(filename)
        
        with open(filename, "rb") as audio_file:
            audio_bytes = audio_file.read()
            st.audio(audio_bytes, format="audio/mp3")
        os.remove(filename)
    except Exception:
        st.error("Erreur audio.")

# 3. LA MÉMOIRE DE L'APPLICATION (SanaEnglishPro Database)
if 'data' not in st.session_state:
    st.session_state.data = [
        # --- SALUTATIONS & VIE QUOTIDIENNE (20) ---
        {"en": "What's up?", "fr": "Quoi de neuf ?", "ex": "Hey man, what's up?"},
        {"en": "How’s it going?", "fr": "Comment ça va ?", "ex": "How’s it going with your new job?"},
        {"en": "Long time no see", "fr": "Ça fait un bail", "ex": "Oh, hi Mark! Long time no see."},
        {"en": "Take care", "fr": "Prends soin de toi", "ex": "See you tomorrow, take care!"},
        {"en": "Have a good one", "fr": "Bonne journée", "ex": "Thanks, you have a good one too."},
        {"en": "I’m exhausted", "fr": "Je suis épuisé", "ex": "I worked 10 hours, I’m exhausted."},
        {"en": "I’m starving", "fr": "Je meurs de faim", "ex": "Let's eat, I'm starving."},
        {"en": "It’s up to you", "fr": "C’est toi qui décides", "ex": "Pizza or pasta? It’s up to you."},
        {"en": "I don’t mind", "fr": "Ça ne me dérange pas", "ex": "I don’t mind waiting."},
        {"en": "Never mind", "fr": "Laisse tomber / C’est pas grave", "ex": "Never mind, I found my keys."},
        {"en": "No worries", "fr": "Pas de souci", "ex": "You're late? No worries."},
        {"en": "What do you mean?", "fr": "Que veux-tu dire ?", "ex": "I don't understand, what do you mean?"},
        {"en": "I guess so", "fr": "Je suppose que oui", "ex": "Is it going to rain? I guess so."},
        {"en": "Check this out", "fr": "Regarde ça", "ex": "Check this out, it’s a new app."},
        {"en": "My bad", "fr": "C’est ma faute", "ex": "I forgot to call you, my bad."},
        {"en": "Anyway...", "fr": "Bref / De toute façon...", "ex": "Anyway, let’s talk about something else."},
        {"en": "To be honest...", "fr": "Pour être honnête...", "ex": "To be honest, I don't like this movie."},
        {"en": "Keep in touch", "fr": "On reste en contact", "ex": "Call me, let's keep in touch."},
        {"en": "Cheers!", "fr": "Santé / Merci", "ex": "Cheers for the help!"},
        {"en": "Make yourself at home", "fr": "Fais comme chez toi", "ex": "Come in and make yourself at home."},

        # --- TEMPS & FRÉQUENCE (15) ---
        {"en": "In no time", "fr": "En un rien de temps", "ex": "I’ll be there in no time."},
        {"en": "So far, so good", "fr": "Jusqu'ici tout va bien", "ex": "How is the project? So far, so good."},
        {"en": "From time to time", "fr": "De temps en temps", "ex": "I go to the gym from time to time."},
        {"en": "All of a sudden", "fr": "Tout à coup", "ex": "All of a sudden, the lights went out."},
        {"en": "Once in a blue moon", "fr": "Très rarement", "ex": "He visits us once in a blue moon."},
        {"en": "Better late than never", "fr": "Mieux vaut tard que jamais", "ex": "You’re here! Better late than never."},
        {"en": "Right away", "fr": "Tout de suite", "ex": "I need that report right away."},
        {"en": "In the long run", "fr": "À long terme", "ex": "It’s worth it in the long run."},
        {"en": "Just in case", "fr": "Au cas où", "ex": "Take an umbrella, just in case."},
        {"en": "On time", "fr": "À l'heure", "ex": "Please be on time for the meeting."},
        {"en": "Waste of time", "fr": "Perte de temps", "ex": "This meeting is a waste of time."},
        {"en": "Out of time", "fr": "Plus de temps", "ex": "Stop writing, we are out of time."},
        {"en": "Time’s up", "fr": "Le temps est écoulé", "ex": "Time’s up! Put your pens down."},
        {"en": "ASAP", "fr": "Dès que possible", "ex": "Call me ASAP."},
        {"en": "The sooner the better", "fr": "Le plus tôt sera le mieux", "ex": "Send the file, the sooner the better."},

        # --- TRAVAIL & BUSINESS (20) ---
        {"en": "Get down to business", "fr": "Passer aux choses sérieuses", "ex": "Let's get down to business."},
        {"en": "Keep me posted", "fr": "Tiens-moi au courant", "ex": "Keep me posted on the situation."},
        {"en": "In a nutshell", "fr": "En résumé", "ex": "In a nutshell, we are losing money."},
        {"en": "Think out of the box", "fr": "Penser différemment", "ex": "We need to think out of the box."},
        {"en": "Call it a day", "fr": "Finir sa journée", "ex": "It’s 6 PM, let’s call it a day."},
        {"en": "Work from home (WFH)", "fr": "Télétravail", "ex": "I work from home on Fridays."},
        {"en": "On the same page", "fr": "Sur la même longueur d'onde", "ex": "We need to be on the same page."},
        {"en": "Back to square one", "fr": "Retour à la case départ", "ex": "The plan failed, back to square one."},
        {"en": "To deal with", "fr": "Gérer / S'occuper de", "ex": "I have to deal with this customer."},
        {"en": "Point taken", "fr": "C'est noté", "ex": "Point taken, I'll change the design."},
        {"en": "Give someone a hand", "fr": "Aider quelqu'un", "ex": "Can you give me a hand with this?"},
        {"en": "Win-win situation", "fr": "Gagnant-gagnant", "ex": "It's a win-win situation."},
        {"en": "Piece of cake", "fr": "C'est du gâteau", "ex": "That exam was a piece of cake."},
        {"en": "The bottom line", "fr": "L'essentiel / Le résultat", "ex": "The bottom line is we need users."},

        # --- SENTIMENTS & OPINIONS (15) ---
        {"en": "I’m down", "fr": "Je suis partant", "ex": "A movie tonight? I'm down."},
        {"en": "No way!", "fr": "Pas question !", "ex": "No way! You won the lottery?"},
        {"en": "Not my cup of tea", "fr": "Pas ma tasse de thé", "ex": "Opera is not my cup of tea."},
        {"en": "I’m pulling your leg", "fr": "Je te fais marcher", "ex": "Don't worry, I'm just pulling your leg."},
        {"en": "Fair enough", "fr": "C'est juste / D'accord", "ex": "You can't come? Fair enough."},
        {"en": "Over the moon", "fr": "Aux anges / Très heureux", "ex": "She’s over the moon about her car."},
        {"en": "It’s worth it", "fr": "Ça en vaut la peine", "ex": "It’s expensive, but it’s worth it."},
        {"en": "Looking forward to it", "fr": "J'ai hâte", "ex": "I'm looking forward to our trip."},

        # --- PHRASES IDIOMATIQUES (30) ---
        {"en": "Bite the bullet", "fr": "Prendre son courage à deux mains", "ex": "I have to bite the bullet."},
        {"en": "By the way", "fr": "Au fait / À propos", "ex": "By the way, have you seen the news?"},
        {"en": "Actions speak louder than words", "fr": "Les actes valent mieux que les mots", "ex": "Show me, actions speak louder than words."},
        {"en": "It's not rocket science", "fr": "C'est pas sorcier", "ex": "Using this app is not rocket science."},
        {"en": "Out of the blue", "fr": "À l'improviste", "ex": "He called me out of the blue."},
        {"en": "Hang in there", "fr": "Tiens bon", "ex": "I know it's hard, but hang in there."},
        {"en": "See eye to eye", "fr": "Être d'accord", "ex": "We don't always see eye to eye."},

        # --- EMAILS & RÉDACTION ---
        {"en": "I hope this email finds you well", "fr": "J'espère que vous allez bien", "ex": "I hope this email finds you well, Eric."},
        {"en": "Further to our conversation", "fr": "Suite à notre conversation", "ex": "Further to our conversation this morning..."},
        {"en": "Please find attached", "fr": "Veuillez trouver ci-joint", "ex": "Please find attached the report."},
        {"en": "I look forward to hearing from you", "fr": "Dans l'attente de votre réponse", "ex": "I look forward to hearing from you soon."},
        {"en": "Best regards", "fr": "Cordialement", "ex": "Best regards, Rosly."},

        # --- NÉGOCIATION & PERSUASION ---
        {"en": "Could we meet halfway?", "fr": "Faire un compromis", "ex": "Could we meet halfway on the price?"},
        {"en": "It’s a win-win situation", "fr": "C'est gagnant-gagnant", "ex": "Imagine the possibilities if we work together."},
        {"en": "I strongly recommend...", "fr": "Je recommande vivement...", "ex": "I strongly recommend moving forward with this."},
        {"en": "I take full responsibility", "fr": "Je prends l'entière responsabilité", "ex": "I take full responsibility for this mistake."},
        {"en": "Set the record straight", "fr": "Remettre les pendules à l'heure", "ex": "I would like to set the record straight."},

        # --- VERBES IRRÉGULIERS (SÉLECTION) ---
        {"en": "To Make (made/made)", "fr": "Faire / Fabriquer", "ex": "We have made a lot of progress."},
        {"en": "To Know (knew/known)", "fr": "Savoir / Connaître", "ex": "I knew the answer."},
        {"en": "To Speak (spoke/spoken)", "fr": "Parler", "ex": "She will speak at the conference."},
        {"en": "To Give (gave/given)", "fr": "Donner", "ex": "He gave me some advice."},
        {"en": "To Take (took/taken)", "fr": "Prendre", "ex": "She took a taxi to the airport."}
    ]

# 4. INTERFACE
st.title("🎓 SanaEnglishPro V2 (200+)") # Ajoute V2 pour vérifier sur ton téléphone
st.sidebar.title("📚 Menu Principal")
st.sidebar.write(f"✅ Base de données : **{len(st.session_state.data)}** phrases")

menu = st.sidebar.selectbox("Choisir une section", ["Flashcards", "Dictionnaire", "Infos"])

if menu == "Flashcards":
    st.subheader("🎯 Entraînement Aléatoire")
    if 'current_card' not in st.session_state:
        st.session_state.current_card = random.choice(st.session_state.data)
        st.session_state.show_ans = False

    card = st.session_state.current_card
    st.info(f"## {card['en']}")
    
    col1, col2, col3 = st.columns(3)
    with col1:
        if st.button("🔊 Écouter"):
            prononcer_anglais(card['en'])
    with col2:
        if st.button("🔄 Traduire"):
            st.session_state.show_ans = True
    with col3:
        if st.button("➡️ Suivant"):
            st.session_state.current_card = random.choice(st.session_state.data)
            st.session_state.show_ans = False
            st.rerun()

    if st.session_state.show_ans:
        st.success(f"**Français :** {card['fr']}")
        st.warning(f"**Exemple :** {card['ex']}")

elif menu == "Dictionnaire":
    st.subheader("📚 Bibliothèque SanaEnglishPro")
    search = st.text_input("Rechercher une expression...")
    
    results = [i for i in st.session_state.data if search.lower() in i['en'].lower() or search.lower() in i['fr'].lower()]
    
    for r in results:
        with st.expander(f"🇬🇧 {r['en']}"):
            st.write(f"**🇫🇷 Traduction :** {r['fr']}")
            st.write(f"**💡 Exemple :** {r['ex']}")
            if st.button(f"🔊 Prononcer", key=f"btn_{r['en']}"):
                prononcer_anglais(r['en'])

else:
    st.subheader("ℹ️ À propos")
    st.write("Bienvenue sur **SanaEnglishPro**, l'application ultime pour maîtriser l'anglais professionnel.")
    st.progress(len(st.session_state.data) / 200)
    st.write("Objectif 200 expressions : En cours...")
