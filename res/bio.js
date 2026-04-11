function switchTo(type) {
    const main = document.getElementById('main-card');
    const furry = document.getElementById('furry-card');
    const navMain = document.getElementById('nav-main');
    const navFurry = document.getElementById('nav-furry');

    if (type === 'furry') {
        const activeCard = main;
        const targetCard = furry;
        const activeNav = navMain;
        const targetNav = navFurry;

        activeCard.classList.remove('active');
        targetCard.classList.add('active');
        activeNav.classList.remove('active');
        targetNav.classList.add('active');
        window.location.hash = 'furry';
    } else {
        const activeCard = furry;
        const targetCard = main;
        const activeNav = navFurry;
        const targetNav = navMain;

        activeCard.classList.remove('active');
        targetCard.classList.add('active');
        activeNav.classList.remove('active');
        targetNav.classList.add('active');
        window.location.hash = 'main';
    }
}

function toggleSelector() {
    const wrapper = document.getElementById('selector-wrapper');
    const toggle = document.getElementById('selector-toggle');
    const isExpanded = wrapper.classList.toggle('expanded');
    toggle.classList.toggle('active');
}

function copyQQ(num) {
    navigator.clipboard.writeText(num).then(() => {
        const toast = document.getElementById('toast');
        toast.classList.add('show');
        setTimeout(() => toast.classList.remove('show'), 2000);
    });
}

window.addEventListener('DOMContentLoaded', () => {
    const hash = window.location.hash.replace('#', '');
    switchTo(hash === 'furry' ? 'furry' : 'main');

    const urlParams = new URLSearchParams(window.location.search);
    if (document.referrer && !urlParams.has('ref')) {
        urlParams.append('ref', document.referrer);
    }

    if (urlParams.toString()) {
        document.querySelectorAll('a[href^="http"]').forEach(a => {
            try {
                const linkUrl = new URL(a.href);
                if (linkUrl.hostname.includes('met6.top')) {
                    urlParams.forEach((value, key) => {
                        if (!linkUrl.searchParams.has(key)) {
                            linkUrl.searchParams.append(key, value);
                        }
                    });
                    a.href = linkUrl.toString();
                }
            } catch (e) {
                console.error("URL 解析失败:", e);
            }
        });
    }
});

window.addEventListener('hashchange', () => {
    const hash = window.location.hash.replace('#', '');
    switchTo(hash === 'furry' ? 'furry' : 'main');
});
