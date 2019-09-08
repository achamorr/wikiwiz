var t = '';
function gText(e) {
    t = (document.all) ? document.selection.createRange().text : document.getSelection();
    // document.getElementById('input').value = t;
    console.log(t)
}  
document.onmouseup = gText;
if (!document.all) document.captureEvents(Event.MOUSEUP);
||||||| merged common ancestors
chrome.runtime.onMessage.addListener(
    function(request, sender, sendResponse) {
      if( request.message === "clicked_browser_action" ) {
        var firstHref = $("a[href^='http']").eq(0).attr("href");
  
        console.log(firstHref);
      }
    }
  );
