'use static'


footer = document.querySelector('.footer');
close = document.querySelector('.help_box-close');
box = document.querySelector('.help_box');

help = document.getElementById('help');


/* button listeners for footer elements */
close = box.addEventListener('click', function() {
    box.style.visibility = 'hidden';
})
open = help.addEventListener('click', function() {
    box.style.visibility = 'visible';
})




