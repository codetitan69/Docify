var input = document.querySelector("#url-form #url")

var submit = document.querySelector("#url-form #submit")

// submit.addEventListener('click',function () {
//     input.value = ""
// })

window.addEventListener('pageshow', function (event) {
  if (event.persisted) {
    // Page was restored from bfcache (back/forward)
    input.value = "";
  }
});