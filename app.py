import streamlit as st
from gtts import gTTS
import os
import random

# 1. CONFIGURATION DE LA PAGE
st.set_page_config(page_title="SanaEnglishPro V2", page_icon="🎓", layout="wide")

# 2. FONCTION AUDIO
def prononcer_anglais(texte):
    try:
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

# 3. BASE DE DONNÉES (200 EXPRESSIONS)
if 'data' not in st.session_state:
    st.session_state.data = [
        # --- VIE QUOTIDIENNE & SALUTATIONS (30) ---
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
        {"en": "Cheers!", "fr": "Santé / Merci / Salut", "ex": "Cheers for the help!"},
        {"en": "Make yourself at home", "fr": "Fais comme chez toi", "ex": "Come in and make yourself at home."},
        {"en": "You're welcome", "fr": "Je vous en prie / De rien", "ex": "Thanks for the gift! - You're welcome."},
        {"en": "I'm on my way", "fr": "Je suis en route", "ex": "Wait for me, I'm on my way."},
        {"en": "Hold on a second", "fr": "Attends une seconde", "ex": "Hold on, I'm on the phone."},
        {"en": "Give me a sec", "fr": "Donne-moi une seconde", "ex": "I'm busy, give me a sec."},
        {"en": "It doesn't matter", "fr": "Ça n'a pas d'importance", "ex": "It doesn't matter if you're late."},
        {"en": "I have no idea", "fr": "Je n'en ai aucune idée", "ex": "Where is he? - I have no idea."},
        {"en": "Can you help me?", "fr": "Peux-tu m'aider ?", "ex": "This is heavy, can you help me?"},
        {"en": "Don't worry about it", "fr": "Ne t'en fais pas pour ça", "ex": "I broke a glass. - Don't worry about it."},
        {"en": "I'm lost", "fr": "Je suis perdu", "ex": "I'm lost, where is the station?"},
        {"en": "Nice to meet you", "fr": "Ravi de vous rencontrer", "ex": "I'm John. - Nice to meet you."},

        # --- TRAVAIL & RÉUNION (40) ---
        {"en": "Get down to business", "fr": "Passons aux choses sérieuses", "ex": "Let's get down to business."},
        {"en": "Keep me posted", "fr": "Tiens-moi au courant", "ex": "Keep me posted on the situation."},
        {"en": "In a nutshell", "fr": "En résumé", "ex": "In a nutshell, we are losing money."},
        {"en": "Think out of the box", "fr": "Penser différemment", "ex": "We need to think out of the box."},
        {"en": "Call it a day", "fr": "Finir sa journée", "ex": "It’s 6 PM, let’s call it a day."},
        {"en": "Work from home (WFH)", "fr": "Télétravail", "ex": "I work from home on Fridays."},
        {"en": "To be on the same page", "fr": "Être sur la même longueur d'onde", "ex": "We need to be on the same page."},
        {"en": "Back to square one", "fr": "Retour à la case départ", "ex": "The plan failed, back to square one."},
        {"en": "Win-win situation", "fr": "Situation gagnant-gagnant", "ex": "It's a win-win situation for us."},
        {"en": "Under the weather", "fr": "Un peu malade", "ex": "I'm feeling a bit under the weather today."},
        {"en": "Piece of cake", "fr": "C'est du gâteau / Très facile", "ex": "That exam was a piece of cake."},
        {"en": "The bottom line", "fr": "L'essentiel / Le résultat net", "ex": "The bottom line is we need more users."},
        {"en": "To meet a deadline", "fr": "Respecter une échéance", "ex": "We must meet the deadline."},
        {"en": "To schedule a meeting", "fr": "Planifier une réunion", "ex": "Can we schedule a meeting for Monday?"},
        {"en": "To follow up", "fr": "Faire un suivi", "ex": "I'll follow up with you tomorrow."},
        {"en": "As far as I'm concerned", "fr": "En ce qui me concerne", "ex": "As far as I'm concerned, it's a good plan."},
        {"en": "In the meantime", "fr": "En attendant", "ex": "Wait here, I'll be back in the meantime."},
        {"en": "I'm overwhelmed", "fr": "Je suis débordé", "ex": "I have too much work, I'm overwhelmed."},
        {"en": "Let's touch base", "fr": "Reprenons contact", "ex": "Let's touch base next week."},
        {"en": "I'll get back to you", "fr": "Je reviendrai vers vous", "ex": "I'll check and get back to you."},
        {"en": "It's a priority", "fr": "C'est une priorité", "ex": "This bug is a priority."},
        {"en": "Can we move on?", "fr": "Pouvons-nous avancer ?", "ex": "Enough about that, can we move on?"},
        {"en": "To summarize", "fr": "Pour résumer", "ex": "To summarize, the project is on track."},
        {"en": "I agree with you", "fr": "Je suis d'accord avec vous", "ex": "I agree with you on this point."},
        {"en": "I don't think so", "fr": "Je ne pense pas", "ex": "Is it easy? - I don't think so."},
        {"en": "That's a good point", "fr": "C'est un bon point", "ex": "You're right, that's a good point."},
        {"en": "Let's wrap it up", "fr": "Finissons-en / Concluons", "ex": "It's late, let's wrap it up."},
        {"en": "What do you think?", "fr": "Qu'en penses-tu ?", "ex": "I like it, what do you think?"},
        {"en": "Any questions?", "fr": "Des questions ?", "ex": "That's all, any questions?"},
        {"en": "To postpone", "fr": "Reporter", "ex": "The meeting is postponed to Friday."},
        {"en": "To cancel", "fr": "Annuler", "ex": "They cancelled the flight."},
        {"en": "Keep up the good work", "fr": "Continue ton bon travail", "ex": "Great results, keep up the good work!"},
        {"en": "To take care of", "fr": "S'occuper de", "ex": "I'll take care of the report."},
        {"en": "I'm in charge of...", "fr": "Je suis responsable de...", "ex": "I'm in charge of maintenance."},
        {"en": "To troubleshoot", "fr": "Dépanner / Résoudre", "ex": "I need to troubleshoot this site."},
        {"en": "Site audit", "fr": "Audit de site", "ex": "We are conducting a site audit."},
        {"en": "Power failure", "fr": "Panne d'électricité", "ex": "There is a power failure at site X."},
        {"en": "To alignment antennas", "fr": "Aligner les antennes", "ex": "You need to align the antennas properly."},
        {"en": "Microwave link", "fr": "Lien hertzien", "ex": "The microwave link is down."},
        {"en": "To perform a test", "fr": "Effectuer un test", "ex": "Let's perform a loop test."},

        # --- EMAILS & RÉDACTION (20) ---
        {"en": "I hope this email finds you well", "fr": "J'espère que vous allez bien", "ex": "Dear Eric, I hope this email finds you well."},
        {"en": "Further to our conversation...", "fr": "Suite à notre conversation...", "ex": "Further to our conversation this morning..."},
        {"en": "Please find attached", "fr": "Veuillez trouver ci-joint", "ex": "Please find attached the report."},
        {"en": "Could you please clarify...?", "fr": "Pourriez-vous clarifier... ?", "ex": "Could you please clarify what you mean by that?"},
        {"en": "I look forward to hearing from you", "fr": "Dans l'attente de votre réponse", "ex": "I look forward to hearing from you soon."},
        {"en": "Best regards", "fr": "Cordialement", "ex": "Best regards, Rosly."},
        {"en": "Thank you for your prompt reply", "fr": "Merci pour votre réponse rapide", "ex": "Got it, thank you for your prompt reply."},
        {"en": "To whom it may concern", "fr": "À qui de droit", "ex": "To whom it may concern, I am writing to..."},
        {"en": "I am writing to inform you", "fr": "Je vous écris pour vous informer", "ex": "I am writing to inform you about the site status."},
        {"en": "Feel free to contact me", "fr": "N'hésitez pas à me contacter", "ex": "Feel free to contact me if you need help."},
        {"en": "Thank you for your cooperation", "fr": "Merci pour votre coopération", "ex": "We fixed the issue. Thank you for your cooperation."},
        {"en": "Regarding your request", "fr": "Concernant votre demande", "ex": "Regarding your request, here is the file."},
        {"en": "In response to your email", "fr": "En réponse à votre email", "ex": "In response to your email dated April 1st..."},
        {"en": "Sorry for the delay", "fr": "Désolé pour le retard", "ex": "Sorry for the delay in getting back to you."},
        {"en": "Please let me know", "fr": "S'il vous plaît faites-moi savoir", "ex": "Please let me know your thoughts."},
        {"en": "I am pleased to confirm", "fr": "J'ai le plaisir de confirmer", "ex": "I am pleased to confirm our meeting."},
        {"en": "It's my pleasure", "fr": "C'est un plaisir", "ex": "Thanks for the help! - It's my pleasure."},
        {"en": "I would appreciate it if...", "fr": "J'apprécierais que...", "ex": "I would appreciate it if you could call me."},
        {"en": "Just a quick reminder", "fr": "Juste un petit rappel", "ex": "Just a quick reminder about the report."},
        {"en": "Yours sincerely", "fr": "Sincèrement vôtre", "ex": "Yours sincerely, Rosly."},

        # --- PHRASES IDIOMATIQUES & EXPRESSIONS (50) ---
        {"en": "Bite the bullet", "fr": "Prendre son courage à deux mains", "ex": "I have to bite the bullet and see the dentist."},
        {"en": "Out of the blue", "fr": "À l'improviste", "ex": "He called me out of the blue."},
        {"en": "Hit the sack", "fr": "Aller se coucher", "ex": "I'm tired, I'm going to hit the sack."},
        {"en": "It's not rocket science", "fr": "C'est pas sorcier", "ex": "Using this app is not rocket science."},
        {"en": "Break the ice", "fr": "Briser la glace", "ex": "He told a joke to break the ice."},
        {"en": "Cost an arm and a leg", "fr": "Coûter les yeux de la tête", "ex": "This car cost an arm and a leg."},
        {"en": "A piece of cake", "fr": "Un jeu d'enfant", "ex": "The test was a piece of cake."},
        {"en": "Under the weather", "fr": "Pas dans son assiette", "ex": "I'm feeling a bit under the weather."},
        {"en": "Kill two birds with one stone", "fr": "Faire d'une pierre deux coups", "ex": "I'll go to the bank and the store, killing two birds with one stone."},
        {"en": "Once in a blue moon", "fr": "Tous les 36 du mois", "ex": "I go to the cinema once in a blue moon."},
        {"en": "The best of both worlds", "fr": "Le meilleur des deux mondes", "ex": "Working from home gives me the best of both worlds."},
        {"en": "Spill the beans", "fr": "Vendre la mèche", "ex": "Don't spill the beans about the surprise party."},
        {"en": "Take it with a grain of salt", "fr": "Prendre avec des pincettes", "ex": "Take his advice with a grain of salt."},
        {"en": "Cry over spilled milk", "fr": "Pleurer sur le lait renversé", "ex": "It's done, don't cry over spilled milk."},
        {"en": "Blessing in disguise", "fr": "Un mal pour un bien", "ex": "Losing that job was a blessing in disguise."},
        {"en": "Beat around the bush", "fr": "Tourner autour du pot", "ex": "Stop beating around the bush and tell me the truth."},
        {"en": "Better late than never", "fr": "Mieux vaut tard que jamais", "ex": "You're late! - Better late than never."},
        {"en": "Call it a day", "fr": "S'arrêter là pour aujourd'hui", "ex": "We're tired, let's call it a day."},
        {"en": "Cut somebody some slack", "fr": "Être indulgent avec quelqu'un", "ex": "He's new, cut him some slack."},
        {"en": "Cutting corners", "fr": "Faire les choses à la va-vite", "ex": "Don't cut corners on safety."},
        {"en": "Easy does it", "fr": "Doucement", "ex": "Easy does it, the glass is fragile."},
        {"en": "Get out of hand", "fr": "Dégénérer", "ex": "The party got out of hand."},
        {"en": "Get something out of your system", "fr": "Se défouler / Évacuer quelque chose", "ex": "I needed to cry to get it out of my system."},
        {"en": "Get your act together", "fr": "Se ressaisir / S'organiser", "en": "You're failing, get your act together."},
        {"en": "Give someone the benefit of the doubt", "fr": "Accorder le bénéfice du doute", "ex": "I don't believe him, but I'll give him the benefit of the doubt."},
        {"en": "Go back to the drawing board", "fr": "Repartir de zéro", "ex": "It failed, let's go back to the drawing board."},
        {"en": "Hang in there", "fr": "Tiens bon", "ex": "I know it's hard, but hang in there."},
        {"en": "Hit the nail on the head", "fr": "Mettre le doigt sur le problème / Voir juste", "ex": "You hit the nail on the head with that analysis."},
        {"en": "Ignorance is bliss", "fr": "L'ignorance est une bénédiction", "ex": "I didn't know the calories. Ignorance is bliss."},
        {"en": "It's the last straw", "fr": "C'est la goutte d'eau qui fait déborder le vase", "ex": "He's late again! This is the last straw."},
        {"en": "Let someone off the hook", "fr": "Sortir quelqu'un d'affaire / Laisser filer", "ex": "I'll let you off the hook this time."},
        {"en": "Make a long story short", "fr": "Pour faire court", "ex": "To make a long story short, we won."},
        {"en": "Miss the boat", "fr": "Rater le coche", "ex": "The sale ended, I missed the boat."},
        {"en": "No pain, no gain", "fr": "On n'a rien sans rien", "ex": "Keep training! No pain, no gain."},
        {"en": "On the ball", "fr": "Être réactif / Dégourdi", "ex": "She's really on the ball at work."},
        {"en": "Pull someone's leg", "fr": "Mener quelqu'un en bateau / Faire une blague", "ex": "Are you serious? - No, I'm pulling your leg."},
        {"en": "Pull yourself together", "fr": "Reprends-toi", "ex": "Stop crying and pull yourself together."},
        {"en": "So far so good", "fr": "Jusqu'ici tout va bien", "ex": "The project is moving, so far so good."},
        {"en": "Speak of the devil", "fr": "Quand on parle du loup", "ex": "Hi John! Speak of the devil, we were just talking about you."},
        {"en": "That's the last straw", "fr": "C'en est trop", "ex": "I'm quitting, that's the last straw."},
        {"en": "The elephant in the room", "fr": "Le sujet tabou", "ex": "We need to talk about the budget, it's the elephant in the room."},
        {"en": "Through thick and thin", "fr": "Contre vents et marées", "ex": "They stayed together through thick and thin."},
        {"en": "Time flies", "fr": "Le temps passe vite", "ex": "Look at the time! Time flies."},
        {"en": "To get bent out of shape", "fr": "Se mettre dans tous ses états", "ex": "Don't get bent out of shape over a small mistake."},
        {"en": "To make matters worse", "fr": "Pour ne rien arranger / Empirer les choses", "ex": "It rained, and to make matters worse, I lost my keys."},
        {"en": "Under the weather", "fr": "Un peu souffrant", "ex": "I'm not coming, I'm under the weather."},
        {"en": "We'll cross that bridge when we come to it", "fr": "On verra le moment venu", "ex": "Don't worry about the future, we'll cross that bridge..."},
        {"en": "Wrap your head around something", "fr": "Arriver à comprendre quelque chose de complexe", "ex": "I can't wrap my head around this new software."},
        {"en": "You can say that again", "fr": "Tu l'as dit / Je suis tout à fait d'accord", "ex": "It's hot today! - You can say that again."},
        {"en": "Your guess is as good as mine", "fr": "Je n'en sais pas plus que toi", "ex": "When will it start? - Your guess is as good as mine."},

        # --- VERBES IRRÉGULIERS & UTILES (60) ---
        {"en": "To bear (bore/borne)", "fr": "Supporter / Porter", "ex": "I can't bear this noise."},
        {"en": "To beat (beat/beaten)", "fr": "Battre", "ex": "Our team beat theirs."},
        {"en": "To become (became/become)", "fr": "Devenir", "ex": "He became a doctor."},
        {"en": "To begin (began/begun)", "fr": "Commencer", "ex": "Let's begin the meeting."},
        {"en": "To bend (bent/bent)", "fr": "Plier", "ex": "Bend your knees."},
        {"en": "To bet (bet/bet)", "fr": "Parier", "ex": "I bet he will be late."},
        {"en": "To bite (bit/bitten)", "fr": "Mordre", "ex": "The dog bit me."},
        {"en": "To bleed (bled/bled)", "fr": "Saigner", "ex": "Your finger is bleeding."},
        {"en": "To blow (blew/blown)", "fr": "Souffler", "ex": "The wind blew hard."},
        {"en": "To break (broke/broken)", "fr": "Casser", "ex": "I broke my glasses."},
        {"en": "To bring (brought/brought)", "fr": "Apporter", "ex": "Bring me the report."},
        {"en": "To build (built/built)", "fr": "Construire", "ex": "They built a new site."},
        {"en": "To burn (burnt/burnt)", "fr": "Brûler", "ex": "The wires burnt out."},
        {"en": "To buy (bought/bought)", "fr": "Acheter", "ex": "I bought a new SFP module."},
        {"en": "To catch (caught/caught)", "fr": "Attraper", "ex": "Catch the ball!"},
        {"en": "To choose (chose/chosen)", "fr": "Choisir", "ex": "Choose a color."},
        {"en": "To come (came/come)", "fr": "Venir", "ex": "Come here please."},
        {"en": "To cost (cost/cost)", "fr": "Coûter", "ex": "How much does it cost?"},
        {"en": "To cut (cut/cut)", "fr": "Couper", "ex": "Cut the power."},
        {"en": "To dig (dug/dug)", "fr": "Creuser", "ex": "They are digging a trench."},
        {"en": "To do (did/done)", "fr": "Faire", "ex": "I did my homework."},
        {"en": "To draw (drew/drawn)", "fr": "Dessiner", "ex": "Draw a diagram."},
        {"en": "To dream (dreamt/dreamt)", "fr": "Rêver", "ex": "I dreamt about work."},
        {"en": "To drink (drank/drunk)", "fr": "Boire", "ex": "Drink some water."},
        {"en": "To drive (drove/driven)", "fr": "Conduire", "ex": "I drive to the site."},
        {"en": "To eat (ate/eaten)", "fr": "Manger", "ex": "Have you eaten?"},
        {"en": "To fall (fell/fallen)", "fr": "Tomber", "ex": "The antenna fell."},
        {"en": "To feed (fed/fed)", "fr": "Nourrir", "ex": "Feed the dog."},
        {"en": "To feel (felt/felt)", "fr": "Ressentir", "ex": "I feel tired."},
        {"en": "To fight (fought/fought)", "fr": "Se battre", "ex": "They fought for the contract."},
        {"en": "To find (found/found)", "fr": "Trouver", "ex": "I found the fault."},
        {"en": "To fly (flew/flown)", "fr": "Voler (air)", "ex": "The bird flew away."},
        {"en": "To forbid (forbade/forbidden)", "fr": "Interdire", "ex": "Access is forbidden."},
        {"en": "To forget (forgot/forgotten)", "fr": "Oublier", "ex": "Don't forget the keys."},
        {"en": "To forgive (forgave/forgiven)", "fr": "Pardonner", "ex": "Forgive me."},
        {"en": "To freeze (froze/frozen)", "fr": "Geler", "ex": "The screen is frozen."},
        {"en": "To get (got/got)", "fr": "Obtenir / Devenir", "ex": "I got the message."},
        {"en": "To give (gave/given)", "fr": "Donner", "ex": "Give me a hand."},
        {"en": "To go (went/gone)", "fr": "Aller", "ex": "I went to the office."},
        {"en": "To grow (grew/grown)", "fr": "Grandir", "ex": "The company is growing."},
        {"en": "To hang (hung/hung)", "fr": "Pendre / Suspendre", "ex": "Hang the tool here."},
        {"en": "To have (had/had)", "fr": "Avoir", "ex": "I have a meeting."},
        {"en": "To hear (heard/heard)", "fr": "Entendre", "ex": "Can you hear me?"},
        {"en": "To hide (hid/hidden)", "fr": "Cacher", "ex": "Hide the cables."},
        {"en": "To hit (hit/hit)", "fr": "Frapper / Atteindre", "ex": "Hit the button."},
        {"en": "To hold (held/held)", "fr": "Tenir", "ex": "Hold this please."},
        {"en": "To hurt (hurt/hurt)", "fr": "Blesser", "ex": "My back hurts."},
        {"en": "To keep (kept/kept)", "fr": "Garder", "ex": "Keep the change."},
        {"en": "To know (knew/known)", "fr": "Savoir", "ex": "I know the answer."},
        {"en": "To lay (laid/laid)", "fr": "Poser à plat", "ex": "Lay the ladder down."},
        {"en": "To lead (led/led)", "fr": "Mener / Diriger", "ex": "He leads the team."},
        {"en": "To learn (learnt/learnt)", "fr": "Apprendre", "ex": "I am learning English."},
        {"en": "To leave (left/left)", "fr": "Partir / Quitter", "ex": "I am leaving now."},
        {"en": "To lend (lent/lent)", "fr": "Prêter", "ex": "Can you lend me a pen?"},
        {"en": "To let (let/let)", "fr": "Laisser", "ex": "Let me see."},
        {"en": "To lie (lay/lain)", "fr": "S'allonger", "ex": "Lie down on the floor."},
        {"en": "To light (lit/lit)", "fr": "Allumer", "ex": "Light the lamp."},
        {"en": "To lose (lost/lost)", "fr": "Perdre", "ex": "I lost my phone."},
        {"en": "To make (made/made)", "fr": "Faire / Fabriquer", "ex": "I made a mistake."},
        {"en": "To mean (meant/meant)", "fr": "Signifier", "ex": "What does it mean?"}
    ]

