const player = document.querySelector('.playerContainer');
const video = document.querySelector('.xdPlayer');
const fullscreenBtn = document.querySelector('.fullscreen');
const seek = document.getElementById('seek');
const speedbtn = document.getElementById('speedbtn');
const playButton = document.getElementById('play');
const playbackIcons = document.querySelectorAll('.playback-icons use');
const togglePlayBtn = document.querySelector('.toggle-play');
const speedBtns = document.querySelectorAll('.speed-item');
const volumeSeek = document.getElementById('volumeSeek');
const lock = document.getElementById('lock');
const unlock = document.getElementById('unlock');
const videocontrols = document.getElementById('video-controls');
const superplay = document.getElementById('superplay');
const rewbtn = document.getElementById('rew');
const forbtn = document.getElementById('for');
var textCurrent = document.querySelector('.current-time');
var duration = document.querySelector('.total-time');
var speedlist = document.querySelector('#speed-list');
let lastVolume = 1;
let isMouseDown = false;
let isSpeedSheet = false;
let isMax = false;

function togglePlay() {
    if (superplay.style.display != 'none') {
        superplay.style.display = 'none';
    }
    if (video.paused || video.ended) {
        video.play();
    } else {
        video.pause();
    }
}

function neatTime(time) {
    let minutes = Math.floor((time % 3600) / 60);
    let seconds = Math.floor(time % 60);
    seconds = seconds > 9 ? seconds : `0${seconds}`;
    return `${minutes}:${seconds}`;
}

function formatTime(timeInSeconds) {
    const result = new Date(timeInSeconds * 1000).toISOString().substr(11, 8);
    return {
        minutes: result.substr(3, 2),
        seconds: result.substr(6, 2),
    };
};

function updatePlayButton() {
    if (video.paused) {
        togglePlayBtn.innerHTML = `<svg version="1.1" id="Capa_1" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" x="0px" y="0px"
		viewBox="0 0 17.804 17.804" style="enable-background:new 0 0 17.804 17.804;" xml:space="preserve"><g><g id="c98_play"><path d="M2.067,0.043C2.21-0.028,2.372-0.008,2.493,0.085l13.312,8.503c0.094,0.078,0.154,0.191,0.154,0.313
			   c0,0.12-0.061,0.237-0.154,0.314L2.492,17.717c-0.07,0.057-0.162,0.087-0.25,0.087l-0.176-0.04
			   c-0.136-0.065-0.222-0.207-0.222-0.361V0.402C1.844,0.25,1.93,0.107,2.067,0.043z"/></g><g id="Capa_1_78_"></g></g><g></g><g></g><g></g><g></g><g></g><g></g><g></g><g></g><g></g><g></g><g></g><g></g><g></g><g></g><g></g></svg>
   `;
    } else {
        togglePlayBtn.innerHTML = `<svg version="1.1" id="Capa_1" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" x="0px" y="0px"
		viewBox="0 0 47.607 47.607" style="enable-background:new 0 0 47.607 47.607;" xml:space="preserve"><g><path d="M17.991,40.976c0,3.662-2.969,6.631-6.631,6.631l0,0c-3.662,0-6.631-2.969-6.631-6.631V6.631C4.729,2.969,7.698,0,11.36,0
		   l0,0c3.662,0,6.631,2.969,6.631,6.631V40.976z"/><path d="M42.877,40.976c0,3.662-2.969,6.631-6.631,6.631l0,0c-3.662,0-6.631-2.969-6.631-6.631V6.631
		   C29.616,2.969,32.585,0,36.246,0l0,0c3.662,0,6.631,2.969,6.631,6.631V40.976z"/></g><g></g><g></g><g></g><g></g><g></g><g></g><g></g><g></g><g></g><g></g><g></g><g></g><g></g><g></g><g></g></svg>
   `;
    }
}

