var x=document.querySelector("p")
//show textContent
x.textContent
//reassign text
x.textContent="new"

// Refresh the page
// Show actual HTML
x.innerHTML

// Edit HTML
x.innerHTML = "This is <strong>BOLD</strong>"

// Can't do that with just textContent

/////////////////
// Attributes //
///////////////

var special = document.querySelector("#special")
var specialA = special.querySelector("a")

specialA.getAttribute("href")

specialA.setAttribute("href","https://www.amazon.com")
