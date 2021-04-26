const textArea = $('.simulate-text');
const simBtn = $('.simulate-btn');

let i = 0;

let appendVal = function(){
    textArea.val("PlaceHolder" + i);
    i++;
}

simBtn.on('click', appendVal);


