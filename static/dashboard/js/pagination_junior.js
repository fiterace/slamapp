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
    {id: 1, text: "<h3>PAGE 1</h3> <p></p>", active: true},
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