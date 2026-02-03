from flask import Flask, render_template_string

app = Flask(__name__)

html = """
<!DOCTYPE html>
<html>
<head>
<title>For Anwesha 💖</title>
<meta name="viewport" content="width=device-width, initial-scale=1.0">

<link href="https://fonts.googleapis.com/css2?family=Pacifico&display=swap" rel="stylesheet">

<style>
body {
    margin: 0;
    font-family: 'Segoe UI', sans-serif;
    background: linear-gradient(135deg, #ff9a9e, #fad0c4);
    text-align: center;
    overflow-x: hidden;
}

section {
    min-height: 100vh;
    padding: 60px 20px;
}

h1 {
    color: #ff2f68;
    font-size: 3em;
}

button {
    padding: 15px 35px;
    font-size: 1.2em;
    border-radius: 40px;
    border: none;
    cursor: pointer;
}

#yes {
    background: #ff2f68;
    color: white;
}

#no {
    background: #555;
    color: white;
    position: absolute;
}

.letter {
    background: white;
    max-width: 850px;
    margin: auto;
    padding: 40px;
    border-radius: 20px;
    box-shadow: 0 20px 40px rgba(0,0,0,0.2);
    font-family: 'Pacifico', cursive;
    font-size: 1.2em;
    animation: fadeIn 2s ease;
}

.photos {
    display: flex;
    justify-content: center;
    gap: 20px;
    flex-wrap: wrap;
    margin-top: 20px;
}

.photos img {
    width: 220px;
    height: 220px;
    object-fit: cover;
    border-radius: 15px;
}

.song-card {
    background: white;
    margin: 15px auto;
    padding: 10px;
    max-width: 400px;
    border-radius: 15px;
    box-shadow: 0 10px 20px rgba(0,0,0,0.15);
}

@keyframes fadeIn {
    from { opacity: 0; transform: translateY(30px); }
    to { opacity: 1; transform: translateY(0); }
}
</style>
</head>

<body>

<audio id="bgMusic" loop>
    <source src="/static/music1.mp3" type="audio/mpeg"> 
</audio>

<!-- PAGE 1 -->
<section id="ask">
    <h1>Will you be my Valentine, Anwesha? 💖</h1>
    <br><br>
    <button id="yes" onclick="openLetter()">YES ❤️</button>
    <button id="no" onmouseover="moveNo()">NO 🙃</button>
</section>

<!-- PAGE 2 -->
<section id="letterSection" style="display:none;">
    <div class="letter">
        My dearest Anwesha,<br><br>
        From the moment you entered my life,
        everything became warmer and brighter.
        Your smile feels like home,
        and loving you feels effortless. You are the most beautiful girl I have ever seen Anwesha, tu mujhe apne pyaar mein pagal krdeti hain tujhe nai pta bhai. I love being with you so much I love youu soo much jaanu <3
        <br><br>
        This Valentine’s Day and every day after,
        I choose you — always. 💖 Love you mera Kuchupuchu <3
        
        <div class="photos">
            <img src="/static/photo1.jpeg">
            <img src="/static/photo2.jpeg">
        </div>

        <br>
        <button onclick="nextPage()">Click Next jaanu 💕</button>
    </div>
</section>

<!-- PAGE 3 -->
<section id="memories" style="display:none;">
    <h1>Us. Always. ❤️</h1>

    <div class="photos">
        <img src="/static/photo3.jpeg">
        <img src="/static/photo4.png">
    </div>

    <h2>Our Songs 🎶</h2>

    <div class="song-card">
        <iframe src="https://open.spotify.com/embed/track/1EjxJHY9A6LMOlvyZdwDly"
        width="100%" height="80" frameBorder="0"
        allow="autoplay; encrypted-media"></iframe>
    </div>

    <div class="song-card">
        <iframe src="https://open.spotify.com/embed/track/3OgOVP2bTK17d4iibgXdI9"
        width="100%" height="80" frameBorder="0"
        allow="autoplay; encrypted-media"></iframe>
    </div>
</section>

<script>
function moveNo() {
    const no = document.getElementById("no");
    no.style.left = Math.random() * 80 + "vw";
    no.style.top = Math.random() * 80 + "vh";
}

function openLetter() {
    document.getElementById("ask").style.display = "none";
    document.getElementById("letterSection").style.display = "block";

    const music = document.getElementById("bgMusic");
    music.volume = 0.3;  //soft romantic volume
    music.play();
    
    startHearts();
}

function nextPage() {
    document.getElementById("letterSection").style.display = "none";
    document.getElementById("memories").style.display = "block";
}

function startHearts() {
    setInterval(() => {
        const h = document.createElement("div");
        h.innerHTML = "❤️";
        h.style.position = "fixed";
        h.style.left = Math.random() * 100 + "vw";
        h.style.top = "-20px";
        h.style.fontSize = "22px";
        h.style.animation = "fall 5s linear";
        document.body.appendChild(h);
        setTimeout(() => h.remove(), 5000);
    }, 400);
}
</script>

</body>
</html>
"""

@app.route("/")
def home():
    return render_template_string(html)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
