// function myFunction() {
//   console.log("clicked");
//   var element = document.getElementById("menu-container-dropdown-id");

//   if (element.classList) { 
//     element.classList.toggle("menu-container-dropdown-display-non-class");
//   } else {
//     var classes = element.className.split(" ");
//     var i = classes.indexOf("menu-container-dropdown-display-non-class");

//     if (i >= 0) 
//       classes.splice(i, 1);
//     else 
//       classes.push("menu-container-dropdown-display-non-class");
//       element.className = classes.join(" "); 
//   }
// }


// function removeDropdownHidingClass(){
//      var element = document.getElementById("menu-container-dropdown-id");
//      if (window.matchMedia("(max-width: 892px)").matches) {
//         /* The viewport is less than, or equal to, 700 pixels wide */
//         element.classList.remove("menu-container-dropdown-display-non-class");
//       } else {
//         /* The viewport is greater than 700 pixels wide */
//       }

// }


// function hide_follow_icons_scroll(){
//   var follow_icons_container = document.getElementById('article-details-follow-midea-cons-id');
//   console.log(follow_icons_container.offsetTop);
//   console.log(window.pageYOffset);

//     if (window.pageYOffset>=300 && window.pageYOffset<=900) {
//       console.log('less or equal 300')
//       follow_icons_container.classList.add("article-details-follow-midea-cons-non-fixed")
//       } else {
//       follow_icons_container.classList.remove("article-details-follow-midea-cons-non-fixed");
//       }
// }

// This code checks to see if any images from the article are too big and overflows, if they do, it make them responsive by making their width 100%
var el = document.querySelectorAll(".blogdetails-content img");
var el2 = document.querySelector(".blogdetails-content");

el.forEach(element => {
  if (element.clientWidth > el2.clientWidth) {
    console.log(element);
    element.style.width = "100%";
    
  }
});
// -----------------------------------------
