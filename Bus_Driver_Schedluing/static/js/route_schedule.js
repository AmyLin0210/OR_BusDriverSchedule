function subscribeRouteButton () {
    document.querySelectorAll('.route__list > .list__route-name > .route-name__item').forEach((element)=> {
        element.addEventListener("click", ()=> {
            let date = document.getElementById("schedule_date").value
            let route_id = element.getAttribute("route_id")
            let url = `http://${window.location.host}/master_list/${date}/${route_id} `
            console.log(url)
            window.location.href = url;
        })
    });
}

subscribeRouteButton();