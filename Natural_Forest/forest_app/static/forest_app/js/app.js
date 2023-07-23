// Привязываем позицию мыши к позиции сцены (передать в css)
document.addEventListener('mousemove', e => {
    // Object.assign() - позволяет применить нужные параметры объекту
    // documentElement - самый корневой элемент (root html)
    Object.assign(document.documentElement, {
        // Ширину и высоту экрана делим на 2, находим центр //
        style: `
        --move-x: ${(e.clientX - window.innerWidth / 2) * -.005}deg;
        --move-y: ${(e.clientY - window.innerHeight / 2) * -.01}deg;
        `
    })
})
