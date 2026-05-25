from flask import Flask,render_template,request
import joblib
import re
import random
app= Flask(__name__)
model = joblib.load("model.pkl")

# Clean text (same as training)
def clean_text(text):
    text = re.sub(r'@\w+', '', text)
    text = re.sub(r'#', '', text)
    text = re.sub(r'[^a-zA-Z ]', '', text)
    return text.lower()
songs = {
    "joy": [
        "Happy - Pharrell Williams",
        "Good Life - OneRepublic",
        "On Top Of The World - Imagine Dragons",
        "Can't Stop The Feeling - Justin Timberlake",
        "Walking On Sunshine - Katrina & The Waves",
        "Uptown Funk - Mark Ronson ft. Bruno Mars",
        "Best Day Of My Life - American Authors",
        "Sugar - Maroon 5",
        "Firework - Katy Perry",
        "Shake It Off - Taylor Swift",
        "Roar - Katy Perry",
        "Don't Stop Me Now - Queen",
        "Lovely Day - Bill Withers",
        "Sunroof - Nicky Youre",
        "Good as Hell - Lizzo",
        "Hey Ya! - Outkast",
        "Levitating - Dua Lipa",
        "Dynamite - BTS",
        "Feel It Still - Portugal. The Man",
        "I'm Still Standing - Elton John",
        "Perfect - Ed Sheeran",
"All of Me - John Legend",
"Until I Found You - Stephen Sanchez",
"Thinking Out Loud - Ed Sheeran",
"At My Worst - Pink Sweat$",
"Adore You - Harry Styles",
"Love Story - Taylor Swift",
"Just The Way You Are - Bruno Mars",
"Best Part - Daniel Caesar ft. H.E.R."
    ],

    "sadness": [
        "Someone Like You - Adele",
        "Let Her Go - Passenger",
        "Fix You - Coldplay",
        "The Night We Met - Lord Huron",
        "All I Want - Kodaline",
        "Back To December - Taylor Swift",
        "Stay With Me - Sam Smith",
        "Hurt - Johnny Cash",
        "When I Was Your Man - Bruno Mars",
        "Drivers License - Olivia Rodrigo",
        "Tears Dry On Their Own - Amy Winehouse",
        "Too Good At Goodbyes - Sam Smith",
        "Jealous - Labrinth",
        "Without Me - Halsey",
        "Say Something - A Great Big World",
        "Someone You Loved - Lewis Capaldi",
        "Breakeven - The Script",
        "Fix You (Acoustic) - Coldplay",
        "Lonely - Justin Bieber",
        "Easy On Me - Adele"
    ],

    "anger": [
        "Believer - Imagine Dragons",
        "Numb - Linkin Park",
        "Stronger - Kanye West",
        "Killing In The Name - Rage Against The Machine",
        "Break Stuff - Limp Bizkit",
        "Bad Guy - Billie Eilish",
        "In The End - Linkin Park",
        "Look What You Made Me Do - Taylor Swift",
        "You Oughta Know - Alanis Morissette",
        "Rolling In The Deep - Adele",
        "Fighter - Christina Aguilera",
        "Natural - Imagine Dragons",
        "My Songs Know What You Did In The Dark - Fall Out Boy",
        "Centuries - Fall Out Boy",
        "Radioactive - Imagine Dragons",
        "Whatever It Takes - Imagine Dragons",
        "Monster - Skillet",
        "DNA - Kendrick Lamar",
        "Till I Collapse - Eminem",
        "Lose Yourself - Eminem"
    ],

    "fear": [
        "Demons - Imagine Dragons",
        "Mad World - Gary Jules",
        "Boulevard of Broken Dreams - Green Day",
        "Creep - Radiohead",
        "Breathe Me - Sia",
        "The Sound of Silence - Disturbed",
        "Runaway - AURORA",
        "Control - Halsey",
        "Everybody's Got To Learn Sometime - Beck",
        "My Immortal - Evanescence",
        "In The Woods Somewhere - Hozier",
        "Falling - Harry Styles",
        "Say Something - A Great Big World",
        "Youth - Daughter",
        "Liability - Lorde",
        "Waves - Dean Lewis",
        "Lost Without You - Freya Ridings",
        "The Scientist - Coldplay",
        "Skinny Love - Bon Iver",
        "Ghost - Justin Bieber"
    ]
    
}
@app.route("/", methods = ["GET","POST"])
def home():
    mood=None
    recommended_songs = []
    if request.method=="POST":
        user_text=request.form["user_text"]
        cleaned = clean_text(user_text)
        mood= model.predict([cleaned])[0]
        if mood in songs:
            recommended_songs = random.sample(
                songs[mood],
                min(3, len(songs[mood]))
            )

    return render_template("index.html", mood=mood, songs=recommended_songs)
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)