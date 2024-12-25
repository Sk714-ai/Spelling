import streamlit as st
import random

# Define English and Arabic word lists
word_lists = {
    "English": {
        "Grade1": [
    "adventure", "black", "brown", "butterfly", "carpet", "cereal", 
    "elephant", "flower", "game", "grapes", "green", "happy", 
    "hill", "house", "king", "lad", "leaves", "love", "orange", 
    "pants", "paper", "purple", "rain", "rainbow", "shirt", 
    "stem", "sunflower", "sweater", "three", "wear", "week", 
    "white", "yard", "yellow", "yelp"],
        "Grade2": [
  "africa", "after", "amharic", "arabic", "bangladesh", "bathroom",
  "bird", "blanket", "bookcase", "books", "canada", "carpet",
  "ceiling", "click", "curiosity", "dresser", "eight", "english",
  "ethiopia", "europe", "familiar", "find", "flower", "gratitude",
  "hindi", "laugh", "mean", "mirror", "palestine", "playground",
  "precious", "radiant", "rectangle", "school", "spanish", "square",
  "symphony", "temperature", "urdu", "write"
],
        "Grade3": [
  "apartment", "backpack", "bicycle", "boxcar", "butterfly", "camera", "chalkboard", "complex", "daring", 
  "delicate", "division", "dreamers", "encyclopedia", "favorite", "guitar", "illuminate", "invent", "jellyfish", 
  "kitchen", "language", "latch", "lessons", "letters", "library", "loaf", "meaning", "microscope", "monkey", 
  "multiplication", "mysterious", "numbers", "nutmeg", "octopus", "peculiar", "perseverance", "plaster", "poached", 
  "pumpkin", "rabbit", "school", "telescope", "umbrella", "violin", "waterfall", "xylophone"
],
        "Grade4": [
  "ambiguous", "antarctic", "calendar", "centipede", "conscientious", "counsel", "coupon", "crackle", "custard", 
  "darkness", "demonstrate", "devastate", "dinosaur", "dither", "essential", "exchange", "exquisite", "giraffe", 
  "glamorous", "graduate", "guess", "handwriting", "hardship", "helicopter", "highlight", "igloo", "ingenious", 
  "jaguar", "kangaroo", "medication", "nightmare", "norsemen", "opportunity", "ostrich", "percentage", "phenomenal", 
  "presentation", "question", "recent", "refrigerator", "rough", "sincere", "spreadsheet", "stampede", "suitable", 
  "swordsmen", "vikings", "windshield", "wishful", "wristwatch"
]
,
        "Grade5": [
  "abdicate", "accommodate", "advanced", "ambiguous", "amusing", "barrage", "belligerent", "berserk", "bizarre", 
  "bureaucracy", "cabbage", "complementary", "confiscate", "construction", "continuous", "creatures", "dehydrated", 
  "derogatory", "eccentricity", "evaporate", "evermore", "extensive", "formidable", "gigantic", "gregarious", 
  "hypnotize", "incognito", "intersect", "intuition", "knelt", "leopard", "meticulous", "nauseate", "nostalgic", 
  "optimistic", "oscillate", "perpendicular", "predominant", "quagmire", "qualitative", "solution", "solvent", 
  "spectators", "squeeze", "translucent", "tuneful", "ubiquitous", "unwavering", "vanish", "versatile", "violet", 
  "voice", "whimsical"
]
,
        "Grade6": [
  "administration", "advanced", "alabaster", "altitude", "amiable", "amusing", "anthem", "banishment", "barricade", 
  "boisterous", "commemorate", "compliant", "conclusion", "conference", "conserve", "discomfort", "disengage", 
  "disseminate", "entrepreneurship", "ephemeral", "esoteric", "exterior", "facetious", "faucet", "garrulous", 
  "hexagonal", "hypothesis", "improvise", "inscrutable", "intrepid", "jubilation", "kaleidoscope", "kneel", 
  "leadership", "lecture", "leeway", "luminance", "mischievous", "negotiation", "partisan", "phenomenon", "primers", 
  "procession", "pronounce", "recognition", "reimburse", "relics", "resemble", "salvation", "scrimmage", "simulation", 
  "spectators", "strident", "subdivision", "vagabond"
],
        "Grade7": [
  "accompany", "affirmation", "alabaster", "altitude", "brigadier", "bulletin", "cherished", "collaboration", 
  "colonel", "commendable", "commissioned", "composure", "conquering", "consecutive", "contagious", "correctional", 
  "defensiveness", "disposition", "disseminate", "enlisted", "euphoria", "fluctuate", "germinate", "inexorable", 
  "infraction", "jettison", "lascivious", "lieutenant", "mellifluous", "metamorphosis", "miniature", "miracle", 
  "narration", "paramedic", "pennant", "percussion", "perfidious", "perish", "perspicacity", "pharaoh", "qualm", 
  "quantum", "recognition", "resourceful", "sausage", "scenery", "scrimmage", "siesta", "sophomore", "stagnant", 
  "superfluous", "sycophant", "travesty", "undeniable", "vegetation", "veracity", "vocational"
]
,
        "Grade8": [
  "adage", "affirmation", "airman", "amethyst", "amphitheater", "annexation", "appendectomy", "azalea", 
  "boisterously", "cacophony", "chandeliers", "cherished", "churlish", "cinnabar", "collaborate", "commendable", 
  "concierge", "connoisseur", "controversy", "defensiveness", "detrimental", "dexterity", "discordant", "discredit", 
  "discrepancy", "disparate", "emaciated", "ephemeral", "excerpt", "extravaganza", "handkerchief", "indelible", 
  "indigenous", "jubilee", "laggard", "masquerade", "merengue", "nauseous", "numbness", "ominous", "onomatopoeia", 
  "perfidious", "piedmont", "plaudits", "preclude", "pronunciation", "pulmonary", "quaint", "quixotic", "redundancy", 
  "remorse", "servile", "sobriety", "sphinx", "tumultuous", "ubiquity", "unfathomable", "venerate", "winchester", 
  "worcestershire"
]
,
    },
    "Arabic": {
        "Grade1": ["بِسْمِ", "ٱلْحَمْدُ", "رَبِّ", "مَـٰلِكِ", "يَوْمِ", "إِيَّاكَ", "نَعْبُدُ", "ٱهْدِنَا",  "صِرَٰطَ", "ٱلَّذِينَ", "أَنْعَمْتَ", "عَلَيْهِمْ",  "غَيْرِ", "عَلَيْهِمْ", "وَلَا"],
        "Grade2":  ["قُلْ", "أَعُوذُ", "بِرَبِّ", "ٱلنَّاسِ", "مَلِكِ", "إِلَـٰهِ", "مِن", "شَرِّ", "ٱلْوَسْوَاسِ", "ٱلْخَنَّاسِ", "ٱلَّذِى", "يُوَسْوِسُ", "فِى", "صُدُورِ", "ٱلْجِنَّةِ", "ٱلْفَلَقِ", "خَلَقَ", "غَاسِقٍ", "إِذَا", "وَقَبَ", "ٱلنَّفَّـٰثَـٰتِ", "ٱلْعُقَدِ", "حَاسِدٍ", "حَسَدَ"],
         "Grade3": ["قُلْ", "هُوَ", "ٱللَّهُ", "أَحَدٌ", "ٱلصَّمَدُ", "لَمْ", "يَلِدْ", "يُولَدْ", "يَكُن", "لَّهُۥ", "كُفُوًا", "تَبَّتْ", "يَدَآ", "أَبِى", "لَهَبٍ", "مَآ", "أَغْنَىٰ", "عَنْهُ", "مَالُهُۥ", "كَسَبَ", "سَيَصْلَىٰ", "نَارًۭا", "ذَاتَ", "وَٱمْرَأَتُهُۥ", "حَمَّالَةَ", "ٱلْحَطَبِ", "فِى", "جِيدِهَا", "حَبْلٌۭ", "مِّن", "مَّسَدٍۭ"],
        "Grade4": ["إِذَا", "جَآءَ", "نَصْرُ", "ٱللَّهِ", "وَٱلْفَتْحُ", "وَرَأَيْتَ", "ٱلنَّاسَ", "يَدْخُلُونَ", "دِينِ", "أَفْوَاجًۭا", "فَسَبِّحْ", "بِحَمْدِ", "رَبِّكَ", "وَٱسْتَغْفِرْهُ", "إِنَّهُۥ", "كَانَ", "تَوَّابًۢا", "قُلْ", "يَـٰٓأَيُّهَا", "ٱلْكَـٰفِرُونَ", "أَعْبُدُ", "تَعْبُدُونَ", "وَلَآ", "أَنتُمْ", "عَـٰبِدُونَ", "عَابِدٌۭ", "عَبَدتُّمْ", "لَكُمْ", "دِينُكُمْ", "وَلِىَ"],
        "Grade5": [ "أَعْطَيْنَـٰكَ", "ٱلْكَوْثَرَ", "فَصَلِّ", "لِرَبِّكَ", "وَٱنْحَرْ", "شَانِئَكَ", "ٱلْأَبْتَرُ", "أَرَءَيْتَ", "ٱلَّذِى", "يُكَذِّبُ", "بِٱلدِّينِ", "يَدُعُّ", "ٱلْيَتِيمَ", "يَحُضُّ", "عَلَىٰ", "طَعَامِ", "ٱلْمِسْكِينِ", "فَوَيْلٌۭ", "لِّلْمُصَلِّينَ", "ٱلَّذِينَ", "صَلَاتِهِمْ", "سَاهُونَ", "يُرَآءُونَ", "وَيَمْنَعُونَ", "ٱلْمَاعُونَ"],
        "Grade6": ["لِإِيلَـٰفِ", "قُرَيْشٍ", "إِۦلَـٰفِهِمْ", "رِحْلَةَ", "ٱلشِّتَآءِ", "وَٱلصَّيْفِ", "فَلْيَعْبُدُوا۟", "هَـٰذَا", "ٱلْبَيْتِ", "ٱلَّذِىٓ", "أَطْعَمَهُم", "جُوعٍۢ", "وَءامَنَهُم", "خَوْفٍۭ", "كَيْفَ", "رَبُّكَ", "بِأَصْحَـٰبِ", "ٱلْفِيلِ", "يَجْعَلْ", "كَيْدَهُمْ", "تَضْلِيلٍۢ", "وَأَرْسَلَ", "عَلَيْهِمْ", "طَيْرًا", "أَبَابِيلَ", "تَرْمِيهِم", "بِحِجَارَةٍۢ", "سِجِّيلٍۢ", "فَجَعَلَهُمْ", "كَعَصْفٍۢ", "مَّأْكُولٍۭ"],
        "Grade7": ["وَيْلٌۭ", "لِّكُلِّ", "هُمَزَةٍۢ", "لُّمَزَةٍ", "ٱلَّذِى", "جَمَعَ", "مَالًۭا", "وَعَدَّدَهُۥ", "يَحْسَبُ", "أَنَّ", "مَالَهُۥٓ", "أَخْلَدَهُۥ", "كَلَّا", "لَيُنۢبَذَنَّ", "فِى", "ٱلْحُطَمَةِ", "وَمَآ", "أَدْرَىٰكَ", "مَا", "ٱلْحُطَمَةُ", "نَارُ", "ٱللَّهِ", "ٱلْمُوقَدَةُ", "ٱلَّتِى", "تَطَّلِعُ", "عَلَى", "ٱلْأَفْـِٔدَةِ", "إِنَّهَا", "عَلَيْهِم", "مُّؤْصَدَةٌۭ", "فِى", "عَمَدٍۢ", "مُّمَدَّدَةٍۭ", "وَٱلْعَصْرِ", "إِنَّ", "ٱلْإِنسَـٰنَ", "لَفِى", "خُسْرٍ", "إِلَّا", "ٱلَّذِينَ", "ءَامَنُوا۟", "وَعَمِلُوا۟", "ٱلصَّـٰلِحَـٰتِ", "بِٱلْحَقِّ", "وَتَوَاصَوْ", "بِٱلصَّبْرِ"],
        "Grade8": ["أَلْهَىٰكُمُ", "ٱلتَّكَاثُرُ", "حَتَّىٰ", "زُرْتُمُ", "ٱلْمَقَابِرَ", "كَلَّا", "سَوْفَ", "تَعْلَمُونَ", "ثُمَّ", "ٱلْيَقِينِ", "لَتَرَوُنَّ", "ٱلْجَحِيمَ", "لَتَرَوُنَّهَا", "عَيْنَ", "لَتُسْـَٔلُنَّ", "يَوْمَئِذٍ", "عَنِ", "ٱلنَّعِيمِ", "ٱلْقَارِعَةُ", "مَا", "يَكُونُ", "ٱلنَّاسُ", "كَٱلْفَرَاشِ", "ٱلْمَبْثُوثِ", "وَتَكُونُ", "ٱلْجِبَالُ", "كَٱلْعِهْنِ", "ٱلْمَنفُوشِ", "ثَقُلَتْ", "مَوَزِينُهُۥ", "عِيشَةٍۢ", "رَّاضِيَةٍۢ", "خَفَّتْ", "فَأُمُّهُۥ", "هَاوِيَةٌۭ", "حَامِيَةٌۢ"]

    },
}

