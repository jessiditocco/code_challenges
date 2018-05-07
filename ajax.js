$.get("/adjective", function(data) {
    alert(data);
});

//////////////////// Javascript with AJAX////////////////////////////

function replaceAdjective(results) {
    let adjective = results;
    $('#adjective').html(adjective)
}

function getAdjective() {
    $.get("/adjective", replaceAdjective);
}

getAdjective();

//////////////////// Javascript with AJAX E2. /////////////////////////

function replaceStates(result) {
    let status = result;
    $("#order-status").html(status);
    console.log("Finished replaceStatus");
}

function updateStatus () {
    $.get("/status", {order: 123}, replaceStatus);
    console.log("Finished sending AJAX");
}

$("#update-status").on("click", updateStatus);


//////////////////// Javascript with AJAX-- Post/////////////////////////

function showOrderResults(result) {
    alert(result);
} 

function submitOrder(evt) {
    evt.preventDefault();

    let formInputs = {
        "type": $("#type-field").val(), 
        "amount" $("#amount-field").val(),
    };

    $.post("/new-order", formInputs, showOrderResults);

}

$("#order-form").on("submit", submitOrder);

//////////////////// Delivery Time /////////////////////////

function showDeliveryInfo(data) {
    let days = data["days"];
    let cost = data["cost"];
    alert('This will arive in' + days + "days");
    alert('This will cost' + cost);
}

function getDeliveryInfo(evt) {
    evt.preventDefault();
    let formValues = $("#color-form").serialize();

    $.get("/deliver-info.json", formValues, showDeliveryInfo);
}

$("#delivery-form").on("submit", getDeliveryInfo);

//////////////////// You can also write AJAX with inline functions ///////////////////

function showInfo(results) {
    alert("Melon type:" + results);
}

function getMelonInfo() {
    $.get("/melon-info", showInfo);
}

function getMelonInfo() {
    $.get("/melon-info", function(results) {
       alert("Melon type:" + results);
    });
}