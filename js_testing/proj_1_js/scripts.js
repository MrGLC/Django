const squares = document.querySelectorAll('.square');

const leftPanel = document.querySelector('.left-panel');

for (let i = 0; i < 16; i++) { // Create 16 squares (4x4)
  const square = document.createElement('div');
  square.classList.add('square');
  leftPanel.appendChild(square);
}

squares.forEach(square => {
  square.addEventListener('click', () => {
    square.classList.toggle('active');
  });
});
