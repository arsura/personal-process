var startTime;
var endTime;

window.onload = function () {
    document.getElementById('stop-btn').disabled = true;
}

function getCheckBoxVal() {
    var checkedValue = null;
    var inputElements = document.getElementsByClassName('checkbox');
    for (var i = 0; inputElements[i]; ++i) {
        if (inputElements[i].checked) {
            checkedValue = inputElements[i].value;
            break;
        }
    }
    return checkedValue;
}

function enableCheckbox() {
    var inputElements = document.getElementsByClassName('checkbox');
    for (var i = 0; inputElements[i]; ++i) {
        if (inputElements[i].checked == true) {
            return false;
        }
    }
    for (var j = 0; inputElements[j]; ++j) {
        inputElements[j].disabled = false;
    }
    return true;
}

function switchState() {
    if (enableCheckbox()) {
        return;
    }
    var inputElements = document.getElementsByClassName('checkbox');
    for (var i = 0; inputElements[i]; ++i) {
        if (inputElements[i].checked != true) {
            inputElements[i].disabled = true;
        }
    }
}

function writeData(assignment, process, comment) {
    var duration = (endTime - startTime) / 1000;
    var id = startTime.getTime();
    
    firebase.database().ref(assignment + '/' + id).set({
        Process: process,
        StartTime: String(startTime),
        StopTime: String(endTime),
        Duration: duration,
        Comment: comment
    });
}

function submit() {
    var checkedValue = getCheckBoxVal();
    var assignment = document.getElementById('assignment').value;
    var duration = (endTime - startTime) / 1000;
    var comment = document.getElementById('comment-txt').value;

    if (checkedValue == null || assignment == '' || String(startTime) == '' || String(endTime) == '') {
        alert('please check your input data')
        return;
    }
    writeData(assignment, checkedValue, comment);
    alert('write data complete')
    //location.reload();
}

function startTimer() {
    document.getElementById('time-show').innerHTML = '<div id="start-time" class="show-time-txt"></div><div id="end-time" class="show-time-txt"></div><div id="duration" class="show-time-txt"></div>';
    startTime = new Date();
    document.getElementById('start-time').innerHTML = startTime;

    // start-btn 'true' then stop-btn 'false'
    document.getElementById('start-btn').disabled = true;
    document.getElementById('stop-btn').disabled = false;
}

function stopTimer() {
    endTime = new Date();
    document.getElementById('end-time').innerHTML = endTime;
    var duration = (endTime - startTime) / 1000;
    document.getElementById('duration').innerHTML = duration + ' sec';

    // start-btn 'false' then stop-btn 'true'
    document.getElementById('stop-btn').disabled = true;
    document.getElementById('start-btn').disabled = false;
}