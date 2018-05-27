local function display_webpage(socket,request)
  
   _, _, method, req, major, minor = string.find(request, "([A-Z]+) (.+) HTTP/(%d).(%d)");

   if(string.find(req,"/temperature")) then -- request made to temperature page
      
     socket:send("HTTP/"..major.."."..minor.." 200 OK\r\nContent-Type: text/html\r\nConnection: close\r\n\r\n")
     socket:send("<html><head></head>")
     socket:send("<body></body></html>")

   elseif (string.find(req,"/temperature.json")) then -- request made to temperature.json page
     
     local temps = getData()
     
     -- serve json
     socket:send("HTTP/"..major.."."..minor.." 200 OK\r\nContent-Type: application/json\r\nConnection: close\r\n\r\n"); 
     socket:send(temps);
     
   end

    socket:close()
    socket = nil
   
end


server = net.createServer(net.TCP)

server:listen(80,function(socket)
  socket:on("receive",display_webpage)
end)
