window.onload = function () {
    var query = firebase.database().ref().orderByKey();
    query.once("value")
        .then(function (snapshot) {
            snapshot.forEach(function (childSnapshot) {

                if (isAssignment(childSnapshot.key) == false) return;

                document.getElementsByClassName('alignleft')[0].innerHTML += '<b>' + childSnapshot.key + '</b> <br><br> <b>Process</b> <br>';
                document.getElementsByClassName('alignright')[0].innerHTML += '<br><br><b>Time(s)</b><br>';
                var i = 1;
                childSnapshot.forEach(function (childAgian) {
                    if (childAgian.key == 'summary') {
                        document.getElementsByClassName('alignleft')[0].innerHTML += '<b>Summary</b><br>';
                        document.getElementsByClassName('alignright')[0].innerHTML += '<br>';
                        childAgian.forEach(function (summary) {
                            document.getElementsByClassName('alignleft')[0].innerHTML += summary.key + '<br>';
                            document.getElementsByClassName('alignright')[0].innerHTML += summary.val() + '<br>';
                        });
                    }
                    else if (childAgian.key == 'varstats') {
                        childAgian.forEach(function (varstats) {
                            document.getElementsByClassName('alignleft')[0].innerHTML += '<b>' + varstats.key + '</b><br>';
                            document.getElementsByClassName('alignright')[0].innerHTML += varstats.val() + '<br>';                                                                          
                        });
                    }
                    else {
                        document.getElementsByClassName('alignleft')[0].innerHTML += i + '. ' + childAgian.val().Process + '<br>';
                        document.getElementsByClassName('alignright')[0].innerHTML += childAgian.val().Duration + '<br>';
                    }
                    i = i + 1;
                });
                document.getElementsByClassName('alignleft')[0].innerHTML += '<br><br>';
                document.getElementsByClassName('alignright')[0].innerHTML += '<br><br>';
            });
        });
}

function isAssignment(rootname) {
    // ES6 Substring style
    var string = rootname;
    if (string.includes("all_varstats") || 
        string.includes("funct_count") || 
        string.includes("lines_count")) {
        return false;
    }
    return true;
}

function update() {
    var query = firebase.database().ref().orderByKey();
    query.once("value")
        .then(function (snapshot) {
            snapshot.forEach(function (childSnapshot) {
                //console.log(childSnapshot.key)
                if (isAssignment(childSnapshot.key) == false) return;

                var process = { "Design": 0, "Code": 0, "Test": 0, "Debug": 0 };
                var durationList = [];
                childSnapshot.forEach(function (childAgian) {
                    if (childAgian.key == 'summary' || childAgian.key == 'varstats') return;
                    // sum value each process -> summary

                    var duration = childAgian.val().Duration;
                    process[String(childAgian.val().Process)] += duration;
                    durationList.push(duration);
                });
                firebase.database().ref(childSnapshot.key + '/' + 'summary').set({
                    Design: Math.round(process['Design'] * 100) / 100,
                    Code: Math.round(process['Code'] * 100) / 100,
                    Test: Math.round(process['Test'] * 100) / 100,
                    Debug: Math.round(process['Debug'] * 100) / 100
                });
                varstats(durationList, childSnapshot.key);
            });
        });
}

function varstats(durationList, rootName) {

    durationList.sort(function (a, b) { return a - b });
    var MinMax = minMax(durationList);
    var Average = average(durationList);
    var Std = stdev(durationList);
    var Med = median(durationList);
    var QT = quartile(durationList);
    var PT = percentile(durationList);

    firebase.database().ref(rootName + '/' + 'varstats').set({
        Min: MinMax[0],
        Max: MinMax[1],
        Average: Average,
        StandardDeviation: Std,
        Median: Med,
        Quartile: QT,
        Percentile: PT
    });
}

function percentile(durationList) {
    PT = [];
    var len = durationList.length;
    for (var i = 10; i <= 90; i += 10) {
        var P = (i / 100) * (len + 1);
        if (P - Math.floor(P) == 0.0) {
            PT.push(durationList[P - 1]);
        }
        else if (P < 1) { 
            PT.push(durationList[0]);
        }
        else if (P > len) {
            PT.push(durationList[len - 1]);
        }
        else {
            var t1 = (P - Math.floor(P));
            var t2 = durationList[Math.floor(P)] - durationList[Math.floor(P) - 1];
            P = durationList[Math.floor(P) - 1] + (t1 * t2);
            P = Math.round(P * 100) / 100; // 2 digit decimal
            PT.push(P);
        }
    }
    return PT;
}

function quartile(durationList) {
    var QT = [];
    var len = durationList.length;

    for (var i = 0.25; i <= 0.75; i += 0.25) {
        var Q = i * (len + 1);                        // 1.25 ; 1 is index 0
        if (Q - Math.floor(Q) == 0) {
            QT.push(durationList[Q - 1]);
        }
        else if (Q < 1) {
            QT.push(durationList[0])
        }
        else if (Q > len) {
            QT.push(durationList[len - 1]);
        }
        else {
            var t1 = (Q - Math.floor(Q));
            var t2 = durationList[Math.floor(Q)] - durationList[Math.floor(Q) - 1];
            Q = durationList[Math.floor(Q) - 1] + (t1 * t2);
            Q = Math.round(Q * 100) / 100;
            QT.push(Q);
        }
    }
    return QT;
}

function median(durationList) {
    // middle value
    // sort
    // if len is odd middle is len / 2 
    // else len is even middle is process[len / 2] + process[(len / 2) - 1]
    var Med;
    var len = durationList.length
    if (len % 2 == 0)
        Med = (durationList[len / 2] + durationList[(len / 2) - 1]) / 2;
    else
        Med = durationList[Math.floor(len / 2)];
    return Med;
}

function stdev(durationList) {
    var Avg = average(durationList);
    var sum = 0;
    for (var i = 0; i < durationList.length; i++) {
        sum += ((durationList[i] - Avg) * (durationList[i] - Avg));
    }
    var std = Math.sqrt(sum / i);
    std = Math.round(std * 100) / 100; // 2 digit decimal
    return std;
}

function average(durationList) {
    var sum = 0;
    for (var i = 0; i < durationList.length; i++) {
        sum += durationList[i];
    }
    var avg = sum / i;
    avg = Math.round(avg * 100) / 100; // 2 digit decimal
    return avg;
}

function minMax(durationList) {
    var min = durationList[0];
    var max = durationList[0];
    for (var i = 0; i < durationList.length; i++) {
        if (durationList[i] > max) {
            max = durationList[i];
        }
        if (durationList[i] < min) {
            min = durationList[i];
        }
    }
    return [min, max];
}