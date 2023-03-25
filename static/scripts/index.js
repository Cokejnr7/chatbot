//endpoint url
const URL = "https://chat.kolawolecoke.repl.co/prompt/";


const userInput = document.querySelector('.prompt');
const sendButton = document.querySelector('.send');
const textArea = document.querySelector('.textarea');
const allParagraphs = document.getElementsByTagName('p');

sendButton.addEventListener('click',myFunc);
userInput.addEventListener('keypress',enterFunc);

function enterFunc(e){
  if(e.key ==='Enter') myFunc(e);
}

async function myFunc(e){
  if(userInput.value !==""){
    
  //make user input and send button hidden
  userInput.style.visibility = "hidden";
  sendButton.style.visibility = "hidden";

  //create new elements
  const paragraph = document.createElement("p");
  const bot = document.createElement("p");

  //change bot response color grey
  bot.style.color = "grey"

  //for typing effect
  let i = 0;
  let speed = 50;

  //user prompt text
  let textValue = userInput.value;
  textArea.append(paragraph);
  paragraph.textContent = "USER: ";
  await typeWriter(paragraph,i,speed,textValue);

  //bot responseText and typewriter effect
  let responseText = await sendPrompt(textValue);
  console.log(responseText)
  bot.textContent = "BOT101: ";
  textArea.append(bot);
  typeWriter(bot,i,speed,responseText);

    bot.scrollIntoView()

  //reset user input and make it visible
   userInput.value = "";
    userInput.style.visibility = "visible";
    sendButton.style.visibility = "visible";
  }

  else if(userInput.value ===""){
    alert('provide an input');
  }
  
}

//recursive function that does a typewriter effect
function typeWriter(p,i,speed,txt) {
  if (i < txt.length) {
    p.textContent += txt.charAt(i);
    i++;
    setTimeout(()=>{
      typeWriter(p,i,speed,txt)
    }, speed);
  }
}

async function sendPrompt(text){
  response = await fetch(URL,{
    method:"POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify(text)
  }
  )
  data = await response.json()
  return data;
}


async function getPrompts(){
  response = await fetch();
}