# Initialize state to track used words, contestants, and rounds
if "used_words" not in st.session_state:
    st.session_state["used_words"] = {"English": {grade: [] for grade in word_lists["English"].keys()},
                                      "Arabic": {grade: [] for grade in word_lists["Arabic"].keys()}}
if "contestants" not in st.session_state:
    st.session_state["contestants"] = {"English": {grade: [] for grade in word_lists["English"].keys()},
                                       "Arabic": {grade: [] for grade in word_lists["Arabic"].keys()}}
if "round" not in st.session_state:
    st.session_state["round"] = {"English": {grade: 1 for grade in word_lists["English"].keys()},
                                 "Arabic": {grade: 1 for grade in word_lists["Arabic"].keys()}}
if "round_history" not in st.session_state:
    st.session_state["round_history"] = {"English": {grade: {} for grade in word_lists["English"].keys()},
                                         "Arabic": {grade: {} for grade in word_lists["Arabic"].keys()}}

# Streamlit app title
st.title("📝 MD Tutorials: Spelling Bee Competition")

# Toggle button for language
language = st.radio("Select Language:", ["English", "Arabic"])

# Sidebar for grade and customization
st.sidebar.header("Customize Spelling Bee")
selected_grade = st.sidebar.selectbox("Select Grade:", options=list(word_lists[language].keys()))

