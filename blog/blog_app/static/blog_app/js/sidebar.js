let recentButton = document.getElementById("recent");
let popularButton = document.getElementById("popular");
let recentPosts = document.getElementsByClassName('recent');
let popularPosts = document.getElementsByClassName('popular');
recentButton.onclick = () => {
    for (let i = 0; i < recentPosts.length; i++) {
        recentPosts[i].style.display = 'block'
    };
    for (let i = 0; i < popularPosts.length; i++) {
        popularPosts[i].style.display = 'none'
    };
};

popularButton.onclick = () => {
    console.log('popular')
    for (let i = 0; i < recentPosts.length; i++) {
        recentPosts[i].style.display = 'none'
    };
    for (let i = 0; i < popularPosts.length; i++) {
        popularPosts[i].style.display = 'block'
    };
};