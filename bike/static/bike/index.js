document.addEventListener("DOMContentLoaded", () => {
    const lockButton = document.querySelector('#lockbtn');
    lockButton.style.visibility = 'hidden';
    const lockButtonStatus = document.querySelector('#lockbtnstatus');
    lockButtonStatus.style.visibility = 'hidden';
    for (let i = 1; i < 9; i++) {

    }

    let spinners = document.getElementsByClassName("spinner-grow");
    for (let i = 0; i < spinners.length; i++) {
        fetch(`status/${spinners[i].id}`)
            .then(response => response.json())
            .then(lot_info => {
                console.log(lot_info.occupied)
                if (lot_info.occupied === "Yes") {
                    spinners[i].className = "spinner-grow text-danger";
                }
                else {
                    spinners[i].className = "spinner-grow text-success";
                }
            })
        spinners[i].addEventListener("click", () => changeSpinner(spinners[i]));
    }

    lockButton.addEventListener("click", () => changeLockStatus(lockButton, lockButtonStatus));

})

function changeLockStatus(btn1, btn2) {
    if (btn1.innerHTML === "Unlock Bike") {
        btn1.className = "btn btn-success";
        btn1.innerHTML = "Lock Bike";
        btn2.className = "badge rounded-pill bg-danger";
        btn2.innerHTML = "Unlocked";
        const lockNo = document.querySelector('#LockNumber').innerHTML;
        fetch(`unlock/${lockNo}`)
            .then(response => response.json())
            .then(lot => {
                console.log(lot)
            })
    }

    else if (btn1. innerHTML === "Lock Bike") {
        btn1.className = "btn btn-danger";
        btn1.innerHTML = "Unlock Bike";
        btn2.className = "badge rounded-pill bg-success";
        btn2.innerHTML = "Locked";
        const lockNo = document.querySelector('#LockNumber').innerHTML;
        fetch(`lock/${lockNo}`)
            .then(response => response.json())
            .then(lot => {
                console.log(lot)
            })
    }
}


function changeSpinner(button) {

    if (button.className === "spinner-grow text-success") {
        document.querySelector('#lockbtnstatus').style.visibility = 'visible';
        document.querySelector('#lockbtn').style.visibility = 'visible';
        button.className = "spinner-grow text-warning";
        fetch(`status/${button.id}`)
            .then(response => response.json())
            .then(lot_info => {
                console.log(lot_info);
                const lotType = document.querySelector("#LotType");
                if (lot_info.type === "LT") {
                    lotType.innerHTML = "Long-term";
                }
                else if (lot_info.type === "ST") {
                    lotType.innerHTML = "Short-term";
                }
                document.querySelector("#LockNumber").innerHTML = lot_info.number;

            })

    }
    else if (button.className === "spinner-grow text-warning") {
        button.className = "spinner-grow text-success";
    }

}

