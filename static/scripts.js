function hamburg() {
    const dropdown = document.getElementById('dropdown');
    dropdown.classList.toggle('active'); // Toggle the dropdown visibility
}

function cancel() {
    const dropdown = document.getElementById('dropdown');
    dropdown.classList.remove('active'); // Hide the dropdown
}


// Optional: Close the dropdown when clicking outside of it
window.onclick = function(event) {
    const dropdown = document.getElementById('dropdown');
    const navContainer = document.querySelector('.nav-container');

    if (!event.target.matches('.hamburg') && !event.target.closest('.dropdown') && dropdown.style.display === 'block') {
        dropdown.style.display = 'none'; // Hide dropdown
        navContainer.style.display = 'flex'; // Show nav container
    }
}


// Attach the cancel function to the cancel button
document.getElementById('cancelButton').addEventListener('click', cancel);

const texts = [
    "DEVELOPER",
    "PROGRAMMER"
];

let speed = 100;
const textElements = document.querySelector(".typewriter-text");

let textindex = 0;
let charcterIndex = 0;

function typeWriter() {
    if (charcterIndex < texts[textindex].length) {
        textElements.innerHTML += texts[textindex].charAt(charcterIndex);
        charcterIndex++;
        setTimeout(typeWriter, speed);
    } else {
        setTimeout(eraseText, 1000);
    }
}


function eraseText() {
    if (textElements.innerHTML.length > 0) {
        textElements.innerHTML = textElements.innerHTML.slice(0, -1);
        setTimeout(eraseText, 50);
    } else {
        textindex = (textindex + 1) % texts.length;
        charcterIndex = 0;
        setTimeout(typeWriter, 500);
    }
}

window.onload = typeWriter;