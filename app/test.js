var PythonShell = require('python-shell');

var options = {
    mode: 'text',
    pythonOptions: ['-W', 'ignore']
};
var pyshell = new PythonShell('import.py', options);


pyshell.on('message', function (message) {
    console.log(message);
});