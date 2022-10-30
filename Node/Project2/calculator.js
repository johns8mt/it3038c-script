//https://stackoverflow.com/questions/51215161/how-to-select-all-buttons-with-foreach-in-js-dom-no-jquery
// This site is where I found how to create this using the buttons feature, there are lots of articles that teach you the basics of setting up things. 

(function(){
  
  let screen = document.querySelector('.screen');
  let buttons = document.querySelectorAll('.btn');
  let clear = document.querySelector('.btn-clear');
  let equal = document.querySelector('.btn-equal');
  
  buttons.forEach(function(button){
    button.addEventListener('click', function(e){
      let value = e.target.dataset.num;
      screen.value += value;
    })
  });
  
  equal.addEventListener('click', function(e){
    if(screen.value === ''){
      screen.value = 'Please Enter a Value';
    } else {
      let answer = eval(screen.value);
      screen.value = answer;
    }
  })
  
  clear.addEventListener('click', function(e){
    screen.value = '';
  })
 
})();
