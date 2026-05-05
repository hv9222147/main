let points = 0;
let currentQ = 0;
let currentSubject = "";

const data = {
  math: [
    { q: "2 + 3 = ?", ans: 5 },
    { q: "4 + 4 = ?", ans: 8 }
  ],
  english: [
    { q: "A for ?", ans: "apple" },
    { q: "B for ?", ans: "ball" }
  ],
  science: [
    { q: "Water formula?", ans: "h2o" }
  ],
  gk: [
    { q: "Capital of India?", ans: "delhi" },
    { q: "National animal?", ans: "tiger" }
  ],
  drawing: [
    { q: "Color of sky?", ans: "blue" },
    { q: "Color of grass?", ans: "green" }
  ]
};

function show(sub) {
  currentSubject = sub;
  currentQ = 0;
  loadQuestion();
}

function loadQuestion() {
  let obj = data[currentSubject][currentQ];

  document.getElementById("content").innerHTML = `
    <h3>${obj.q}</h3>
    <input id="userAns" placeholder="Your answer">
    <br><br>
    <button onclick="checkAnswer()">Submit</button>
    <p id="result"></p>
  `;
}

function checkAnswer() {
  let user = document.getElementById("userAns").value.toLowerCase();
  let correct = data[currentSubject][currentQ].ans;

  if (user == correct) {
    document.getElementById("result").innerText = "✅ Correct!";
    points += 10;
  } else {
    document.getElementById("result").innerText = "❌ Wrong!";
  }

  document.getElementById("points").innerText = points;
  document.getElementById("progress").style.width = points + "%";

  currentQ++;

  setTimeout(() => {
    if (currentQ < data[currentSubject].length) {
      loadQuestion();
    } else {
      document.getElementById("content").innerHTML =
        `<h2>🎉 Completed ${currentSubject}!</h2>`;
    }
  }, 1000);
}

// Show subject questions
function show(sub) {
  currentSubject = sub;
  currentQ = 0;
  loadQuestion();
}

// Load question
function loadQuestion() {
  let obj = data[currentSubject][currentQ];

  document.getElementById("content").innerHTML = `
    <h3>${obj.q}</h3>
    <input id="userAns" placeholder="Your answer">
    <br><br>
    <button onclick="checkAnswer()">Submit</button>
    <p id="result"></p>
  `;
}

// Check answer
function checkAnswer() {
  let user = document.getElementById("userAns").value.toLowerCase();
  let correct = data[currentSubject][currentQ].ans.toString().toLowerCase();

  if (user == correct) {
    document.getElementById("result").innerText = "✅ Correct!";
    points += 10;
  } else {
    document.getElementById("result").innerText = "❌ Your answer is wrong";
  }

  update();

  currentQ++;

  // Next question ya reward
  setTimeout(() => {
    if (currentQ < data[currentSubject].length) {
      loadQuestion();
    } else {
      document.getElementById("content").innerHTML =
        `<h2>🎉 You completed ${currentSubject}!</h2>
         <h3>⭐ Reward Points: ${points}</h3>`;
    }
  }, 1000);
}

// Update progress
function update() {
  document.getElementById("points").innerText = points;
  document.getElementById("progress").style.width = points + "%";
}

// Dark mode
function toggleDark() {
  document.body.classList.toggle("dark");
}

// Drag & Drop
window.onload = function () {
  let apple = document.getElementById("apple");
  let basket = document.getElementById("basket");

  apple.addEventListener("dragstart", () => {});

  basket.addEventListener("dragover", (e) => e.preventDefault());

  basket.addEventListener("drop", () => {
    alert("🎉 Great Job!");
    points += 20;
    update();
  });
};

// Chatbot
function chat() {
  let textBox = document.getElementById("input");
  let outputBox = document.getElementById("output");

  let userText = textBox.value.toLowerCase();

  if (userText === "") {
    outputBox.innerText = "Please type something!";
    return;
  }

  if (userText.includes("hello")) {
    outputBox.innerText = "Hi 😊 How are you?";
  } 
  else if (userText.includes("math")) {
    outputBox.innerText = "Let's do some math!";
  } 
  else {
    outputBox.innerText = "I am your learning buddy 🤖";
  }

  textBox.value = ""; // clear input
}