/*
  Here first i created four arrays for each city with paths used for image slidrs.
  Then deffining function to manage current index of images in each slider starting with an index set to 0 then 
  incrementing it by 1 each time function is called.
  And at bottom calling out the function and setting diferent intervals for each slider.
 */

const londonimg = [
    "/static/images/london1.png",
    "/static/images/london2.png"
];

const glasgowimg = [
    "/static/images/glasgow1.png",
    "/static/images/glasgow2.png"
];

const dublinimg = [
    "/static/images/dublin1.png",
    "/static/images/dublin2.png"
];

const cardiffimg = [
    "/static/images/cardiff1.png",
    "/static/images/cardiff2.png"
];

function startSlider(elementId, images, interval) {
    let currentIndex = 0;
    const sliderElement = document.getElementById(elementId);

    if (!sliderElement) return;

    function changeImage() {
        const img = sliderElement.querySelector("img");
        img.src = images[currentIndex];
        currentIndex = (currentIndex + 1) % images.length;

        setTimeout(changeImage, interval);
    }
    changeImage();
}

startSlider("london-slider", londonimg, 3000);
startSlider("glasgow-slider", glasgowimg, 2500);
startSlider("dublin-slider", dublinimg, 3500);
startSlider("cardiff-slider", cardiffimg, 3100);