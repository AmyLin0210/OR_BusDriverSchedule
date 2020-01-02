function subscribeRouteButton () {
    document.querySelectorAll('.driver__driver-select > .driver-select__driver-name > .driver-name__item').forEach((element)=> {
        element.addEventListener("click", ()=> {
            let date = document.getElementById("schedule_week").value
            let driver_id = element.getAttribute("driver_id")
            let url = `http://${window.location.host}/driver_schedule/${date}/${driver_id} `
            window.location.href = url;
        })
    });
    document.getElementById("driver-name_title").addEventListener("click", ()=> {
        let item = document.getElementById("driver-name_item")
        if(item.classList.contains("driver-select__driver-name--hidden")) {
            item.classList.remove("driver-select__driver-name--hidden")
        }
        else {
            item.classList.add("driver-select__driver-name--hidden")
        }
    })
}

subscribeRouteButton();