

//commit + push einer json datei, später ps datei
const jsonfile = require('jsonfile');
const moment = require('moment');
const simpleGit = require('simple-git');

const FILE_PATH = './project.py';

const DATE = moment().format();
//const DATE = moment().subtract(1, 'd').format();

const data = {
    date: DATE
}

jsonfile.writeFile(FILE_PATH, data, ()=>{
    simpleGit().add([FILE_PATH]).commit(DATE, {'--date': DATE}).push();
});

//dateien aus einer webseite extrahieren

