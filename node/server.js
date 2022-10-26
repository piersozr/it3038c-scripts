const http = require("http");
const fs = require("fs");
const os = require("os");
const ip = require('ip');
const { uptime } = require("process");

http.createServer((req, res) => {
  if (req.url === "/") {
      fs.readFile("./public/index.html", "UTF-8", (err, body) => {
      res.writeHead(200, {"Content-Type": "text/html"});
      res.end(body);
    });
  } else if(req.url.match("/sysinfo")) {
    myHostName=os.hostname();
    myFreeMemory = os.freemem();
    let uptime = os.uptime;
    
    let uptime_days = Math.floor(uptime / (60*60*24));
    uptime -= Math.floor(uptime_days * (60*60*24));

    let uptime_hours = Math.floor(uptime / (60*60));
    uptime -= Math.floor(uptime_hours * (60 * 60));

    let uptime_minutes = Math.floor(uptime / (60));
    uptime -= Math.floor(uptime_minutes * (60));

    let uptime_seconds = Math.floor(uptime);

    let totalmem = Math.floor((os.totalmem/1024)/1024);
    let freemem = Math.floor((os.freemem/1024)/1024);
    let oscores = os.cpus().length;
    html=`
    
    <!DOCTYPE html>
    <html>
      <head>
        <title>Node JS Response</title>
      </head>
      <body>
        <p>Hostname: ${myHostName}</p>
        <p>IP: ${ip.address()}</p>
        <p>Server Uptime: Days:${uptime_days}, Hours:${uptime_hours}, Minutes:${uptime_minutes}, Seconds:${uptime_seconds} </p>
        <p>Total Memory: ${totalmem} MB</p>
        <p>Free Memory: ${freemem} MB</p>
        <p>Number of CPUs: ${oscores}</p>
      </body>
    </html>`
    res.writeHead(200, {"Content-Type": "text/html"});
    res.end(html);
  } else {
    res.writeHead(404, {"Content-Type": "text/plain"});
    res.end(`404 File Not Found at ${req.url}`);
  }
}).listen(3000);

console.log("Server listening on port 3000");