gsap.registerPlugin(ScrollTrigger, ScrollSmoother)

// // праверяем если не мобильное устройство инициализируем ScrollSmoother (на мобильных получается отключаем)
// if (ScrollTrigger.isTouch !== 1) {
// 		// инициализируем ScrollSmoother
// 	ScrollSmoother.create({
// 		// задаём облочку внутри которой элементы будут плавать
// 		wrapper: '.wrapper',
// 		// то что будет плавать внутри враппера
// 		content: '.content',
// 		// скорость скролла
// 		smooth: 1.5,
// 		// применение различных эффектов к отдельным элементам
// 		effects: true,
// 	});
//
// 	// to - указываем куда должен придти обьект анимации конечная точка, from - откуда,
// 	// fromTo - указываем начальную и конечную точкн
// 	// первые скобки = значения до анимации, вторые - после
// 	gsap.fromTo('.hero-section', { opacity: 1 }, {
// 		opacity: 0,
// 		// обьект конфигурации ScrollTrigger
// 		scrollTrigger: {
// 			// указываем тригер который должен появиться во вьюпорте
// 			trigger: '.hero-section',
// 			// позиция элемента во вьюпорте для срабатывания тригера
// 			// Могут быть разные значения для позиции, например, start: 'top center',
// 			// что означает, что анимация начнется, когда верх элемента окажется в середине окна.
// 			start: 'center',
// 			// позиция элемента относительно вьюпорта для окончания действия анимации, Можно настроить конец анимации с помощью различных параметров, например, end: 'top 50%', что остановит анимацию, когда верхняя часть элемента будет на 50% высоты окна просмотра.
// 			end: '820',
// 			// scrub определяет, синхронизируется ли анимация с прокруткой страницы.
// 			scrub: true
// 		}
// 	})
// 	// это утилита из GSAP, которая принимает строку-селектор (или NodeList/HTMLCollection) и возвращает массив из элементов, соответствующих этому селектору.
// 	let itemsL = gsap.utils.toArray('.gallery__left .gallery__item')
//
// 	itemsL.forEach(item => {
// 		gsap.fromTo(item, {x: -50, opacity: 0 }, {
// 			opacity: 1, x: 0,
// 			scrollTrigger: {
// 				trigger: item,
// 				start: '-850',
// 				end: '-100',
// 				scrub: true
// 			}
// 		})
// 	})
//
// 	let itemsR = gsap.utils.toArray('.gallery__right .gallery__item')
//
// 	itemsR.forEach(item => {
// 		gsap.fromTo(item, {x: 50, opacity: 0 }, {
// 			opacity: 1, x: 0,
// 			scrollTrigger: {
// 				trigger: item,
// 				start: '-850',
// 				end: '-100',
// 				scrub: true
// 			}
// 		})
// 	})
//
// }

ScrollSmoother.create({
	// задаём облочку внутри которой элементы будут плавать
	wrapper: '.wrapper',
	// то что будет плавать внутри враппера
	content: '.content',
	// скорость скролла
	smooth: 1.5,
	// применение различных эффектов к отдельным элементам
	effects: true,
});

// to - указываем куда должен придти обьект анимации конечная точка, from - откуда,
// fromTo - указываем начальную и конечную точкн
// первые скобки = значения до анимации, вторые - после
gsap.fromTo('.hero-section', { opacity: 1 }, {
	opacity: 0,
	// обьект конфигурации ScrollTrigger
	scrollTrigger: {
		// указываем тригер который должен появиться во вьюпорте
		trigger: '.hero-section',
		// позиция элемента во вьюпорте для срабатывания тригера
		// Могут быть разные значения для позиции, например, start: 'top center',
		// что означает, что анимация начнется, когда верх элемента окажется в середине окна.
		start: 'center',
		// позиция элемента относительно вьюпорта для окончания действия анимации, Можно настроить конец анимации с помощью различных параметров, например, end: 'top 50%', что остановит анимацию, когда верхняя часть элемента будет на 50% высоты окна просмотра.
		end: '820',
		// scrub определяет, синхронизируется ли анимация с прокруткой страницы.
		scrub: true
	}
})
// это утилита из GSAP, которая принимает строку-селектор (или NodeList/HTMLCollection) и возвращает массив из элементов, соответствующих этому селектору.
let itemsL = gsap.utils.toArray('.gallery__left .gallery__item')

itemsL.forEach(item => {
	gsap.fromTo(item, {x: -50, opacity: 0 }, {
		opacity: 1, x: 0,
		scrollTrigger: {
			trigger: item,
			start: '-850',
			end: '-100',
			scrub: true
		}
	})
})

let itemsR = gsap.utils.toArray('.gallery__right .gallery__item')

itemsR.forEach(item => {
	gsap.fromTo(item, {x: 50, opacity: 0 }, {
		opacity: 1, x: 0,
		scrollTrigger: {
			trigger: item,
			start: '-850',
			end: '-100',
			scrub: true
		}
	})
})
