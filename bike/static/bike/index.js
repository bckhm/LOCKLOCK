document.addEventListener("DOMContentLoaded", () => {
    const lockButton = document.querySelector('#lockbtn');
    const lockButtonStatus = document.querySelector('#lockbtnstatus');
    lockButton.addEventListener("click", () => changeLockStatus(lockButton, lockButtonStatus));
})

function changeLockStatus(btn1, btn2) {
    if (btn1.innerHTML === "Unlock Bike") {
        btn1.className = "btn btn-success";
        btn1.innerHTML = "Lock Bike";
        btn2.className = "badge rounded-pill bg-danger";
        btn2.innerHTML = "Unlocked";
    }

    else {
        btn1.className = "btn btn-danger";
        btn1.innerHTML = "Unlock Bike";
        btn2.className = "badge rounded-pill bg-success";
        btn2.innerHTML = "Locked";
    }
}