# 4. INTERFACE UTILISATEUR
st.title("🎓 SanaEnglishPro V2 (200+)")
st.sidebar.title("📚 Menu")
st.sidebar.write(f"✅ Base de données : **{len(st.session_state.data)}** phrases")

menu = st.sidebar.selectbox("Choisir une section", ["Flashcards", "Dictionnaire", "Objectif & Stats"])

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
    st.subheader("📚 Bibliothèque Complète")
    search = st.text_input("Rechercher un mot ou une expression...")
    
    results = [i for i in st.session_state.data if search.lower() in i['en'].lower() or search.lower() in i['fr'].lower()]
    
    st.write(f"Résultats trouvés : {len(results)}")
    
    for r in results:
        with st.expander(f"🇬🇧 {r['en']}"):
            st.write(f"**🇫🇷 Traduction :** {r['fr']}")
            st.write(f"**💡 Exemple :** {r['ex']}")
            if st.button(f"🔊 Prononcer", key=f"btn_{r['en']}"):
                prononcer_anglais(r['en'])

else:
    st.subheader("ℹ️ À propos & Objectifs")
    st.write(f"Félicitations Rosly ! Ton application contient maintenant **{len(st.session_state.data)}** expressions professionnelles.")
    
    progression = len(st.session_state.data) / 200
    st.progress(min(progression, 1.0))
    
    st.write("### Prochaines étapes :")
    st.write("1. Pratique tes flashcards 10 minutes par jour.")
    st.write("2. Utilise le dictionnaire pour tes rapports techniques.")
    st.write("3. Écoute la prononciation avant tes réunions avec Eric.")
    
    st.balloons()