# Input number of contestants
st.subheader("Setup Contestants")
num_contestants = st.number_input("Number of contestants:", min_value=1, step=1, key=f"{language}_contestants_input")

# Assign words for the current round
if st.button("Assign Words for Current Round"):
    available_words = [
        word for word in word_lists[language][selected_grade]
        if word not in st.session_state["used_words"][language][selected_grade]
    ]

    if len(available_words) >= num_contestants:
        assigned_words = random.sample(available_words, num_contestants)
        st.session_state["used_words"][language][selected_grade].extend(assigned_words)
        st.session_state["contestants"][language][selected_grade] = assigned_words

        # Save to round history
        current_round = st.session_state["round"][language][selected_grade]
        st.session_state["round_history"][language][selected_grade][current_round] = assigned_words

        st.success(f"Round {current_round} Words Assigned ({language}):")
        for i, word in enumerate(assigned_words, start=1):
            st.write(f"Contestant {i}: {word}")
    else:
        st.warning(f"Not enough {language} words available to assign to all contestants.")

# Display round history
st.subheader("Round History")
# Ensure the selected grade exists in round_history before accessing it
if selected_grade in st.session_state["round_history"][language]:
    for round_number, words in st.session_state["round_history"][language][selected_grade].items():
        st.markdown(f"**Round {round_number}:** {', '.join(words)}")
else:
    st.write(f"No history available for {selected_grade} in {language}.")


# Progress to the next round
if st.button("Next Round"):
    st.session_state["round"][language][selected_grade] += 1
    st.success(f"Advanced to Round {st.session_state['round'][language][selected_grade]} ({language}).")
