Flow: 
User goes to Site A (Client) 
User enters username and password 
Site A calls Site B (Server) resource /login which sets cookie in response 
Site A calls Site B resource /user which validates cookie sent in request and returns user details 
Site A displays user details 

Sequence diagram: 
Mermaid - link 



Scenarios: 
TPC (third-party cookie) disabled [chrome incognito] 
TPC enabled [chrome, firefox] 

Results: 
TPC disabled - Doesn't work. Browser blocks both setting TPC by server as well as sending TPC to server. 
TPC enabled - Works on both chrome and firefox.  
