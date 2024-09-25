document.addEventListener('DOMContentLoaded', function() {
    const buttons = document.querySelectorAll('button:not(#start-timer):not(#copy-button)');
    const previewBox = document.getElementById('preview-box');
    const copyButton = document.getElementById('copy-button');
    const timerDisplay = document.getElementById('timer');
    const startTimerButton = document.getElementById('start-timer');

    let timerInterval;
    let seconds = 0;
    let isTimerRunning = false;

    function formatTime(totalSeconds) {
        const minutes = Math.floor(totalSeconds / 60);
        const seconds = totalSeconds % 60;
        return `${minutes.toString().padStart(2, '0')}:${seconds.toString().padStart(2, '0')}`;
    }

    function startTimer() {
        if (isTimerRunning) {
            // Reset timer
            clearInterval(timerInterval);
            seconds = 0;
            timerDisplay.textContent = '00:00';
            startTimerButton.textContent = 'Start Timer';
            isTimerRunning = false;
        } else {
            // Start timer
            timerInterval = setInterval(() => {
                seconds++;
                timerDisplay.textContent = formatTime(seconds);
            }, 1000);
            startTimerButton.textContent = 'Reset Timer';
            isTimerRunning = true;
        }
    }

    startTimerButton.addEventListener('click', startTimer);

    buttons.forEach(button => {
        button.addEventListener('click', function() {
            if (!isTimerRunning) {
                alert('Please start the timer first!');
                return;
            }
            const currentTime = timerDisplay.textContent;
            const text = `${currentTime} [${this.textContent.trim()}]`;
            if (previewBox.textContent) {
                previewBox.textContent += '\n' + text;
            } else {
                previewBox.textContent = text;
            }
        });
    });

    copyButton.addEventListener('click', function() {
        if (previewBox.textContent) {
            navigator.clipboard.writeText(previewBox.textContent).then(() => {
                alert('Content copied to clipboard!');
            }).catch(err => {
                console.error('Failed to copy: ', err);
                alert('Failed to copy to clipboard. Please try again.');
            });
        } else {
            alert('No content to copy. Please log some events first.');
        }
    });
});
