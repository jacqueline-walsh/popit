var number = 1;
var up = document.getElementById('up');
var down = document.getElementById('down');

var thumbsUp = document.getElementById('thumbsUp');
thumbsUp.addEventListener('click', plusOne);

var thumbsDown = document.getElementById('thumbsDown');
thumbsDown.addEventListener('click', minusOne);

function plusOne() {
  number++;
  up.innerHTML = number;
}

function minusOne() {
    if (number > 0) {
        number--
        down.innerHTML = number;
    } 
    down.innerHTML = number;
  }
