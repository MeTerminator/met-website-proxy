// 3D INTERACTIVE TILT & HOLOGRAM SHEEN SCRIPT

const cardWrapper = document.getElementById('pass-card-wrapper');
const charImage = document.getElementById('char-image');

// Interpolation targets and current states
let targetRx = 0, targetRy = 0;
let currentRx = 0, currentRy = 0;
let targetX = 0, targetY = 0;
let currentX = 0, currentY = 0;
let targetSheenX = 50, targetSheenY = 50;
let currentSheenX = 50, currentSheenY = 50;
let targetShadowX = 0, targetShadowY = 0;
let currentShadowX = 0, currentShadowY = 0;

// Baseline for gyroscope
let baseBeta = null;
let baseGamma = null;
let isUsingGyro = false;

// Mouse movement handler
document.addEventListener('mousemove', (e) => {
    if (!cardWrapper) return;
    // Disable mouse updates if gyroscope has taken over
    if (isUsingGyro) return;

    const rect = cardWrapper.getBoundingClientRect();
    const cardCenterX = rect.left + rect.width / 2;
    const cardCenterY = rect.top + rect.height / 2;

    const dx = e.clientX - cardCenterX;
    const dy = e.clientY - cardCenterY;

    const rangeX = window.innerWidth / 2;
    const rangeY = window.innerHeight / 2;

    const ratioX = dx / rangeX;
    const ratioY = dy / rangeY;

    targetRx = -ratioY * 14;
    targetRy = ratioX * 14;

    targetX = ratioX * -10;
    targetY = ratioY * -10;

    targetSheenX = ((e.clientX - rect.left) / rect.width) * 100;
    targetSheenY = ((e.clientY - rect.top) / rect.height) * 100;

    targetShadowX = -ratioX * 5;
    targetShadowY = -ratioY * 5;
});

document.addEventListener('mouseleave', resetCard);

function resetCard() {
    targetRx = 0;
    targetRy = 0;
    targetX = 0;
    targetY = 0;
    targetSheenX = 50;
    targetSheenY = 50;
    targetShadowX = 0;
    targetShadowY = 0;
    if (isUsingGyro) {
        baseBeta = null;
        baseGamma = null;
    }
}

// Gyroscope orientation handler
function handleOrientation(e) {
    const beta = e.beta;
    const gamma = e.gamma;

    if (beta === null || gamma === null) return;

    isUsingGyro = true;

    if (baseBeta === null) {
        baseBeta = beta;
        baseGamma = gamma;
    }

    // Calculate delta relative to baseline
    let deltaBeta = beta - baseBeta;
    let deltaGamma = gamma - baseGamma;

    // Clamp delta values to prevent excessive displacement
    const maxDelta = 20;
    deltaBeta = Math.max(-maxDelta, Math.min(maxDelta, deltaBeta));
    deltaGamma = Math.max(-maxDelta, Math.min(maxDelta, deltaGamma));

    // Map to image offsets (ratio between -1 and 1, max shift 15px)
    targetX = (deltaGamma / maxDelta) * -15;
    targetY = (deltaBeta / maxDelta) * -15;

    // Set slight tilt and shadow shifts for mobile gyro too
    targetRx = (deltaBeta / maxDelta) * -4;
    targetRy = (deltaGamma / maxDelta) * 4;
    targetShadowX = (deltaGamma / maxDelta) * -2;
    targetShadowY = (deltaBeta / maxDelta) * -2;
}

// Request Gyroscope permissions (specifically for iOS 13+)
function requestGyroPermission() {
    if (typeof DeviceOrientationEvent !== 'undefined' && typeof DeviceOrientationEvent.requestPermission === 'function') {
        DeviceOrientationEvent.requestPermission()
            .then(response => {
                if (response === 'granted') {
                    window.addEventListener('deviceorientation', handleOrientation);
                }
            })
            .catch(console.error);
    } else {
        window.addEventListener('deviceorientation', handleOrientation);
    }
}

// Request permissions on first user interaction
document.addEventListener('click', requestGyroPermission, { once: true });
document.addEventListener('touchstart', requestGyroPermission, { once: true });

// Animation Loop using requestAnimationFrame (Lerp for buttery smoothness)
function animate() {
    currentRx += (targetRx - currentRx) * 0.1;
    currentRy += (targetRy - currentRy) * 0.1;
    currentX += (targetX - currentX) * 0.1;
    currentY += (targetY - currentY) * 0.1;
    currentSheenX += (targetSheenX - currentSheenX) * 0.1;
    currentSheenY += (targetSheenY - currentSheenY) * 0.1;
    currentShadowX += (targetShadowX - currentShadowX) * 0.1;
    currentShadowY += (targetShadowY - currentShadowY) * 0.1;

    if (cardWrapper) {
        cardWrapper.style.transform = `rotateX(${currentRx}deg) rotateY(${currentRy}deg)`;
        cardWrapper.style.setProperty('--sheen-x', `${currentSheenX}%`);
        cardWrapper.style.setProperty('--sheen-y', `${currentSheenY}%`);
        cardWrapper.style.setProperty('--shadow-shift-x', `${currentShadowX}%`);
        cardWrapper.style.setProperty('--shadow-shift-y', `${currentShadowY}%`);
    }

    if (charImage) {
        charImage.style.transform = `translateZ(50px) translate(${currentX}px, ${currentY}px) scale(1.05)`;
    }

    requestAnimationFrame(animate);
}

// Start animation loop
animate();