function updateProgress() {
    seek.value = Math.floor(video.currentTime);
    textCurrent.innerHTML = `${neatTime(video.currentTime)}`;
    if (isMax) {} else {
        const time = formatTime(Math.round(video.duration))
        duration.innerHTML = `${time.minutes}:${time.seconds}`;
        seek.setAttribute('max', Math.round(video.duration));
        console.log(video.lenth);
        isMax = true;
    }
}

function changevolume() {
    if (video.muted) {
        video.muted = false;
    }
    video.volume = volumeSeek.value;
}

function skipAhead(event) {
    const skipTo = event.target.dataset.seek ? event.target.dataset.seek : event.target.value;
    video.currentTime = skipTo;
    seek.value = skipTo;
}

function launchIntoFullscreen(element) {
    if (element.requestFullscreen) {
        element.requestFullscreen();
    } else if (element.mozRequestFullScreen) {
        element.mozRequestFullScreen();
    } else if (element.webkitRequestFullscreen) {
        element.webkitRequestFullscreen();
    } else if (element.msRequestFullscreen) {
        element.msRequestFullscreen();
    }
}

function exitFullscreen() {
    if (document.exitFullscreen) {
        document.exitFullscreen();
    } else if (document.mozCancelFullScreen) {
        document.mozCancelFullScreen();
    } else if (document.webkitExitFullscreen) {
        document.webkitExitFullscreen();
    }
}
var fullscreen = false;

function toggleFullscreen() {
    fullscreen ? exitFullscreen() : launchIntoFullscreen(player)
    fullscreen = !fullscreen;
}

function setSpeed(e) {
    console.log(parseFloat(this.dataset.speed));
    video.playbackRate = this.dataset.speed;
    speedBtns.forEach(speedBtn => speedBtn.classList.remove('active'));
    this.classList.add('active');
}

function showSpeedSheet() {
    if (isSpeedSheet) {
        speedlist.style.display = 'none';
        isSpeedSheet = false;
    } else {
        speedlist.style.display = 'block';
        isSpeedSheet = true;
    }
}

function handleKeypress(e) {
    switch (e.key) {
        case 'p':
            togglePlay();
            break;
        case 'm':
            volumeSeek.value = 0;
            video.volume = volumeSeek.value;
            break;
        case 'f':
            toggleFullscreen();
            break;
        case 's':
            showSpeedSheet();
            break;
        case 'p':
            togglePip();
            break;
    }
}

function lockControls() {
    unlock.style.display = 'block';
    videocontrols.style.opacity = '0';
}

function unLockControls() {
    unlock.style.display = 'none';
    videocontrols.style.opacity = '.9';
}
playButton.addEventListener('click', togglePlay);
video.addEventListener('click', togglePlay);
video.addEventListener('play', updatePlayButton);
video.addEventListener('pause', updatePlayButton);
video.addEventListener('ended', togglePlay);
video.addEventListener('timeupdate', updateProgress);
video.addEventListener('canplay', updateProgress);
superplay.addEventListener('click', function() {
    superplay.style.display = 'none';
    togglePlay();
})
seek.addEventListener('input', skipAhead);
volumeSeek.addEventListener('input', changevolume);
lock.addEventListener('click', lockControls);
unlock.addEventListener('click', unLockControls);
rewbtn.addEventListener('click', function() {
    let skip = video.currentTime - 10;
    video.currentTime = skip;
    seek.value = skip;
});
forbtn.addEventListener('click', function() {
    let skip = video.currentTime + 10;
    video.currentTime = skip;
    seek.value = skip;
});
window.addEventListener('mousedown', () => isMouseDown = true)
window.addEventListener('mouseup', () => isMouseDown = false)
fullscreenBtn.addEventListener('click', toggleFullscreen);
speedbtn.addEventListener('click', showSpeedSheet);
speedBtns.forEach(speedBtn => {
    speedBtn.addEventListener('click', setSpeed);
});
window.addEventListener('keyup', handleKeypress);