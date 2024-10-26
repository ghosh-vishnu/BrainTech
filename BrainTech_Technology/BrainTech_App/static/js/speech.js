// welcome.js

document.addEventListener("DOMContentLoaded", function() {
    // Function to speak the welcome message
    function speakWelcome() {
        // Create a new SpeechSynthesisUtterance
        var utterance = new SpeechSynthesisUtterance("Welcome to BrainTech Technology");
        utterance.lang = 'en-US';

        // Speak the utterance
        window.speechSynthesis.speak(utterance);
    }

    // Call the speakWelcome function after a short delay
    setTimeout(speakWelcome, 1000); // 1 second delay before speaking
});
