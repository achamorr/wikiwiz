function pasteSelection() {

           chrome.tabs.executeScript( {
  code: "window.getSelection().toString();"
}, function(selection) {
    var text = document.getElementById('text'); 
    text.innerHTML = selection[0];;

});
 
}
pasteSelection(); 

