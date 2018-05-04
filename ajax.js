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


