/*

Inspired by Florin Pop's coding challenges, you can check them here: https://www.florin-pop.com/blog/2019/03/weekly-coding-challenge/

= Pagination short logic description =
 
  We set collection of our pages as an array of objects.
  Each object is a page with properties:
    * id - used as identifier
    * text - HTML page content
    * active - flag for page that is currently rendered.
 
  Logic is to check which object is flagged active and render that page.
 
  Page gets flagged as active by button click events.
 
  Buttons are rendered according to pages - for every page we create one button with:
    * corresponding number as text
    * corresponding ID as a button title.
 
  Rest are button click events for switching pages.
*/

// Pages and their content
let pages = [
    {id: 1, text: "<h3>PAGE 1</h3> <p>When life gives you lemon throw it back, and ask for a college life once again where you could have earned your farewell without a \"bat\" coming all the way from China and hindering your way. 4 years isn't a small time yet when you look back , tons of things are still left to to be completed and cherished . As Naina told you years back, \"life mein jitna bhi try kar lo kuchh Na kuchh to chhutega hi !!!\". None the less college life gave you millions of memories, pain, gossips,smiles and love in the past four years from your junior senior and batchmates and gave you a home away from home.</p><p>so why not sit back, close your eyes and relax and let us dive deep into the four year long memory lane of your college life to relish and re live every memory that you created years and months ago which still seems like yesterday. Here is the team of Litsoc not in front of you , but in your hearts re-creating memories which begins from jam nights and ends with games like Scrabble, word puzzle, biggest liar and \" baba ki Bakar\" , \"wittyness of Param sir\", \"Shivam sir\'s literature\", \"Chirag sir\'s lapdance\", \"Siddharth sir ki vocabulary\" and other great names, great talents.</p><p>I know there's a lot that you have missed, a lot was left yet to complete, and a lot that you maybe are regretting now. You missed what you deserved. Seems like you were denied that fruit which you planted and watered from years. You are ones who did gazillions of things for the college, for our college, took these primary clubs from level0 to level1 or maybe more(you know words always fail to express your sentiments fully, you surely do know!).In every small-big possible way, you contributed for the development of a newly grown IIT.But, fate had decided something else for you.</p><p>To our Litsoc seniors , I know you have missed a lot. Your dreams of last semester's tomfoolery, last college trips with your friends, last hug from your college juniors on your last day of college, graduation dinners, GPL of friends, and a lot lot lot more. For four years , IIT Mandi proved to be not just your college but home, juniors were not just students but your siblings, alumni were not just seniors but your guardians in times of crisis and collegues were not just friends but proved out to be brothers and sisters. Though everything was not as beautiful as I'm writing , I know it was full of ups and downs and at times you fought them all alone despite of being surrounded by everyone, but yet you pulled out the best out of yourselves and cheerfully succeded to make it to your final years.I know it would be a nightmare for you all to wake up one day just 5 minutes before 9 and instead of rushing to your classes in loose pyjamas and sleepy eyes, you all would be rushing for your office with unknotted ties and messed up files in your folder.My pen feels so heavy to sum up these things yet all these writings are so insignificant compared to what are going through right now.</p><p>But you know, you would prove to be the best of all batches because you have witnessed the pain of separation, devastation, rejection , denial and distances. You are ones who will have multiples of success stories to tell to your next generations because you knew how to make things work despite of miles of physical distances from each other and yet being so close. This lockdown taught mankind millions of small things and you are ones who were hit and got over it.</p>", active: true},
    {id: 2, text: "<h3>PAGE 2</h3> <p>Lorem ipsum dolor sit amet consectetur adipisicing elit. Deleniti id impedit natus at! Necessitatibus voluptatem rerum repellat adipisci molestiae totam.</p>", active: false},
    {id: 3, text: "<h3>PAGE 3</h3> <p>Lorem ipsum dolor sit amet consectetur adipisicing elit. Deleniti id impedit natus at! Necessitatibus voluptatem rerum repellat adipisci molestiae totam.</p>", active: false},
    {id: 4, text: "<h3>PAGE 4</h3> <p>Lorem ipsum dolor sit amet consectetur adipisicing elit. Deleniti id impedit natus at! Necessitatibus voluptatem rerum repellat adipisci molestiae totam.</p>", active: false},
    {id: 5, text: "<h3>PAGE 5</h3> <p>Lorem ipsum dolor sit amet consectetur adipisicing elit. Deleniti id impedit natus at! Necessitatibus voluptatem rerum repellat adipisci molestiae totam.</p>", active: false}
  ];
  
  // UI Elements
  const pagesContainer = document.querySelector(".pages"),
        buttonsContainer = document.querySelector(".paginator"),
        numButtonsContainer = document.querySelector(".page-nums");
  
  
  // Clear pages
  function clearPages() {
    while(pagesContainer.firstChild) {
      pagesContainer.firstChild.remove();
    }
  }
  
  // Clear Buttons
  function clearButtons() {
    while(numButtonsContainer.firstChild) {
      numButtonsContainer.firstChild.remove();
    }
  }
  
  // Render buttons
//   function renderButtons(activePage) {
//     clearButtons();
   
//     pages.forEach(function(current) {
//       const button = document.createElement("button");
//       button.className = "page-num";
//       button.type = "button";
//       button.title = current.id;
//       button.textContent = current.id;
     
//       if(current.id === activePage.id) {
//         button.classList.add("active");
//       } else {
//           button.classList.remove("active");
//       }
     
//       numButtonsContainer.appendChild(button);
//     })
//   }
  
  // Main render
  function render() {
    clearPages();
   
    let activePage = pages.find(function(current) {
      return current.active === true;
    })
   
    const div = document.createElement("div");
    div.className = "page";
    div.dataset.id = activePage.id;
    div.innerHTML = activePage.text;
   
    pagesContainer.appendChild(div);
   
    setTimeout(function() {
      div.classList.add("active");
    }, 10);
   
    renderButtons(activePage)
  }
  
  // Event listeners for button clicks
  
  // Buttons with page numbers click event
  numButtonsContainer.addEventListener("click", function(e) {
    if(e.target.classList.contains("page-num")) {
     
      const activePage = pages.find(function(current) {
        return current.active;
      })
     
      if(e.target.title != activePage.id) {
       
        pages.forEach(function(current) {
         current.active = false;
       })
       
        pages[e.target.title - 1].active = true;
        render();
      }
    }
  })
  
  // Arrow buttons click event
  buttonsContainer.addEventListener("click", function(e) {
    let activePage = pages.find(function(current) {
        return current.active === true;
      });
   
    if(e.target.className === "arrow-left") {
     
      if(pages[0].active === true) {
        pages[activePage.id - 1].active = false;
        pages[pages.length - 1].active = true;
        render();
       
      } else {
          pages[activePage.id - 1].active = false;
          pages[(activePage.id - 1) - 1].active = true;
          render();
        }
     
    } else if(e.target.className === "arrow-right") {
        if(pages[pages.length - 1].active === true) {
          pages[activePage.id - 1].active = false;
          pages[0].active = true;
          render();
          
        } else {
            pages[activePage.id - 1].active = false;
            pages[(activePage.id - 1) + 1].active = true;
            render();
          }
     
    } else return;
  })
  
  // Initial render of the app
  render();