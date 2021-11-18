// Code as a for loop//
/*function raisinAlarm(cookie) {
    for (let i = 0; i < cookie.length; i++) {
        if (cookie[i] === "raisin") {
            return console.log("Raisin alert!");
        }
    }
    return console.log('All good!');
}*/
// code without emojis //
/*const raisinAlarm = (cookie) => {
    if (cookie.find(x => x === 'raisin')) {
        console.log("Raisin alert!");
    } else {
        console.log('All good!');
    }
}
raisinAlarm(['chocolate', 'raisin', 'chocolate', 'chocolate',]);
raisinAlarm(['chocolate', 'chocolate', 'chocolate', 'chocolate',]);
raisinAlarm(['chocolate', 'raisin', 'chocolate', 'chocolate',]);
raisinAlarm([]);*/
// Code with emojis //
const raisinAlarm = (cookie) => {
    if (cookie.find(x => x === '🍇')) {
        console.log("Raisin alert!");
    } else {
        console.log('All good!');
    }
}
raisinAlarm(['🍫', '🍇', '🍫', '🍫',]);
raisinAlarm(['🍫', '🍫', '🍫', '🍫',]);
raisinAlarm(['🍫', '🍇', '🍫', '🍫',]);
raisinAlarm([]);