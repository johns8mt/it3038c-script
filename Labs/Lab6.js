var http = require("http")
var fs = require("fs")
var os = require("os")
var ip = require("ip")

name = os.hostname;


uptime = os.uptime
uptimeDays = Math.floor (uptime / 86400)
uptime = uptime - (uptimeDays * 86400);
upHours = Math.floor (uptime / 3600);
uptime = uptime - (upHours * 3600);
upMins = Math.floor (uptime / 60);
uptime = uptime - (upMins *60)
upSecs = Math.floor (uptime);

cpus = os.cpus(),
cpuNumber = cpus.length;
Memory = os.totalmem;
FreeMemory = os.freemem;
TotalMemory = Memory / 1000000;
FreeMemory = FreeMemory / 1000000;

var server = http.createServer(function(req,res){
    res.writeHead(200, {"Content-Type":"text/html"});
    res.end(
