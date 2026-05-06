let points = 0;
let currentQ = 0;
let currentSubject = "";

const data = {
  math: [
    { q: "What is 2 + 3?", ans: "5" },
    { q: "What is 4 + 4?", ans: "8" },
    { q: "What is 10 - 5?", ans: "5" },
    { q: "What is 3 × 2?", ans: "6" }
  ],
  english: [
    { q: "What starts with A? (Hint: 🍎)", ans: "apple" },
    { q: "What starts with B? (Hint: ⚽)", ans: "ball" },
    { q: "What starts with C? (Hint: 🐱)", ans: "cat" },
    { q: "What starts with D? (Hint: 🐶)", ans: "dog" }
  ],
  science: [
    { q: "What is the chemical formula for water?", ans: "h2o" },
    { q: "What planet is known as the Red Planet?", ans: "mars" },
    { q: "What do plants need to make food?", ans: "sunlight" }
  ],
  gk: [
    { q: "What is the capital of India?", ans: "delhi" },
    { q: "What is India's national animal?", ans: "tiger" },
    { q: "How many continents are there?", ans: "7" },
    { q: "What is the color of the sky on a clear day?", ans: "blue" }
  ],
  drawing: [
    { q: "What color is the sky?", ans: "blue" },
    { q: "What color is grass?", ans: "green" },
    { q: "What color are bananas?", ans: "yellow" },
    { q: "What color is the sun?", ans: "yellow" }
  ]
};

function show(sub) {
  currentSubject = sub;
  currentQ = 0;
  loadQuestion();
}

function loadQuestion() {
  if (currentQ >= data[currentSubject].length) {
    document.getElementById("content").innerHTML = `<h2>🎉 You completed ${currentSubject}!</h2><h3>⭐ Total Points: ${points}</h3>`;
    return;
  }
  let obj = data[currentSubject][currentQ];
  document.getElementById("content").innerHTML = `
    <h3>${obj.q}</h3>
    <input id="userAns" placeholder="Your answer" type="text">
    <br><br>
    <button onclick="checkAnswer()">Submit</button>
    <p id="result"></p>
  `;
}

function checkAnswer() {
  let user = document.getElementById("userAns").value.trim().toLowerCase();
  let correct = data[currentSubject][currentQ].ans.toString().toLowerCase();

  if (user === correct) {
    document.getElementById("result").innerText = "✅ Correct! Great job!";
    points += 10;
    // Simple animation
    document.getElementById("result").style.color = "green";
    setTimeout(() => document.getElementById("result").style.color = "", 500);
  } else {
    document.getElementById("result").innerText = `❌ Wrong! The correct answer is ${data[currentSubject][currentQ].ans}`;
    document.getElementById("result").style.color = "red";
    setTimeout(() => document.getElementById("result").style.color = "", 500);
  }

  updateProgress();
  currentQ++;

  setTimeout(() => {
    loadQuestion();
  }, 2000);
}

function updateProgress() {
  document.getElementById("points").innerText = points;
  // Cap progress at 100%
  let progressPercent = Math.min(points, 100);
  document.getElementById("progress").style.width = progressPercent + "%";
}

function toggleDark() {
  document.body.classList.toggle("dark");
}

// Drag & Drop
window.onload = function () {
  let apple = document.getElementById("apple");
  let basket = document.getElementById("basket");

  apple.addEventListener("dragstart", (e) => {
    e.dataTransfer.setData("text", e.target.id);
  });

  basket.addEventListener("dragover", (e) => {
    e.preventDefault();
  });

  basket.addEventListener("drop", (e) => {
    e.preventDefault();
    let data = e.dataTransfer.getData("text");
    if (data === "apple") {
      alert("🎉 Great Job! You dragged the apple to the basket!");
      points += 20;
      updateProgress();
      // Hide apple after drop
      apple.style.display = "none";
    }
  });
};

function resetProgress() {
  points = 0;
  currentQ = 0;
  currentSubject = "";
  document.getElementById("content").innerHTML = "";
  updateProgress();
}

// Chatbot
function chat() {
  let textBox = document.getElementById("input");
  let outputBox = document.getElementById("output");

  let userText = textBox.value.trim().toLowerCase();

  if (userText === "") {
    outputBox.innerText = "Please type something! 😊";
    return;
  }

  if (userText.includes("hello") || userText.includes("hi")) {
    outputBox.innerText = "Hi there! How are you? 😊";
  } else if (userText.includes("math")) {
    outputBox.innerText = "Math is fun! Let's solve some problems! ➕";
  } else if (userText.includes("english")) {
    outputBox.innerText = "English helps us communicate! 🔤";
  } else if (userText.includes("science")) {
    outputBox.innerText = "Science is amazing! 🔬";
  } else if (userText.includes("gk") || userText.includes("general knowledge")) {
    outputBox.innerText = "GK makes you smarter! 🌍";
  } else if (userText.includes("drawing")) {
    outputBox.innerText = "Drawing is creative! 🎨";
  } else if (userText.includes("help")) {
    outputBox.innerText = "I can help you learn! Choose a subject above. 🤖";
  } else {
    outputBox.innerText = "I'm your learning buddy! Ask me about subjects or say hello. 🤖";
  }

  textBox.value = ""; // clear input
}

// Allow Enter key to send message
document.getElementById("input").addEventListener("keypress", function(event) {
  if (event.key === "Enter") {
    chat();
  }
});