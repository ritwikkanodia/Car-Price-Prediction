function onClickedEstimatePrice()
{
    var symboling = document.getElementById("uisymboling");
    var fueltype = document.getElementById("uifueltype");
    var aspiration = document.getElementById("uiaspiration");
    var doornumber = document.getElementById("uidoornumber");
    var carbody = document.getElementById("uicarbody");
    var drivewheel = document.getElementById("uidrivewheel");
    var enginelocation = document.getElementById("uienginelocation");
    var wheelbase = document.getElementById("uiwheelbase");
    var carlength = document.getElementById("uicarlength");
    var carwidth = document.getElementById("uicarwidth");
    console.log(symboling.value)
    var carheight = 1
    var curbweight = 1
    var enginetype = "dohc"
    var cylindernumber = 'six'
    var enginesize = 1
    var fuelsystem = 'mpfi'
    var boreratio = 1
    var stroke = 1
    var compressionratio = 1
    var horsepower = 1
    var peakrpm = 1
    var citympg = 1
    var highwaympg = 1
//    var estPrice = 1


//    var carlength = document.getElementById("uicarlength");
//    var carwidth = document.getElementById("uicarwidth");
//    var carheight = document.getElementById("uicarheight");
//    var curbweight = document.getElementById("uicurbweight");
//    var enginetype = document.getElementById("uienginetype");
//    var cylindernumber = document.getElementById("uicylindernumber");
//    var enginesize = document.getElementById("uienginesize");
//    var fuelsystem = document.getElementById("uifuelsystem");
//    var boreratio = document.getElementById("uiboreratio");
//    var stroke = document.getElementById("uistroke");
//    var compressionratio = document.getElementById("uicompressionratio");
//    var horsepower = document.getElementById("uihorsepower");
//    var peakrpm = document.getElementById("uipeakrpm");
//    var citympg = document.getElementById("uicitympg");
//    var highwaympg = document.getElementById("uihighwaympg");
    var estPrice = document.getElementById("uiEstimatedPrice");

    var url = "http://127.0.0.1:5000/predict_machine_price";

    $.post(
    url,
    {
        symboling: parseInt(symboling.value), //categorical
        fueltype: fueltype.value, //categorical
        aspiration: aspiration.value,  //categorical
        doornumber: doornumber.value,  //categorical
        carbody: carbody.value,  //categorical
        drivewheel: drivewheel.value,  //categorical
        enginelocation: enginelocation.value, //categorical
        wheelbase: parseFloat(wheelbase.value),
        carlength: parseFloat(carlength.value),
        carwidth: parseFloat(carwidth.value),
        carheight: parseFloat(carheight),
        curbweight: parseInt(curbweight),
        enginetype: enginetype, //categorical
        cylindernumber: cylindernumber, //categorical
        enginesize: parseInt(enginesize),
        fuelsystem: fuelsystem, //categorical
        boreratio: parseFloat(boreratio),
        stroke: parseFloat(stroke),
        compressionratio: parseFloat(compressionratio),
        horsepower: parseInt(horsepower),
        peakrpm: parseInt(peakrpm),
        citympg: parseInt(citympg),
        highwaympg: parseInt(highwaympg),
//        carlength: parseFloat(carlength.value),
//        carwidth: parseFloat(carwidth.value),
//        carheight: parseFloat(carheight.value),
//        curbweight: parseFloat(curbweight.value),
//        enginetype: parseInt(enginetype.value), //categorical
//        cylindernumber: parseInt(cylindernumber.value), //categorical
//        enginesize: parseFloat(enginesize.value),
//        fuelsystem: parseInt(fuelsystem.value), //categorical
//        boreratio: parseFloat(boreratio.value),
//        stroke: parseFloat(stroke.value),
//        compressionratio: parseFloat(compressionratio.value),
//        horsepower: parseFloat(horsepower.value),
//        peakrpm: parseFloat(peakrpm.value),
//        citympg: parseFloat(citympg.value),
//        highwaympg: parseFloat(highwaympg.value),
    },
    function (data, status) {
        console.log(data.estimated_price.toString())
        console.log(estPrice)
        estPrice.innerHTML =
        "<h2>" + data.estimated_price.toString() + " USD</h2>";
    }
    );

}

function getCarBodyValue() {
    return 2
}

function getFuelSystemValue() {
    return 1
}
