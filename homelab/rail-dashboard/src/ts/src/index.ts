const timeObject = {
    currentTime: new Date().toLocaleTimeString()
};


function updateTime() {
    timeObject.currentTime = new Date().toLocaleTimeString();
    document.getElementById("time")!.textContent = timeObject.currentTime;
}


setInterval(updateTime, 1000)