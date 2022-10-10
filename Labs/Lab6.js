var osutils = require("os-utils");

console.log("Platform: " + osutils.platform());
console.log("Number of CPUs: " + osutils.cpuCount());

osutils.cpuUsage(function(v) {
  console.log("CPU Usage (%) : " + v);
});

console.log("Total Memory: " + osutils.totalmem() + "MB");

console.log("Free Memory: " + osutils.freemem() + "MB");

console.log("System Uptime: " + osutils.sysUptime() + "ms");
