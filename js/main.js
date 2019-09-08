chrome.app.runtime.onLaunched.addListener(function(){
    console.log(window.getSelection())
    console.log('hello')
    chrome.app.window.create('test.html', {
        innerBounds: {
            'width' : 1280,
            'height' : 800
        }
    })
})