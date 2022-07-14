if ('serviceWorker' in navigator){
    navigator.serviceWorker.register('serviceworker.js')
    .then(reg => console.log('ServiceWorker Successfull installed :)', reg))
    .catch(err => console.warn('Error', err))
}