// Заносим видео через класс в переменную (для работы gsap)

// const video = document.querySelector('.video-background')
//
// const swiperText = new Swiper('.swiper', {
// 	speed: 1600,
//
// 	mousewheel: {},
// 	pagination: {
// 		el: '.swiper-pagination',
// 		clickable: true
// 	},
// 	navigation: {
// 		prevEl: '.swiper-button-prev',
// 		nextEl: '.swiper-button-next'
// 	}
// })
//
// // Привязываем смену слайдов к анимации видео
// swiperText.on('slideChange', function() {
// 	// применяем gsap к видео, 1.6s равна времени пролистывания в настройках swiper
// 	gsap.to(video, 1.6, {
// 		// чтобы узнать начало текущего фрагмента видео текущего сkайда,
// 		// длительность видео делим на количество слайдов и умножаем на тндекс текущего слайда
// 		currentTime: (video.duration / (this.slides.length - 1)) * this.realIndex,
// 		ease: Power1.easeOut
// 	})
// })

const video = document.querySelector('.video-background')

video.addEventListener('loadedmetadata', function() {
	const swiperText = new Swiper('.swiper', {
		speed: 1600,
		mousewheel: {  },
		pagination: {
			el: '.swiper-pagination',
			clickable: true
		},
		navigation: {
			prevEl: '.swiper-button-prev',
			nextEl: '.swiper-button-next'
		}
	})


	swiperText.on('slideChange', function() {
		const targetTime = (video.duration / (this.slides.length - 1)) * this.realIndex;

		gsap.to(video, {
			duration: 1.6,
			currentTime: targetTime,
			ease: Power2.ease,
			onUpdate: function() {
				video.currentTime = gsap.getProperty(video, "currentTime");
			}
		})
	})

		// Уменьшаем opacity при начале анимации
	swiperText.on('slideChangeTransitionStart', function() {
		// добавляем к видео класс chango
		video.classList.add('change')
	}).on('slideChangeTransitionEnd', function() {
		video.classList.remove('change')
	})
})

// // Уменьшаем opacity при начале анимации
// swiperText.on('slideChangeTransitionStart', function() {
// 	// добавляем к видео класс chango
// 	video.classList.add('change')
// }).on('slideChangeTransitionEnd', function() {
// 	video.classList.remove('change')
// })