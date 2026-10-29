<!DOCTYPE html>
<html lang="hi">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>G&SR Railway Operating Quiz</title>
    <style>
        body { font-family: 'Segoe UI', Arial, sans-serif; background-color: #f4f7f6; margin: 0; padding: 20px; display: flex; justify-content: center; }
        .quiz-container { background-color: #fff; padding: 30px; border-radius: 10px; box-shadow: 0 4px 15px rgba(0,0,0,0.1); max-width: 650px; width: 100%; }
        h1 { color: #007bff; text-align: center; font-size: 24px; margin-bottom: 20px; }
        .progress { font-size: 14px; color: #666; margin-bottom: 10px; text-align: right; }
        .question { font-size: 18px; font-weight: 600; color: #333; margin-bottom: 20px; }
        .options { display: flex; flex-direction: column; gap: 12px; }
        .btn { background-color: #f8f9fa; border: 2px solid #e9ecef; padding: 12px 15px; font-size: 16px; border-radius: 6px; cursor: pointer; text-align: left; transition: all 0.2s ease; color: #495057; width: 100%; }
        .btn:hover:not([disabled]) { background-color: #e2e6ea; border-color: #dae0e5; }
        .btn.correct { background-color: #d4edda !important; border-color: #c3e6cb !important; color: #155724 !important; font-weight: bold; }
        .btn.wrong { background-color: #f8d7da !important; border-color: #f5c6cb !important; color: #721c24 !important; }
        .feedback { margin-top: 20px; padding: 15px; border-radius: 6px; display: none; font-size: 15px; line-height: 1.5; }
        .feedback.show { display: block; }
        .feedback-correct { background-color: #e2f0d9; color: #385723; border-left: 5px solid #385723; }
        .feedback-wrong { background-color: #fff2cc; color: #7f6000; border-left: 5px solid #7f6000; }
        .next-btn { display: block; width: 100%; background-color: #007bff; color: white; border: none; padding: 12px; font-size: 16px; border-radius: 6px; cursor: pointer; margin-top: 20px; font-weight: bold; text-align: center; }
        .next-btn:hover { background-color: #0056b3; }
        .result-screen { text-align: center; }
        .score { font-size: 48px; font-weight: bold; color: #28a745; margin: 20px 0; }
    </style>
</head>
<body>
<div class="quiz-container">
    <div id="quiz-box">
        <h1>रेलवे संचालन एवं G&SR क्विज़</h1>
        <div class="progress" id="progress">प्रश्न 1 / 10</div>
        <div class="question" id="question-text">लोड हो रहा है...</div>
        <div class="options" id="options-box"></div>
        <div class="feedback" id="feedback-box"></div>
        <button class="next-btn" id="next-button" style="display:none;" onclick="nextQuestion()">अगला प्रश्न</button>
    </div>
    <div id="result-box" class="result-screen" style="display:none;">
        <h1>क्विज़ समाप्त!</h1>
        <p>आपका कुल स्कोर नीचे दिया गया है:</p>
        <div class="score" id="final-score">0 / 0</div>
        <button class="next-btn" onclick="restartQuiz()">दोबारा शुरू करें</button>
    </div>
</div>
<script>
    const quizData = [
        { question: "पॉइन्ट इन्डीकेटर सीधी लाइन के लिए सेट हो तो रात में कौन सी बत्ती बताएगा?", options: ["हरी बत्ती", "सफेद बत्ती", "लाल बत्ती", "पीली बत्ती"], correct: 1, reason: "पॉइन्ट इन्डीकेटर जब सीधे ट्रैक (Main Line) के लिए सेट होता है, तो रात के समय सुरक्षित परिचालन को दर्शाने के लिए सफेद रोशनी प्रदर्शित करता है।" },
        { question: "ब्लॉक सेक्शन लिमिट बोर्ड (BSLB) कौन से स्टेशन पर होता है?", options: ["ए क्लास सिंगल लाइन स्टेशन", "बी क्लास डबल लाइन बहुसंकेती स्टेशन", "सी क्लास स्टेशन", "डी क्लास फ्लैग स्टेशन"], correct: 1, reason: "BSLB हमेशा बी-क्लास डबल लाइन स्टेशन पर लगाया जाता है जहाँ सबसे बाहरी पॉइंट ट्रेलिंग होता है, ताकि शंटिंग सीमाओं की पहचान हो सके।" },
        { question: "स्टेशन सेक्शन कौन से क्लास के स्टेशन पर होता है?", options: ["ए क्लास स्टेशन", "बी क्लास स्टेशन", "सी क्लास स्टेशन", "स्पेशल क्लास स्टेशन"], correct: 1, reason: "स्टेशन सेक्शन तकनीकी रूप से केवल बी-क्लास स्टेशनों का एक हिस्सा होता है, जो सिगनलों द्वारा संरक्षित होता है।" },
        { question: "बहुसंकेतीय (MACL) सिगनल व्यवस्था वाले स्टेशन पर लाइन क्लीयर देने की पर्याप्त दूरी (Block Overlap) कितनी होती है?", options: ["400 मीटर", "180 मीटर", "120 मीटर", "270 मीटर"], correct: 1, reason: "बहुसंकेती (Multiple Aspect) व्यवस्था में ब्लॉक ओवरलैप न्यूनतम 180 मीटर होना आवश्यक है, जबकि दो-संकेती में यह 400 मीटर होता है।" },
        { question: "खराब आगमन रोक सिगनल (Home Signal) को 'ऑन' स्थिति में पार करने के लिए स्टेशन मास्टर द्वारा कौन सा प्राधिकार पत्र दिया जाता है?", options: ["T-409", "T-369 (3b)", "T-806", "T-511"], correct: 1, reason: "किसी भी खराब रोक सिगनल को ऑन स्थिति में सुरक्षित रूप से पार करने के लिए अधिकृत फॉर्म T-369(3b) जारी किया जाता है।" },
        { question: "ब्लॉक सेक्शन में धुन्ध या कोहरे के मौसम में सम्पूर्ण ब्लॉक पद्धति के अन्तर्गत गाड़ी की अधिकतम गति क्या होगी?", options: ["30 किमी/घंटा", "60 किमी/घंटा", "15 किमी/घंटा", "सामान्य गति"], correct: 1, reason: "कोहरे के दौरान दृश्यता कम होने पर सुरक्षा के दृष्टिकोण से पूर्ण ब्लॉक सिस्टम में अधिकतम गति 60 किमी/घंटा निर्धारित की गई है।" },
        { question: "रेलवे यार्ड में सामान्यतः शंटिंग संचालन के दौरान अधिकतम अनुमेय गति कितनी होती है?", options: ["30 किमी/घंटा", "15 किमी/घंटा", "8 किमी/घंटा", "25 किमी/घंटा"], correct: 1, reason: "G&SR नियमों के तहत यार्ड के अंदर सामान्य शंटिंग मूवमेंट्स के लिए अधिकतम गति सीमा 15 किमी/घंटा फिक्स है।" },
        { question: "किसी पहले से अवरुद्ध लाइन (Occupied Line) पर किसी ट्रेन को रिसीव करने के लिए स्टेशन मास्टर द्वारा कौन सा प्राधिकार पत्र जारी किया जाता है?", options: ["T-369(3b)", "T-509", "T-511", "T-806"], correct: 1, reason: "जब किसी line पर पहले से ही कोई अवरोध या वाहन खड़ा हो और वहाँ ट्रेन लेनी हो, तो फॉर्म T-509 का उपयोग किया जाता है।" },
        { question: "डबल लाइन (Double Line) सेक्शन पर पूर्ण संचार व्यवस्था भंग (Total Failure) होने पर लोको पायलट को कौन सा प्राधिकार पत्र दिया जाता है?", options: ["T/B-602", "T/C-602", "T/D-602", "T/A-602"], correct: 1, reason: "डबल लाइन पर जब संचार के सभी साधन ठप हो जाएँ, तो ट्रेनों को आगे भेजने के लिए अथॉरिटी फॉर्म T/C-602 दिया जाता है।" },
        { question: "ब्लॉक यंत्रों (Block Instruments) को ऑपरेट करने के लिए स्टेशन मास्टर के पास कौन सा वैध दस्तावेज होना अनिवार्य है?", options: ["ड्राइविंग लाइसेंस", "सक्षमता प्रमाण-पत्र (Competency)", "स्वास्थ्य प्रमाण-पत्र", "पहचान पत्र"], correct: 1, reason: "सेफ्टी गियर और ब्लॉक पैनल हैंडल करने के लिए ऑपरेटिंग स्टाफ के पास वैध सक्षमता प्रमाण-पत्र (Competency Certificate) होना अनिवार्य है, जो हर 3 साल में रिन्यू होता है।" }
    ];

    let currentQuestionIndex = 0, score = 0;
    const questionText = document.getElementById("question-text"), optionsBox = document.getElementById("options-box"), progressText = document.getElementById("progress"), feedbackBox = document.getElementById("feedback-box"), nextButton = document.getElementById("next-button"), quizBox = document.getElementById("quiz-box"), resultBox = document.getElementById("result-box"), finalScore = document.getElementById("final-score");

    function loadQuestion() {
        resetState();
        let currentQuestion = quizData[currentQuestionIndex];
        progressText.innerText = `प्रश्न ${currentQuestionIndex + 1} / ${quizData.length}`;
        questionText.innerText = currentQuestion.question;
        currentQuestion.options.forEach((option, index) => {
            const button = document.createElement("button");
            button.innerText = option; button.classList.add("btn");
            button.addEventListener("click", () => selectOption(index, button));
            optionsBox.appendChild(button);
        });
    }

    function resetState() {
        nextButton.style.display = "none";
        feedbackBox.classList.remove("show", "feedback-correct", "feedback-wrong");
        feedbackBox.innerText = "";
        while (optionsBox.firstChild) { optionsBox.removeChild(optionsBox.firstChild); }
    }

    function selectOption(selectedIndex, clickedButton) {
        let currentQuestion = quizData[currentQuestionIndex];
        const allButtons = optionsBox.querySelectorAll(".btn");
        allButtons.forEach(btn => btn.disabled = true);
        if (selectedIndex === currentQuestion.correct) {
            clickedButton.classList.add("correct"); score++;
            feedbackBox.innerText = "✓ सही उत्तर!\n" + currentQuestion.reason;
            feedbackBox.classList.add("show", "feedback-correct");
        } else {
            clickedButton.classList.add("wrong"); allButtons[currentQuestion.correct].classList.add("correct");
            feedbackBox.innerText = "✕ गलत उत्तर!\n" + currentQuestion.reason;
            feedbackBox.classList.add("show", "feedback-wrong");
        }
        nextButton.style.display = "block";
    }

    function nextQuestion() {
        currentQuestionIndex++;
        if (currentQuestionIndex < quizData.length) { loadQuestion(); } else { showResults(); }
    }

    function showResults() { quizBox.style.display = "none"; resultBox.style.display = "block"; finalScore.innerText = `${score} / ${quizData.length}`; }
    function restartQuiz() { currentQuestionIndex = 0; score = 0; quizBox.style.display = "block"; resultBox.style.display = "none"; loadQuestion(); }
    loadQuestion();
</script>
</body>
</html>
