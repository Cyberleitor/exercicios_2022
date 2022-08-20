document.querySelectorAll('.topic').forEach(subject => {
    subject.onclick = function(e) {
        const ul = subject.nextElementSibling
        const opened = ul.style.display
        ul.style.display = opened === 'none' ? 'block' : 'none'
    }
})